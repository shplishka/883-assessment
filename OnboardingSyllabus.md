# 883 Team Onboarding Syllabus

## Week 1: Introduction to Data Ops and Hadoop Ecosystem
- **Chapter 1:** Overview of Data Ops in the Modern Data Landscape
- **Chapter 2:** Deep Dive into Hadoop Ecosystem Components (Hive, Oozie, HDFS, YARN, Impala)
- **Exercise:** Set up a local Hadoop cluster for hands-on experience in Cloudera Cloud Platform.
- **Showcase:** Explain the core concept of Hadoop ecosystem components.

## Week 2: Proficiency in Spark

- **Chapter 3:** Spark Essentials and Best Practices
In this chapter, we will delve into the fundamental concepts of Apache Spark. Topics covered will include:
    - [Introduction to Apache Spark](https://spark.apache.org/)
    - Understanding the Spark ecosystem components: Spark Core, RDD, Shuffle, Transformations, Actions, Spark SQL and Spark Streaming.
    - Spark architecture and its role in distributed data processing.

- **Exercise:** Develop a Sample Spark Job
Hands-on experience is crucial for mastering Spark. We will guide you through the process of developing a sample Spark job using: [Spark's official documentation](https://spark.apache.org/docs/latest/)
    - Python programming languages for Spark job development.
    - Executing and validating the Spark job locally.

- **Showcase:** Present Best Practices for Optimizing Spark Jobs
Optimizing Spark jobs is essential for efficient data processing. During the showcase, we will discuss and demonstrate:

    - [Spark Performance Tuning](https://spark.apache.org/docs/latest/tuning.html)
    - Best practices for configuring Spark applications.
    - Strategies for handling large datasets and improving job performance.


## Week 3: Mastering Apache Airflow for Workflow Orchestration

- **Chapter 4:** Mastering Apache Airflow for Workflow Orchestration
This chapter focuses on mastering Apache Airflow, an open-source platform to programmatically author, schedule, and monitor workflows. Topics covered include:

    - [Introduction to Apache Airflow](https://airflow.apache.org/)
    - Understanding the architecture and components of Airflow.
    - Exploring the Airflow web UI and CLI for workflow management.
    - Defining key concepts like DAGs, Operators, and Sensors in Airflow.

- **Exercise:** Create an Airflow DAG for Orchestrating a Data Workflow
In this hands-on exercise, you will learn to:

    - Design an Airflow DAG to represent a data workflow.
    - Use different Operators (e.g., PythonOperator, BashOperator) to define tasks within the DAG.
    - Schedule and execute the DAG to orchestrate the defined workflow.

- **Showcase:**  Explain Key Concepts of Airflow DAGs
During the showcase, we will dive deeper into Airflow DAGs, discussing:

    - [Airflow Concepts and Terminology](https://airflow.apache.org/docs/apache-airflow/stable/concepts/index.html)
    - DAG structure and its components.
    - Task dependencies and execution order.
    - Monitoring and logging capabilities in Airflow.


## Week 4: DevOps in Kubernetes
- **Chapter 5:** Kubernetes Fundamentals for Data Ops using "zero to hero" Openshift labs.
- **Chapter 6:** Helm for Kubernetes Package Management using "Advenced labs" Openshift labs.
- **Exercise:** Deploy a Spark application using Helm on a Openshift cluster.
- **Showcase:** Present the advantages of Kubernetes in a data ops context and discuss Helm's role in managing Kubernetes applications.

## Week 5: Iceberg and Trino in Data Operations
- **Chapter 7:** Managing Data with Iceberg
- **Chapter 8:** Exploring Trino as a Query Engine
- **Exercise:** Implement Iceberg for data management and work with Trino for querying data efficiently - create mini parquet merager.
- **Showcase:** Showcase the benefits of using Iceberg for managing evolving datasets and discuss Trino's advantages as a query engine.

## Week 6: Operators and Controllers in Kubernetes
- **Chapter 9:** Understanding Kubernetes Operators
- **Chapter 10:** Custom Controllers for Data Ops
- **Exercise:** Develop a custom Kubernetes controller to handle ConfigMap upgrades in given namespaces.
- **Showcase:** Explain the concept of Kubernetes operators and their role VS contorllers.

## Week 7: Real-world Project Simulation
- **Chapter 11:** Simulating Real-world Data Ops Projects
- **Chapter 12:** Troubleshooting and Debugging Techniques
- **Exercise:**  Do [Final Exercise](FinalExercise.md) and present the solution.
- **Showcase:** Share insights gained from the simulation and discuss troubleshooting strategies.

## Week 8: Best Practices and Spark Optimization
- **Chapter 13:** Best Practices and Spark Optimization in Spark metrics and Spark ui analysis
- **Chapter 14:** Performance Spark Optimization Strategies
- **Exercise:** Optimize a Spark job for better performance and efficiency.
- **Showcase:** Present the optimized Spark job and discuss the strategies employed for performance improvement.

## Week 9: Advanced Airflow Concepts and Practical Implementation
- **Chapter 15:** Airflow Cluster Setup and Configuration
- **Chapter 16:** Writing Custom Airflow Operators
- **Exercise:** Set up an Airflow cluster and write a custom operator to interact with an external system.
- **Showcase:** Demonstrate the configured Airflow cluster and showcase the custom operator in action.

## Week 10: Documentation and Knowledge Sharing
- **Chapter 17:** Importance of Documentation in Data Ops
- **Chapter 18:** Effective Knowledge Sharing within the Team
- **Exercise:** Create documentation for a sample project and present it to the team.
- **Showcase:** Lead a discussion on the significance of documentation and effective knowledge sharing practices.

## Continuous Learning and Specialized Tracks
- Encourage continuous learning in areas like cloud integration, security, and emerging technologies.
- Provide access to resources and support for team members to specialize in areas of interest.
