## Cloud Deployment
Use the "AirQualityStream.py" Python Script.

# 1. Terraform Deployment

- terraform init & terraform validate

![image](https://github.com/Timilla/api-kafka-spark-pipeline/assets/104758161/7c10f3d2-6306-4d52-96eb-2c8cc7b5ff4e)


- terraform plan

![image](https://github.com/Timilla/api-kafka-spark-pipeline/assets/104758161/d67205fe-7949-493e-8868-bd41026be6e7)





- terraform apply

![image](https://github.com/Timilla/api-kafka-spark-pipeline/assets/104758161/8f9f3b98-eb55-4cd7-b543-ac0b40efc98a)


# 2. Create a kafka topic
 
 ![image](https://github.com/Timilla/api-kafka-spark-pipeline/assets/104758161/f3523379-be7e-4923-b2b0-6ac8f3770ca3)
![image](https://github.com/Timilla/api-kafka-spark-pipeline/assets/104758161/24254791-7bd0-4339-9678-33141a6892e8)


# 3. Export Files to the Amazon S3 Bucket

![image](https://github.com/Timilla/api-kafka-spark-pipeline/assets/104758161/bef956d3-e279-4504-9912-3f9d32988b6a)
![image](https://github.com/Timilla/api-kafka-spark-pipeline/assets/104758161/23a767c9-9582-4b0b-991c-1719e7da2428)

 
# 4. Initiate a Spark Job on Amazon EMR
 
 
![image](https://github.com/Timilla/api-kafka-spark-pipeline/assets/104758161/70eb7ce5-09c1-4a1f-8633-b60bbb96fe93)

![image](https://github.com/Timilla/api-kafka-spark-pipeline/assets/104758161/afac080b-f604-448d-8c92-35b6fd5769d7)

![image](https://github.com/Timilla/api-kafka-spark-pipeline/assets/104758161/ab377e67-73e2-43a8-bb9f-188ba885020f)

![image](https://github.com/Timilla/api-kafka-spark-pipeline/assets/104758161/dba9a3f0-d3eb-4c89-b2ab-e5616589d592)
 
![image](https://github.com/Timilla/api-kafka-spark-pipeline/assets/104758161/e847db35-bf6b-4322-8678-6826b07164cd)


# 5. Monitor and Verify Deployment :
All instances are functioning properly.
The job has been initiated successfully.
However, the Spark job failed after running successfully. Further investigation and resolution are required.
