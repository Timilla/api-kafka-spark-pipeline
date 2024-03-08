import requests
import sys
import os
import math
import time
import json

from confluent_kafka import Producer

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, udf, when
from pyspark.sql.types import FloatType, StructField, StructType


# Accessing the environment variable
api_key = os.environ.get('API_KEY')

# Using the API key
if not api_key:
    print("API key is not set in environment variables")


# Define fixed parameters
AQI_optimal_weather = 60  # Paris's mean AQI (Air Quality Index), in optimal weather conditions.
city = "Paris"  # Set the city for weather fetching


# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        weather_data = response.json()
        print("Weather data successfully retrieved from OpenWeather API")
        return weather_data
    except requests.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return None


# Function to produce weather data to Kafka topic
def produce_to_kafka(producer, kafka_topic, weather_data):
    producer.produce(kafka_topic, key="weather", value=json.dumps(weather_data), callback=delivery_report)
    producer.poll(0)  # Check if the message is delivered to the topic


# Delivery report callback function
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


# Function to calculate AQI adjusted value
def calculate_AQI_adjusted(temperature, humidity):
    AQI_adjusted = AQI_optimal_weather * (1 + (temperature - 10) / 40) * math.exp(
        ((humidity - 50) ** 2) / (2 * 50 ** 2))
    return AQI_adjusted


# Function to determine AQ alert level
def determine_AQ_AlertLevel(AQI_value):
    return when(AQI_value <= 50, "Good") \
        .when((AQI_value > 50) & (AQI_value <= 100), "Moderate") \
        .when((AQI_value > 100) & (AQI_value <= 150), "Unhealthy for Sensitive Groups") \
        .when((AQI_value > 150) & (AQI_value <= 200), "Unhealthy") \
        .when((AQI_value > 200) & (AQI_value <= 300), "Very Unhealthy") \
        .otherwise("Hazardous")


# Function to determine AQ alert color
def determine_AQ_AlertColor(AQI_value):
    return when(AQI_value <= 50, "Green") \
        .when((AQI_value > 50) & (AQI_value <= 100), "Yellow") \
        .when((AQI_value > 100) & (AQI_value <= 150), "Orange") \
        .when((AQI_value > 150) & (AQI_value <= 200), "Red") \
        .when((AQI_value > 200) & (AQI_value <= 300), "Purple") \
        .otherwise("Maroon")


def main(output_path, kafka_bootstrap_servers, kafka_topic):
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("AirQualityStream") \
        .config("spark.streaming.uninterruptibleThread", "true") \
    .getOrCreate()

    # Initialize Kafka producer
    producer = Producer({"bootstrap.servers": kafka_bootstrap_servers})

    # Create streaming DataFrame from Kafka
    kafka_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
        .option("subscribe", kafka_topic) \
        .load()

    # Retrieve timestamp and convert value column to string
    kafka_stream_df = kafka_df.selectExpr("CAST(value AS STRING)", "CAST(timestamp AS TIMESTAMP) as time")

    # Parse JSON data from Kafka messages
    schema = StructType([
        StructField("temperature", FloatType(), True),
        StructField("humidity", FloatType(), True)
    ])
    parsed_stream_df = kafka_stream_df.select(from_json(col("value"), schema).alias("data"), "time")

    # Register UDF to calculate AQI adjusted value
    calculate_AQI_adjusted_udf = udf(calculate_AQI_adjusted, FloatType())

    # Calculate AQI adjusted value for each record
    AQ_stream_df = parsed_stream_df \
        .withColumn("AirQuality_Index", calculate_AQI_adjusted_udf(col("data.temperature"), col("data.humidity"))) \
        .withColumn("AirQuality_Alert_Level", determine_AQ_AlertLevel(col("AirQuality_Index"))) \
        .withColumn("AirQuality_Alert_Color", determine_AQ_AlertColor(col("AirQuality_Index"))) \
        .select("time", "data.temperature", "data.humidity", "AirQuality_Index", "AirQuality_Alert_Level",
                "AirQuality_Alert_Color")

    # Write the results to the output using foreachBatch
    def write_to_file(df, epoch_id):
        print(f"Output file updated. Epoch ID: {epoch_id}")
        if df.count() > 0:
            # Create a DataFrame with column names as the first row
            column_names = df.schema.names
            header_row = spark.createDataFrame([column_names], column_names)
            # Union the header row with the DataFrame
            df_with_header = header_row.union(df)
            # Write to CSV
            df_with_header.coalesce(1).write.mode("overwrite").csv(output_path + f"/epoch_{epoch_id}")

    # Start the streaming query with a trigger interval of 60 seconds
    query = AQ_stream_df.writeStream \
        .foreachBatch(write_to_file) \
        .trigger(processingTime="300 seconds") \
        .outputMode("update") \
        .start()
    # Output AQ information to console
    # console_query = AQ_stream_df.writeStream \
    #     .outputMode("update") \
    #     .format("console") \
    #     .start()

    # Start fetching weather data and producing to Kafka every 5 seconds
    while True:
        weather_data = fetch_weather_data(api_key, city)
        if weather_data:
            temperature = weather_data.get("main", {}).get("temp")
            humidity = weather_data.get("main", {}).get("humidity")

            if temperature is not None and humidity is not None:
                data = {"temperature": temperature, "humidity": humidity}
                produce_to_kafka(producer, kafka_topic, data)
            else:
                print("Temperature or humidity data not available")
        else:
            print("No weather data available.")

        time.sleep(20)  # Fetch weather data every 20 seconds


if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Invalid arguments, please supply <output_path> <kafka_bootstrap_servers> <kafka_topic>")
        sys.exit(1)

    # The output path, Kafka bootstrap servers, and Kafka topic are passed as arguments
    output_path = sys.argv[1]
    kafka_bootstrap_servers = sys.argv[2]
    kafka_topic = sys.argv[3]

    main(output_path, kafka_bootstrap_servers, kafka_topic)
