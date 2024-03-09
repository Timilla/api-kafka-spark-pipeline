#  Option1 - Air Quality Streaming Pipeline

## Description
This repository contains the source code for the Air Quality Streaming Pipeline. The pipeline retrieves real-time data from the OpenWeatherMap API, ingests it into a Kafka topic,
processes it using Apache Spark Structured Streaming and stores the results for subsequent analysis and visualization.

This project is a proof-of-concept founded upon an imagined real-world application of the pipeline [Context.md](Context.md)..


![image](https://github.com/Timilla/api-kafka-spark/assets/95149290/2476cc03-d04a-48e6-b30d-e29be2aae3fe)




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




## Repository structure
```markdown

AirQualityPipeline/
│
├── .venv/
│
├── dependencies/
│   ├── Dockerfile
│   └── pyspark_airquality.tar.gz
│
├── results/
│
├── terraform/
│   ├── .terraform/
│   ├── .terraform.lock.hcl
│   ├── bastion.tftpl
│   ├── config.tf
│   ├── data.tf
│   ├── main.tf
│   ├── outputs.tf
│   ├── terraform.tfstate
│   ├── terraform.tfstate.backup
│   └── variables.tf
│
├── AirQualityStream.py
├── AirQualityStream_Local.py
├── requirements.txt
├── README.md
├── Context.md
├── Local.md
└── Cloud.md
```



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



## Cloud Deployment
follow this step-by-step guide for deploying the solution on Amazon Web Services using Terraform :

1. **Configure AWS Profile** :
   - Sign in to your AWS account and create an IAM user with administrative permissions.
   - Generate the access key and secret key for the IAM user.
   - Configure AWS profile on your local machine by running the following command in the terminal:
   ```bash
   aws configure --profile stream_dsti
   ```


2. **Create Terraform Infrastructure** :
   - Create a new Terraform repository with the necessary files (config.tf, variables.tf, main.tf, data.tf, outputs.tf, bastion.tftpl).
   - Specify the necessary configurations, including AWS resources (MSK, EMR, S3 bucket), networking settings, IAM roles, etc.


3. **Dockerize the Environment** :
   - Create a new repository named "dependencies" and add a Dockerfile inside it to configure the environment encapsulation.
   - Specify the necessary dependencies and installation steps in the Dockerfile.
   - Build the Docker image using the following commands:
   ```bash
   docker build -t pyspark_airquality .
   docker buildx build --output type=local,dest=. .
   ```


4. **Terraform Deployment** :
   - Navigate to your Terraform repository and initialize Terraform :
   ```bash
   terraform init
   ```
   - Validate the Terraform configuration :
   ```bash
   terraform validate
   ```
   - Plan the deployment to review the changes that will be applied :
   ```bash
   terraform plan -var="profile=stream_dsti"
   ```
   - Apply the Terraform changes to deploy the infrastructure :
   ```bash
   terraform apply -var="profile=stream_dsti"
   ```
     When the deployment is finished, information about the remote MSK hostname is printed to the terminal.


4. **Create a kafka topic** :
   - Access the AWS Management Console and navigate to the deployed MSK cluster, manually create the Kafka topic under the desired broker.
   - Alternatively, connect to the Amazon MSK cluster locally using the previously obtained MSK hostname :
   ```bash
   ssh ec2-user@54.73.144.82 -i cert.pem
   ```
   -  Check for running brokers :
   ```bash
   more bootstrap-servers
   ```
   -  Choose the broker where to create the topic and proceed with topic creation :
   ```bash
   kafka-topics.sh --bootstrap-server b-1.groupmsk.3ecnii.c3.kafka.eu-west-1.amazonaws.com:9092 --create --topic weather_data_topic --partitions 1 --replication-factor 1
   ```

5. **Export Files to the Amazon S3 Bucket** :
   - Upload the local environment dockerized file to the artifacts folder and the the Python script to code folder, both isnide the created S3 bucket instance. You can perform this task manually or by running :
   ```bash
   aws s3 cp pyspark_airquality.tar.gz s3://airquality-dsti-bucket/artifacts/pyspark_airquality.tar.gz
   aws s3 cp AirQualityStream.py s3://airquality-dsti-bucket/code/AirQualityStream.py
   ```


6. **Initiate a Spark Job on Amazon EMR** :
   - Navigate to the AWS Management Console and access the EMR studio.
   - Within the EMR Studio, create a new EMR serverless application.
   - Submit a Spark job using the spark-submit command. Ensure to specify the necessary parameters such as the path to dependencies, the path to the PySpark code, and its arguments (S3 bucket location, broker name, topic name) etc.
   - Update the EMR default role policy allowing access to the MSK cluster.



7. **Monitor and Verify Deployment** :
   - Monitor the resources in the AWS Management Console to ensure everything is functioning as expected.
   - Test the deployed solution to verify that data is being processed correctly and that the desired outcomes are achieved.
  

  
The AWS cloud Application job run details are available for consultation in [Cloud.md](Cloud.md).





## Developer Guide
For upcoming work :
- Enhance the pipeline by addressing any limitations and integrating additional parameters.
- Implement CI/CD using GitHub Actions.
- Investigate and resolve the AWS failure Spark job.



## Authors
- Othmane Tantaoui (othmane.tantaoui@edu.dsti.institute)
- Omar Ait Ali (omar.aitali@edu.dsti.institute)
- Anwar Timilla (anwar.timilla@edu.dsti.institute)
