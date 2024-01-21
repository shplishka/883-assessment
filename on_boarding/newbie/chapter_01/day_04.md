# Day 04 - Introduction to Data concept & Hadoop Ecosystem :elephant::elephant:

## Goals:
- Gain a foundational understanding of the Hadoop ecosystem.
- Explore key components and their roles in big data processing.
- Make connections between the Hadoop ecosystem and real-world use cases.
- Develop a high-level understanding of the Hadoop ecosystem and its role in big data processing.
- Familirize yourself with the Hadoop ecosystem and its role in big data processing.
- Continue to work with time estimation and planning.

:warning: **Note:**
- This is a self-study day, it is important to be able to work independently and manage your time.
- A lot of newbies have a problem with self-study and time management, so breath and take your time to plan your day carefully.
- Be aware of the importance of time management. Plan your time 
and tasks, and try to stick to your plan. If you are not able to finish the tasks in the time you have planned, you should discuss it with your mentor, maybe you learn more then you should.

**Total Time:** 8.5 hours


## Chapter 7: Apache HBase
**Est. Time:** 1.5 hours
- [Apache HBase](https://hbase.apache.org/)
### Core Concepts

#### 1. **Table:**
- Fundamental data storage unit in HBase, similar to a table in a relational database.
- Tables are distributed across the cluster and consist of rows and columns.

#### 2. **Row Key:**
- Unique identifier for each row in an HBase table.
- Determines the physical storage location of the data in the distributed environment.

#### 3. **Column Family:**
- Groups of related columns stored together for efficient retrieval.
- Defined at the table level and must be declared upfront.

#### 4. **Column Qualifier:**
- Part of a column that further qualifies the data within a column family.
- Combined with the column family and row key, it forms a unique cell in the table.

#### 5. **Cell:**
- Intersection of a row, column family, and column qualifier.
- Stores the actual data along with a timestamp.

#### 6. **HFile:**
- The underlying storage format for HBase tables.
- Represents the sorted and indexed form of the data on disk.

#### 7. **Region:**
- A contiguous range of rows stored together in an HBase table.
- Tables are horizontally partitioned into regions to enable parallel processing.

#### 8. **Region Server:**
- Hosts one or more regions and manages read and write requests for those regions.
- Distributes data across regions based on the row key.

#### 9. **ZooKeeper:**
- Coordinates and manages distributed components in HBase.
- Helps in leader election, synchronization, and distributed configuration.

#### 10. **Coprocessors:**
- Custom user code that can be executed on HBase servers.
- Provides the ability to perform operations close to the data.

#### 11. **Mob (Medium Object):**
- A storage feature in HBase for optimizing the storage of large cells (typically larger than 100KB).
- MOBs are stored separately from the normal cell data in a special MOB storage area to prevent large cells from impacting the performance of small cells.

#### 12. **WAL (Write-Ahead Log):**
- A log file where HBase records all changes to data before they are written to the actual storage.
- The WAL ensures data integrity and allows the system to recover from failures by replaying the log entries.

#### 13. **Compaction (Major and Minor):**
- A background process in HBase that reorganizes data to improve read performance and reclaim space.
   - **Minor Compaction:** Merges smaller HFiles into larger ones, reducing the number of files and improving read performance.
   - **Major Compaction:** Merges all HFiles in a region, removing deleted and expired cells. This process also rewrites data according to the latest schema, ensuring data consistency and optimal storage usage.

### **Real-World Use Cases:**

- **Real-time Big Data Access:** HBase excels in providing low-latency access to large datasets, making it suitable for real-time applications.
- **Time-Series Data:** Well-suited for scenarios involving time-series data due to its efficient storage and retrieval mechanisms.
- **Scalable and Distributed Storage:** HBase scales horizontally, making it suitable for handling massive amounts of data across a distributed environment.
Certainly! Here are the three key reasons in Markdown format:

- **Linear Scalability:** HBase is designed for horizontal scalability, allowing organizations to easily scale their clusters by adding more nodes. This ensures consistent performance as data volumes grow, making it suitable for large-scale applications.

- **Low Latency:** HBase is optimized for low-latency data access, making it a strong choice for real-time applications where quick retrieval and updates are crucial. Its architecture enables fast responses to queries, making it ideal for use cases with stringent latency requirements.

- **Integration with Hadoop Ecosystem:** HBase seamlessly integrates with other components of the Hadoop ecosystem, providing a unified platform for storing, processing, and analyzing data. This integration simplifies the development and maintenance of big data pipelines and analytics workflows.


- **Use Case:**
  - Predicting customer churn by analyzing user behavior and subscription patterns to proactively address potential cancellations.

- **Real Example:**
  - Netflix utilizes Apache Spark MLlib for machine learning tasks, including customer churn prediction. By analyzing viewing habits, engagement metrics, and other relevant data, Netflix can identify users at risk of churning and take personalized actions to retain subscribers.


## Chapter 8: Apache Kafka
**Est. Time:** 0.5 hour
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)

