# Local Deployment
Use the "AirQualityStream_Local.py" Python Script.


## 1) Install Dependencies

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/c55acc4a-fffd-4a7a-a7fe-11c17cc02dbc)



## 2) Start Zookeeper

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/7c9f9c42-b101-4697-a808-877afa97a6a9)




## 3) Start Kafka Broker

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/08556ccc-93c6-434f-88a5-4c6bb17bc97b)




## 4) Create a Kafka Topic

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/01b801af-be63-4dcb-9e60-2dbe50a99680)




## 5) Run the Pipeline
- Add arguments to the Python script :

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/28fc43cc-8058-4e42-ab38-b3498b8b6798)

- Output AirQuality informations to the console :

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/a27cc1ce-825c-4e53-a656-cda9f84e5019)



- Store AirQuality informations into a .csv file for each time epoch (2 time steps configuration here) :

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/9d3ba523-853a-406c-8a69-65945453b932)

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/ad61a2b1-47be-4ace-993c-6e5580932838)

![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/4e647567-c46d-41db-aaef-d471a783bce3)
