## Cloud Deployment
Use the "AirQualityStream.py" Python Script.



# 1) Configure AWS Profile
    -- Not to show



# 2. Create Terraform Infrastructure
    -- look inside "terraform" directory



# 3. Dockerize the Environment
    -- look inside "dependencies" directory



# 4. Terraform Deployment

- terraform init & terraform validate
![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/fb969d63-b872-47c8-81e4-8019a2d589a6)

- terraform plan
![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/3e0ceedc-3816-411c-a936-30d02f484dc4)

- terraform apply
![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/dfecdfee-75dc-4112-a96a-3d32b2762f6a)



# 4. Create a kafka topic
![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/a189df20-6124-42a7-b580-e2c3ba626981)

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/4001bd45-5841-4835-905d-760abeb25ff0)




# 5. Export Files to the Amazon S3 Bucket
![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/2bcb69b4-55b0-4438-ad08-8aaec2ed0479)

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/16dbbe3f-6908-40cd-9287-d044efa129cf)



# 6. Initiate a Spark Job on Amazon EMR
![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/e754a014-5114-4d96-ad14-005445d47f97)

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/b8e5a382-8910-4cdd-999d-1133309756eb)

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/b1d40fd6-9930-4745-a51e-60598c211274)

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/9b70e525-ba3b-49a4-9d56-f14ace855266)

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/cc0cc101-29b2-48da-bd4f-aa744b4aacfe)

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/944b62a7-8611-4dea-99f2-8b7577f9d9af)



# 7. Monitor and Verify Deployment :
All instances are functioning properly.
The job has been initiated successfully.
However, the Spark job failed after running successfully. Further investigation and resolution are required.