### Core Concepts:

#### 1. **Topics:**
   - Kafka organizes data into topics, which represent feeds of messages. Producers publish messages to topics, and consumers subscribe to topics to process those messages.

#### 2. **Partitions:**
   - Topics can be divided into partitions, allowing for parallel processing of messages. Each partition is an ordered and immutable sequence of records.

#### 3. **Brokers:**
   - Kafka brokers are servers that store data and serve client requests. They manage the storage and retrieval of messages, as well as the communication between producers and consumers.

#### 4. **Producers:**
   - Producers are responsible for publishing messages to Kafka topics. They send messages to specific topics, and Kafka ensures that these messages are distributed across partitions.

#### 5. **Consumers:**
   - Consumers subscribe to topics and process messages. They can maintain their own offset, indicating the position in the partition from which they have consumed messages.

#### 6. **Consumer Groups:**
   - Consumers can be organized into consumer groups, allowing multiple instances to work together to consume messages from a topic. Each consumer in a group processes a different subset of the partitions.

#### Real-World Use Cases:

1. **Log Aggregation:**
   - *Core Concept Applied:* Topics and Partitions
   - *Use Case:* Imagine a bustling library of online experiences. **LinkedIn** employs Kafka to aggregate logs, creating a comprehensive anthology of user interactions. Each log type is a distinct section, and Kafka partitions ensure parallel processing, turning logs into valuable stories for platform enhancement.

2. **Event Sourcing:**
   - *Core Concept Applied:* Producers and Topics
   - *Use Case:* Picture an eventful journey with **Uber**, where every ride is a story. Kafka captures and replays these events, creating a historical record. The events (chapters) are written by various producers, and Kafka's topics maintain the narrative's integrity for accurate retrospection.

3. **Real-Time Data Processing:**
   - *Core Concept Applied:* Producers, Consumers, and Topics
   - *Use Case:* Enter the fast-paced world of social media at **Twitter**. Kafka processes and analyzes tweets in real-time, crafting a dynamic narrative of trending topics, user sentiments, and global conversations—a real-time storybook that captivates millions.

4. **Microservices Communication:**
   - *Core Concept Applied:* Producers, Consumers, and Topics
   - *Use Case:* Journey into the realm of digital streaming with **Netflix**. Kafka acts as the communication backbone between microservices, allowing seamless interaction. Each microservice contributes to the collective storyline, enabling scalable and fault-tolerant storytelling in the digital entertainment saga.

## Chapter 9: Apache Impala
**Est. Time: 1 hours**

### Core Concepts
1. **Impala Daemon:**
   - Fundamental processing unit in Impala, responsible for executing queries and managing data distribution.
   - Impala daemons are distributed across the cluster to ensure parallel processing.
2. **Table:**
   - Similar to a table in a relational database, tables in Impala store structured data.
   - Tables can be external, managed, or virtual, each with its own characteristics.
3. **Schema:**
   - A blueprint that defines the structure of tables and their columns in Impala.
   - Schemas help maintain data integrity and organization within the database.
4. **SQL Support:**
   - Impala supports SQL-92 and SQL-2003 standards, allowing users to write complex queries.
   - It also offers various SQL extensions to optimize query performance.
5. **Query Execution:**
   - Impala uses a massively parallel processing (MPP) architecture to execute queries efficiently.
   - Queries are distributed across multiple Impala daemons for faster execution.
6. **Data Formats:**
   - Impala supports various file formats like Parquet, Avro, and ORC for efficient data storage and retrieval.
   - Choosing the right data format is crucial for query performance.
7. **Catalog Service:**
   - Manages metadata about tables, schemas, and other database objects.
   - Helps optimize query planning and execution by storing essential metadata.
