# Senior Data Infra Engineer Assessment

## Introduction:
In this assessment, you will be tasked with designing and implementing an Airflow Directed Acyclic Graph (DAG) that demonstrates your skills as a senior data infra engineer. The DAG will read metadata from Kafka, retrieve data from S3, perform aggregation tasks on the data with Spark, and store the aggregated results in a SQL database.

## Objective:
Your objective is to create a robust and maintainable Airflow DAG that achieves the following:

- Consumes metadata from Kafka topics.
- Fetches data files from S3.
- Performs data aggregation tasks on the fetched data with Spark.
- Stores the aggregated data in a SQL database.

## Requirements:

1. **Kafka Setup:**
   - You can use a mock Kafka producer to simulate metadata. It doesn't need to be a live Kafka instance.

2. **S3 Data Retrieval:**
   - Retrieve data files from a specified S3 bucket or directory.
   - Process the data files to perform the required aggregation.

3. **Aggregation Tasks:**
   - Implement appropriate data aggregation tasks that showcase your expertise in data transformation and manipulation.
   - For example, aggregate data by date, calculate sums, averages, etc.
   - Use Spark to perform the aggregation tasks.
   - You can use a local Spark instance.

4. **SQL Database:**
   - Store the aggregated data in a SQL database.
   - You can use SQLite, MySQL, PostgreSQL, or any other suitable SQL database.

5. **Airflow DAG:**
   - Design an Airflow DAG that orchestrates the entire process.
   - Utilize the relevant operators provided by Airflow (e.g., PythonOperator, BashOperator, S3FileTransformOperator, Sensors etc.).
   - Ensure that the DAG is fault-tolerant and handles retries appropriately.

## Bonus (Optional):

6. **Configuration and Parameters:**
   - Utilize Airflow's configuration files to manage DAG parameters, credentials, and other settings.
   - Make use of environment variables or Airflow's variable feature for sensitive information like credentials.

7. **Documentation:**
   - Include clear and concise comments within your DAG to explain the purpose of each task and any relevant details.
   - Provide a high-level explanation of your approach and design decisions in a README file.

8. **Include Swagger documentation for the following APIs:**

    - Delete API: A RESTful API to delete a specific run of the DAG.
    - Run API: A RESTful API to manually trigger a run of the DAG.
    - Stop API: A RESTful API to stop an ongoing execution of the DAG.

    In addition, create a microservice that handles these APIs. The microservice should include the following steps:

    1. Choose a programming language and framework.
    2. Create API endpoints for delete, run, and stop.
    3. Integrate Swagger documentation for the APIs.
    4. Implement the logic to interact with Airflow for DAG operations.
    5. Dockerize the microservice.
    6. Deploy the microservice to a hosting platform.
    7. Test, debug, and document your code.

## Evaluation Criteria:
Your solution will be evaluated based on the criteria outlined in the initial assessment.

## Submission:
Please provide a Git repository link containing your DAG code, any necessary configuration files, and a README explaining your solution and design choices.

Feel free to reach out if you have any questions or need further clarification. Good luck!
