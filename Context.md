# Project Context

## Goal
Our primary objective is to develop a robust pipeline for real-time air quality monitoring in the Île-de-France region, aligning with specific requirements outlined by our customer, the regional climate surveillance agency. The ultimate goal is to create a dynamic air quality map.

## Current Work
Currently, our efforts are focused on the proof-of-concept phase, where we are establishing the foundational elements of the pipeline.

## Customer Specifications
1. **Dynamic Air Quality Map:**
   - The pipeline aims to generate a dynamic air quality map, capturing one image every 2 hours. This approach allows for differentiation of air quality across different times of the day, weekdays, and seasons throughout the entire year.
   
2. **High-Frequency Data Updates:**
   - To meet the customer's need for more granular data, we are delivering CSV file epochs with information stored every minute. This high-frequency update enables the detection of potential anomalies and micro-perturbations.
   
3. **Calculation and Alerting:**
   - A calculation formula for the AQI is provided by the customer, necessitating data processing during the stream. For the proof-of-concept (POC), a simplified formula tailored to the fetched data is utilized.

## Simplifications for the POC Phase
1. **Focus on Paris:**
   - To reduce data volume and complexity.

2. **Data Fetching:**
   - Fetching exclusively temperature and humidity data from the OpenWeather API. We acknowledge that other parameters may have more significant impacts. However, for accessibility, we are focusing on temperature and humidity.

3. **AQI Calculation:**
   - Utilizing a simple approximate formula based on temperature and humidity (and some constants) for AQI calculation and subsequent air quality alert color, providing a visual representation of air quality conditions.

4. **Stream Optimization:**
   - Implementing a shortened stream timing of 20 seconds to fetch weather information and 2 minutes epoch to store CSV files, reducing testing time and costs during.

## Future Works
As we move forward, our plan is to refine and expand the pipeline, addressing limitations, and incorporating additional parameters.