8. **Query Coordinator:**
   - Coordinates query execution and optimization across the Impala cluster.
   - Decides how to distribute queries to Impala daemons for maximum efficiency.
9. **Partitioning:**
   - Partitioning in Impala involves dividing tables into smaller, manageable units based on specific criteria.
   - It improves query performance by reducing the amount of data scanned.
10. **User-Defined Functions (UDFs):**
    - Allows users to create custom functions in Python, C++, or Java for advanced data processing.
    - UDFs enhance Impala's flexibility in handling complex tasks.
11. **Refresh and Invalidate:**
    - **Refresh:** Impala allows you to refresh metadata about tables and schemas, ensuring that the latest changes are reflected in queries.
    - **Invalidate:** You can also invalidate metadata to force Impala to recompute it, ensuring data consistency and accuracy.
12. **Impala Shell:**
      - Impala Shell is a command-line interface for interacting with Impala.
      - It allows users to execute queries, manage database objects, and perform other administrative tasks.
13. **StateStore:**
    - A critical component in Impala that maintains the overall state of the Impala daemons within the cluster.
    - It ensures high availability and consistency across the cluster by syncing metadata and query states, allowing Impala daemons to recover and continue processing in case of failures.
    - The StateStore plays a vital role in distributing configuration changes and updates, ensuring that each daemon has the latest view of the cluster's state.

14. **Topics in Impala:**
    - Topics in Impala refer to the communication channels used by the StateStore to broadcast updates and messages to Impala daemons.
    - These topics ensure that critical information like metadata changes, query states, or daemon health is efficiently propagated across the cluster, maintaining the cluster's overall health and coordination.


### Real-World Use Cases
1. **Interactive SQL Queries:**
   - Impala is ideal for interactive SQL queries on large datasets, providing real-time responses for analytics and reporting.
2. **Data Exploration:**
   - Analysts and data scientists can use Impala to explore data quickly and perform ad-hoc analysis, gaining valuable insights.
3. **ETL Processing:**
   - Impala supports efficient Extract, Transform, Load (ETL) operations, making it suitable for data transformation tasks.
4. **Business Intelligence (BI):**
   - Impala integrates seamlessly with BI tools like Tableau, Qlik, and Power BI, enabling easy data visualization and reporting.
5. **Data Warehousing:**
   - Impala can serve as a high-performance data warehouse, handling complex queries and supporting concurrent users.
6. **IoT Data Processing:**
   - With its ability to handle high-speed data streams, Impala is suitable for processing IoT data for real-time monitoring and analysis.

In summary, Apache Impala is a powerful tool for SQL-based data processing, offering real-time query performance and versatility for a wide range of use cases in the big data ecosystem.

## Chapter 10: Partitioning
**Est. Time:** 0.5 hour

In the realm of databases and data storage, a **partition** is a logical division of a dataset into smaller, more manageable segments. The partitioning strategy is applied to enhance data organization, retrieval efficiency, and overall system performance. Each partition forms a distinct subset of the dataset, and the division is typically based on specific criteria.

### Core Concepts:

#### 1. **Partitioning Criteria:**
   - The criteria for partitioning can vary based on the nature of the data and the requirements of the system. Common partitioning criteria include numerical ranges, alphabetical ranges, or datetime intervals.

#### 2. **Benefits of Partitioning:**
   - Partitioning provides several benefits, including improved query performance, enhanced parallelism, and efficient data maintenance. It enables the system to process and retrieve only the relevant partitions, reducing the computational load.

#### 3. **Partition Key:**
   - The partition key is the attribute or column based on which the dataset is partitioned. It guides the system in determining which partition should store a particular record. The choice of a suitable partition key is crucial for optimizing data access patterns.

#### 4. **Partition Pruning:**
   - Partition pruning is an optimization technique where the query optimizer skips unnecessary partitions during query execution. This process is essential for reducing the amount of data scanned and improving overall query efficiency.

#### 5. **Partitions with Datetime(DT):**
- In the context of datetime-based partitioning, the organization of data is based on datetime values, creating partitions that represent specific time intervals. This approach is particularly useful in scenarios where chronological ordering and time-based queries are essential, such as time-series data.

