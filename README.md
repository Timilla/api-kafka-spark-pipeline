#  Option1 - Air Quality Streaming Pipeline

 

## Description

This repository contains the source code for the Air Quality Streaming Pipeline. The pipeline retrieves real-time data from the OpenWeatherMap API, ingests it into a Kafka topic,

processes it using Apache Spark Structured Streaming and stores the results for subsequent analysis and visualization.

 

This project is a proof-of-concept founded upon an imagined real-world application of the pipeline [Context.md](Context.md)..

 

 

## Prerequisites

For deploying the solution within your on-premises infrastructure, you will need:

- A local development environment with Python installed.

- Internet access to fetch weather data from the OpenWeatherMap API.

- Kafka installed and configured locally for message ingestion.

- Apache Spark installed and configured for local streaming processing.

- Installation of the necessary Python libraries, which can be found in the requirements.txt file

 

To deploy the solution in the AWS cloud environment using Terraform, you will need:

- AWS account to provision cloud resources.

- Terraform to manage the infrastructure as code.

- Docker Desktop for containerizing the environment.

- AWS Command Line Interface (CLI) for interacting with AWS services from the command line.

 

 

## Local Deployment

To deploy the solution locally, follow these steps:

 

1. **Install Dependencies** :

   - Create a virtual environment and install dependencies from `requirements.txt`:

   ```bash

   pip install -r requirements.txt

   ```

 

2. **Start Zookeeper** :

   - Zookeeper is required for Kafka to manage and coordinate distributed systems. It helps Kafka perform tasks such as electing leaders, coordinating tasks, and managing configurations.

   ```bash

   C:\kafka\bin\windows\zookeeper-server-start.bat C:\kafka\config\zookeeper.properties

   ```

 

3. **Start Kafka Broker (Server)** :

   - The Kafka broker acts as the central component in the pipeline, managing the storage and retrieval of messages. It ensures fault tolerance and high availability of data.:

   ```bash

   C:\kafka\bin\windows\kafka-server-start.bat C:\kafka\config\server.properties

   ```

 

4. **Create a Kafka Topic** :

   - This step involves creating a Kafka topic named 'weather_data_topic' where the weather data will be ingested. The topic creation specifies the replication factor and number of partitions..

   ```bash

   C:\kafka\bin\windows\kafka-topics.bat --create --topic weather_data_topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1

   ```

 

5. **Run the pipeline** :

   - Execute the PySpark script 'AirQualityStream_Local.py' which processes the weather data stream. The script is encoded into one 'main.py' file for simplicity and easy deployment, accepting arguments for the output path, Kafka bootstrap servers, and Kafka topic:

   ```bash

   python AirQualityStream_Local.py "C:\Users\Vador\Desktop\DSTI\Data pipe2\Weather_project\pythonProject1\results" "localhost:9092" "weather_data_topic"

   ```

 

The local run details are available for consultation in [Local.md](Local.md).