#### 6. **Real-World Examples:**
In practical scenarios, datetime-based partitioning is instrumental for efficiently managing and querying datasets with temporal dimensions. Here are more detailed examples:

##### 1. **Financial Transactions:**
   - *Use Case:* Consider a financial database storing transaction records. Datetime-based partitioning allows for the organization of data by daily intervals. Each partition represents a day's worth of transactions, making it seamless to analyze daily financial activities. This proves invaluable for tasks like identifying trends, anomalies, or auditing transactions for a specific date range.

##### 2. **IoT Sensor Data:**
   - *Use Case:* In the realm of the Internet of Things (IoT), imagine a database capturing sensor data from a network of devices. Datetime-based partitioning can organize this data by hourly intervals. Each partition encapsulates sensor readings for a specific hour, enabling quick retrieval of data for particular hours or periods. This proves indispensable for monitoring and analyzing device behavior over time.

##### 3. **E-commerce Order Processing:**
   - *Use Case:* For an e-commerce platform, datetime-based partitioning aids in managing order data efficiently. Data could be partitioned by day, allowing for swift queries related to daily sales, peak order times, or order processing efficiency. This enhances operational insights and contributes to optimizing the overall order processing workflow.

##### 4. **Social Media Activity:**
   - *Use Case:* Consider a social media platform dealing with vast amounts of user activity data. Datetime-based partitioning by day or hour facilitates the efficient storage and retrieval of data related to user posts, likes, and comments. This enables the platform to analyze trends, user engagement patterns, and content popularity over specific timeframes.

##### 5. **Event Logging:**
   - *Use Case:* In systems where events are logged, such as server logs or application logs, datetime-based partitioning ensures an organized and easily navigable structure. Each partition represents a specific time period, simplifying the process of identifying and troubleshooting issues within a given timeframe. This is crucial for effective system monitoring and maintenance.

These examples illustrate how datetime-based partitioning enhances the management and analysis of time-sensitive data in various domains. The choice of partitioning strategy, whether daily, hourly, or at a different granularity, depends on the specific requirements of each use case.


## Chapter 11: Kerberos Authentication
**Est. Time: Time: 1.5 hours**

### Core Concepts
#### 1. **Kerberos Protocol:**
   - Kerberos is a network authentication protocol designed to secure communication over an insecure network, providing strong authentication and encryption.

#### 2. **Principal:**
   - A principal is a unique identity, often associated with a user or service, in the Kerberos authentication system. It's represented by a unique name, such as "user@REALM."

#### 3. **KDC (Key Distribution Center):**
   - The Key Distribution Center is the central authentication server in a Kerberos system. It consists of two main components: 
     - Authentication Server (AS): Responsible for initial authentication and issuing tickets.
     - Ticket Granting Server (TGS): Grants service tickets to users for accessing specific services.

#### #### 4. **Tickets:**
   - Kerberos relies on the use of tickets for authentication. There are two primary types of tickets:
     - Ticket Granting Ticket (TGT): Obtained after initial authentication with the AS and used to request service tickets.
     - Service Ticket: Grants access to a specific service, proving the user's identity to that service.

#### 5. **Authentication Process:**
   - Kerberos authentication involves a series of steps, #### including authentication, ticket issuance, and ticket validation. The process ensures that users or services can securely access resources.

#### 6. **Single Sign-On (SSO):**
   - Kerberos enables Single Sign-On, allowing users to access multiple services without re-entering their credentials after the initial authentication.

#### 7. **Realm:**
   - A realm is a Kerberos administrative domain where users, services, and the KDC reside. It's represented as a realm name, such as "EXAMPLE.COM."

#### 8. **Key Encryption Key (KEK):**
   - KEK is used for securing the communication between the client and the KDC. It helps protect the TGT from eavesdropping during transmission.

#### 9. **Time Sensitivity:**
   - Kerberos tickets have a limited validity period to enhance security. The short-lived nature of tickets reduces the risk of compromise if they are intercepted.

### Kerberos Commands

#### `kinit` - Kerberos Ticket Initialization
The `kinit` command is used to obtain a Ticket Granting Ticket (TGT) from the Key Distribution Center (KDC) after a user successfully authenticates using their credentials (typically a username and password). It stores the TGT in a cache, allowing the user to request service tickets without entering their credentials again during their session.

**Usage:**
~~~
kinit username@REALM
~~~


#### `klist` - List Kerberos Tickets
The `klist` command is used to display the contents of the Kerberos ticket cache, showing the currently obtained tickets, including the TGT and any service tickets. This command is helpful for users to check their active tickets and their expiration times.

**Usage:**
~~~
klist
~~~

### Real-World Use Cases
1. **Network Security:**
   - Kerberos is widely used in securing network communications, such as authentication in Active Directory for Windows environments.

2. **Cross-Realm Authentication:**
   - Organizations with multiple realms can use Kerberos to establish trust relationships and allow users to access resources across different administrative domains.

3. **Secure Service Access:**
   - Many network services, including databases and web applications, support Kerberos authentication to ensure secure access and data protection.

4. **Single Sign-On (SSO):**
   - Kerberos-based SSO simplifies user authentication, reduces password fatigue, and enhances user experience by requiring users to log in only once.

5. **Data Protection:**
   - The encryption and time-sensitive nature of Kerberos tickets provide robust security for protecting sensitive data during transmission and access.

In summary, Kerberos authentication is a robust and widely-used protocol for securing network communication, ensuring strong authentication, encryption, and Single Sign-On capabilities in various real-world applications. The `kinit` and `klist` commands are essential tools for managing Kerberos tickets and authenticating users.


## Chapter 12: Oozie Workflow Scheduler
**Est. Time: 1.5 hours**

### Core Concepts
#### 1. **Oozie Overview:**
   - Apache Oozie is a workflow scheduler for Hadoop systems. It is used to manage and coordinate complex workflows of jobs, such as Hadoop MapReduce, Pig, Hive jobs, and more.

#### 2. **Workflow:**
   - An Oozie Workflow is a collection of actions (jobs) arranged in a directed acyclic graph (DAG). Workflows define the sequence of jobs to be executed.

#### 3. **Coordinator:**
   - An Oozie Coordinator job is a higher-level abstraction that allows the management of recurrent Workflow jobs triggered by time (frequency) and data availability.

#### 4. **Bundle:**
   - An Oozie Bundle provides a way to package multiple Coordinator and Workflow jobs and manage their lifecycle together.

#### 5. **Action Node:**
   - In an Oozie workflow, an action node represents a workflow task, like running a MapReduce job, executing a Hive script, or running a Pig script.

#### 6. **Control Node:**
   - Control nodes in Oozie workflows manage the workflow execution path with nodes for defining the start and end of a workflow and decision, fork, and join nodes for controlling the workflow execution flow.

#### 7. **Job Properties:**
   - Oozie jobs are configured with properties files, which are XML files containing job-specific parameters and settings.

#### 8. **Application Master:**
   - Oozie uses YARN’s Application Master to manage the lifecycle of a workflow. Each Oozie workflow job is a YARN application.

#### 9. **SLA Monitoring:**
   - Oozie supports Service Level Agreement (SLA) monitoring for jobs, allowing users to track the progress and performance of their workflows against predefined SLAs.

### Oozie Commands

#### `oozie job` - Oozie Job Operations
The `oozie job` command is used to perform job operations such as running, starting, suspending, resuming, and killing Oozie Workflow, Coordinator, or Bundle jobs.

**Usage:**
~~~
oozie job -oozie <oozie_URL> -config <job.properties> -run
~~~


### Real-World Use Cases
1. **Complex Data Pipelines:**
   - Oozie is used to schedule and manage complex data processing pipelines involving multiple stages and dependencies, ensuring that jobs are executed in the correct order.

2. **Recurring Jobs:**
   - With Oozie's Coordinator jobs, organizations can manage recurring jobs, ensuring that data processing tasks are performed at regular intervals or triggered by data availability.

3. **Resource Management:**
   - Oozie integrates with YARN to ensure efficient resource allocation and management for Hadoop jobs, optimizing cluster resource usage.

4. **SLA Compliance:**
   - Oozie’s SLA feature allows organizations to monitor and enforce service level agreements, ensuring that data processing jobs meet performance expectations.

5. **Scalability and Reliability:**
   - Oozie's robust architecture allows it to manage a large number of jobs reliably, making it suitable for enterprise-scale data processing.

Oozie's integration with the Hadoop stack, its ability to manage complex workflows, and its support for SLA monitoring make it an essential tool for efficient and reliable data processing and job scheduling in Hadoop ecosystems.


