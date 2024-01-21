# Day 03 - Introduction to Data concept & Hadoop Ecosystem :elephant:

## Goals:
- Gain a foundational understanding of the Hadoop ecosystem.
- Explore key components and their roles in big data processing.
- Make connections between the Hadoop ecosystem and real-world use cases.
- Develop a high-level understanding of the Hadoop ecosystem and its role in big data processing.
- Familirize yourself with the Hadoop ecosystem and its role in big data processing.
- Start to work with time estimation and planning.

:warning: **Note:**
- This is a self-study day, it is important to be able to work independently and manage your time.
- A lot of newbies have a problem with self-study and time management, so breath and take your time to plan your day carefully.
- Be aware of the importance of time management. Plan your time 
and tasks, and try to stick to your plan. If you are not able to finish the tasks in the time you have planned, you should discuss it with your mentor, maybe you learn more then you should.

**Total Time:** 8.5 hours

## Chapter 1: Introduction to Big Data and Hadoop
**Est. Time:** 1 hour
- [Apache Hadoop](https://hadoop.apache.org/)

Apache Hadoop is a powerful framework for distributed storage and processing of large datasets, commonly associated with big data analytics and processing tasks. In this chapter, we introduce some of the fundamental concepts of Big Data and Hadoop.

### 1. **What are the different vendor-specific distributions of Hadoop?**
   - Hadoop has gained popularity in various industries, leading to the development of different vendor-specific distributions. Some notable distributions include:
     - **Cloudera**: Cloudera offers Cloudera Distribution for Hadoop (CDH), a comprehensive distribution that includes various Hadoop ecosystem components along with management and monitoring tools.
     - **Amazon EMR**: Amazon Elastic MapReduce (EMR) is a cloud-native Hadoop distribution provided by Amazon Web Services (AWS), offering easy scalability and integration with other AWS services.
     - **Microsoft Azure**: Microsoft provides Azure HDInsight, a Hadoop distribution on the Azure cloud platform, with support for various big data and machine learning frameworks.

### 2. **What are the different Hadoop configuration files, explain each?**
   - Hadoop configuration files play a crucial role in defining the behavior and settings of various Hadoop components. Here's an overview of some essential Hadoop configuration files:

     - `core-site.xml`: This file contains core configuration settings, such as the file system, I/O settings, and network addresses. It is used to specify properties like the Hadoop cluster's default file system and various I/O-related configurations.

     - `hdfs-site.xml`: For the Hadoop Distributed File System (HDFS), this file defines configuration parameters like replication factors, block sizes, and data node settings. It is vital for tuning HDFS to suit specific requirements.

     - `mapred-site.xml`: When working with the MapReduce framework, this file is used to configure settings related to job tracking, task scheduling, and resource management. It defines properties like the job tracker address and task tracker settings.

     - `yarn-site.xml`: In the context of Yet Another Resource Negotiator (YARN), this file specifies configurations for resource management, node manager settings, and resource allocation policies. It plays a significant role in optimizing resource utilization in Hadoop clusters.

     - `hadoop-env.sh`: This script allows you to set environment variables and customize options for Hadoop processes. It is particularly useful for configuring memory settings and Java-related parameters for Hadoop components.

Hadoop configuration files provide the flexibility to tailor the behavior of Hadoop components to meet specific performance, scalability, and resource management requirements. Proper configuration is essential for optimizing Hadoop clusters and achieving desired outcomes in big data processing tasks.

Remember that Hadoop's flexibility extends beyond these core configuration files, as it allows you to create custom configurations and adapt the framework to the unique needs of your big data projects.

## Chapter 2: Hadoop Distributed File System (HDFS) :star:
**Est. Time:** 4 hours
- [Hadoop Distributed File System (HDFS)](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html)

Hadoop Distributed File System (HDFS) is a foundational component of the Hadoop ecosystem, designed to store and manage large volumes of data across a distributed cluster.

### Core Concepts

#### 1. NameNode and DataNode
- **NameNode:**
  - Centralized metadata repository managing file system namespace and hierarchy.
  - Keeps track of file metadata and the location of data blocks.
- **DataNode:**
  - Stores and manages the actual data blocks.
  - Communicates with the NameNode to report block information and perform block-related operations.

#### 2. Block Storage
- HDFS divides files into fixed-size blocks (default 128 MB or 256 MB).
- Each block is stored redundantly across multiple DataNodes for fault tolerance.
- Redundant storage ensures data availability even in the case of node failures.

#### 3. Replication
- HDFS replicates data blocks to multiple DataNodes to ensure data durability and fault tolerance.
- The default replication factor is three, but it can be configured based on specific requirements.

#### 4. Rack Awareness
- HDFS is rack-aware, meaning it considers the physical network topology.
- Replication is done across racks to enhance fault tolerance and reduce network congestion.

#### 5. High Availability (HA)
- HDFS supports High Availability configurations for the NameNode.
- In HA mode, two NameNodes (Active and Standby) work in coordination to ensure continuous operation in the event of a NameNode failure.

#### 6. Data Integrity
- HDFS ensures data integrity through checksums.
- Checksums are calculated for data blocks, and any corruption is detected during read operations.

#### 7. HDFS Federation
- HDFS Federation allows multiple independent HDFS namespaces to share a common cluster.
- Enhances scalability by distributing namespace and storage across multiple NameNodes.

#### 8. Snapshots
- HDFS supports snapshots for creating point-in-time copies of a directory or the entire file system.
- Useful for data recovery, testing, and backup purposes.

#### 9. JournalNode
  - In HDFS High Availability (HA) configurations, JournalNodes are integral for synchronizing the file system metadata between Active and Standby NameNodes. They maintain a shared edit log, ensuring that any changes made by the Active NameNode are quickly replicated to the Standby NameNode.
  - The Active NameNode records each metadata change to multiple JournalNodes (forming a quorum) for fault tolerance. This approach ensures that the Standby NameNode can seamlessly transition to an Active role if needed, providing robustness against failures.
  - The deployment of JournalNodes is crucial and should be strategically planned to ensure network reliability and reduce the risk of simultaneous failures, thus maintaining the high availability and integrity of the HDFS namespace.

  #### 10. NameService
  - The NameService in HDFS is a logical grouping of NameNodes in a federated setup. It facilitates the use of multiple NameNodes in the cluster, each managing a distinct namespace volume.
  - NameServices allow for horizontal scalability of the namespace, as additional NameNodes can be added to handle more files and directories.
  - Each NameService is configured with one or more NameNodes for redundancy and high availability, ensuring the file system's resilience and reliability.

#### 11. Block Report
  - Block Reports are periodic messages sent by DataNodes to the NameNode. These reports contain a list of all blocks on a DataNode, allowing the NameNode to keep its block mapping up-to-date.
  - Block Reports are crucial for maintaining the integrity of the file system, enabling the NameNode to identify missing blocks and initiate necessary replication to maintain the desired level of redundancy.

#### 12. RPC Requests
  - Remote Procedure Call (RPC) requests in HDFS are used for communication between the NameNode, DataNodes, and clients. They facilitate operations like opening files, creating directories, renaming files, and replicating or deleting blocks.
  - RPC ensures a standardized method of communication across the distributed components of HDFS, providing a seamless operational experience and ensuring the efficiency and reliability of the file system's operations.
  

#### 10. HDFS Deep Dive
- [HDFS Deep Dive](./deep_dive/HDFS.md)
### Real-World Examples:

#### 1. **Big Data Analytics in Financial Services:**
   - *Use Case:* A financial institution leverages HDFS for storing and managing vast datasets used in big data analytics. The distributed nature of HDFS allows the institution to scale its data storage and processing capabilities to gain insights into market trends, customer behavior, and risk assessment.

#### 2. **Log Storage and Analysis in Cybersecurity:**
   - *Use Case:* A cybersecurity firm utilizes HDFS to store and analyze large volumes of log data generated by various security tools. HDFS's fault-tolerant design ensures that log data is resilient to node failures, and the distributed nature facilitates parallel processing for real-time threat detection and response.

#### 3. **Genomic Data Storage in Healthcare Research:**
   - *Use Case:* In healthcare research, HDFS serves as the storage foundation for large-scale genomic datasets. The ability of HDFS to manage and replicate data across nodes ensures the integrity and availability of genomic data for analysis and research in fields like precision medicine.

#### 4. **Media and Entertainment Content Distribution:**
   - *Use Case:* A media company employs HDFS for the storage and distribution of multimedia content. The distributed nature of HDFS allows efficient storage and retrieval of large video and audio files, supporting content delivery networks and optimizing the streaming experience for end-users.

#### 5. **IoT Data Management for Smart Cities:**
   - *Use Case:* In smart city initiatives, HDFS is used for storing and processing data generated by IoT devices, sensors, and connected infrastructure. The scalability and fault tolerance of HDFS accommodate the diverse and massive data streams, enabling data-driven decision-making for urban planning and management.

These real-world examples illustrate the versatility and applicability of Hadoop Distributed File System (HDFS) across diverse industries and use cases.


## Chapter 3: MapReduce Programming Model
**Est. Time:** 0.5 hours
- [MapReduce Tutorial](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)

MapReduce is a Java-based, distributed execution framework within the Apache Hadoop Ecosystem.  It takes away the complexity of distributed programming by exposing two processing steps that developers implement: **1) Map** and **2) Reduce**. In the Mapping step, data is split between parallel processing tasks. Transformation logic can be applied to each chunk of data. Once completed, the Reduce phase takes over to handle aggregating data from the Map set.. In general, MapReduce uses Hadoop Distributed File System (HDFS) for both input and output. However, some technologies built on top of it, such as Sqoop, allow access to relational systems.

### Core Concepts

A MapReduce system is usually composed of three steps (even though it's generalized as the combination of Map and Reduce operations/functions). The MapReduce operations are:

#### 1. **Map:** 
- The input data is first split into smaller blocks. The Hadoop framework then decides how many mappers to use, based on the size of the data to be processed and the memory block available on each mapper server. Each block is then assigned to a mapper for processing. Each ‘worker’ node applies the map function to the local data, and writes the output to temporary storage. The primary (master) node ensures that only a single copy of the redundant input data is processed.

#### 2. **Shuffle:**
- combine and partition: worker nodes redistribute data based on the output keys (produced by the map function), such that all data belonging to one key is located on the same worker node. As an optional process the combiner (a reducer) can run individually on each mapper server to reduce the data on each mapper even further making reducing the data footprint and shuffling and sorting easier. Partition (not optional) is the process that decides how the data has to be presented to the reducer and also assigns it to a particular reducer.

#### 3. **Reduce:**
- A reducer cannot start while a mapper is still in progress. Worker nodes process each group of <key,value> pairs output data, in parallel to produce <key,value> pairs as output. All the map output values that have the same key are assigned to a single reducer, which then aggregates the values for that key. Unlike the map function which is mandatory to filter and sort the initial data, the reduce function is optional.

## Chapter 4: Hadoop YARN
**Est. Time:** 1.5 hours
- [Apache Hadoop YARN](https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html)

YARN (Yet Another Resource Negotiator) is a fundamental component in the Hadoop ecosystem, serving as a resource management layer to efficiently share resources among multiple applications in a Hadoop cluster.

### Core Concepts

#### 1. Resource Manager (RM)
- Central component managing and allocating resources across the Hadoop cluster.
- Keeps track of available resources and schedules applications based on their resource requirements.

#### 2. Node Manager (NM)
- Runs on each machine in the cluster, managing resources (CPU, memory, etc.) on that specific node.
- Communicates with the Resource Manager to provide information about available resources and request resources for running applications.

#### 3. Application Master (AM)
- Created for each application submitted to YARN.
- Negotiates with the Resource Manager to obtain resources and coordinates the execution of tasks on Node Managers.
- Acts as a liaison between the application and the resource manager.

#### 4. Container
- Fundamental unit of resource allocation in YARN.
- Represents the allocated resources (CPU, memory) on a specific node for a particular application.
- Applications may consist of one or more containers.

#### 5. Application Lifecycle
- When a client submits a job to YARN, an Application Master is created for that job.
- The Application Master negotiates with the Resource Manager to obtain resources and launches containers on the Node Managers.
- Containers execute the tasks of the application.

#### 6. Schedulers
- YARN supports different schedulers, such as CapacityScheduler and FairScheduler.
- CapacityScheduler allows sharing resources among multiple queues with allocated capacities.
- FairScheduler assigns resources in a balanced manner, ensuring that all applications get a fair share.

#### 7. Resource Allocation
- YARN supports dynamic resource allocation, allowing applications to request additional resources or release unused resources during runtime.
- This flexibility enables optimal resource utilization based on the varying needs of applications.

#### 8. Fault Tolerance
- YARN provides fault tolerance by monitoring the health of Node Managers and restarting failed containers on healthy nodes.
- Ensures the reliability of applications by handling node failures and container restarts.

#### 9. Security
- YARN includes security features such as authentication and authorization to control access to cluster resources.
- Helps maintain the integrity and security of the Hadoop cluster.

#### 10. Preemption
- Preemption is a feature in YARN that allows the Resource Manager to interrupt and reclaim resources from running applications.
- Useful in multi-tenant environments where higher-priority applications may need resources currently allocated to lower-priority applications.

#### 11. Queue
- In the context of Apache Hadoop YARN, a "queue" refers to a logical subdivision or container for managing and allocating resources within a cluster.
- YARN queues play a crucial role in the resource management layer, allowing organizations to control how resources are shared among different applications or user groups.
- Queues facilitate multi-tenancy by providing distinct containers for different teams or applications, preventing resource contention and ensuring efficient workload isolation.


### Real-World Examples:
In real-world scenarios, Apache Hadoop YARN serves as a crucial resource management layer, enabling dynamic resource allocation and workload diversity. Here are detailed examples showcasing the practical applications of Apache Hadoop YARN:

#### 1. **Large-Scale Data Processing in E-commerce:**
   - *Use Case:* A multinational e-commerce company relies on YARN to process and analyze vast amounts of customer and transaction data in a cloud environment. YARN dynamically allocates resources for diverse workloads, from routine batch processing to complex analytics, ensuring optimal resource utilization. This enables the company to handle the global scale of its operations efficiently.

#### 2. **Enterprise Data Lakes for Financial Analysis:**
   - *Use Case:* A financial institution employs YARN to manage its enterprise data lake for in-depth financial analysis. YARN's resource allocation capabilities support concurrent execution of data processing tasks, allowing financial analysts to run complex algorithms and queries without contention. This ensures timely insights into market trends, risk assessment, and investment strategies.

#### 3. **Genomic Data Processing in Healthcare:**
   - *Use Case:* A healthcare research institution utilizes YARN for processing large-scale genomic data. YARN's ability to dynamically allocate resources based on the computational needs of genomic analysis tasks ensures efficient utilization of cluster resources. This accelerates genomic research, enabling scientists to analyze and interpret vast datasets for precision medicine initiatives.

#### 4. **Log Analysis for Cybersecurity:**
   - *Use Case:* A cybersecurity firm employs YARN for log analysis to detect and respond to security threats. YARN's resource management ensures that log processing tasks receive the necessary resources for real-time analysis. This allows the firm to identify and mitigate security incidents promptly, enhancing the overall cybersecurity posture.

#### 5. **Media and Entertainment Content Processing:**
   - *Use Case:* A media and entertainment company uses YARN to process and analyze content data, including video transcoding and metadata extraction. YARN's flexibility in handling diverse workloads allows the company to efficiently allocate resources for tasks like video processing, image recognition, and content recommendation, optimizing the content delivery pipeline.

These examples demonstrate how Apache Hadoop YARN plays a pivotal role in diverse industries, providing scalable and efficient resource management for a wide range of data processing tasks.


## Chapter 5: Apache Hive
**Est. Time:** 1.5 hours
- [Apache Hive Documentation](https://hive.apache.org/documentation.html)

### Core Concepts

#### 1. **Hive Metastore:**
- Centralized metadata repository that stores schema and partition information for Hive tables.
- Allows Hive to operate independently of the underlying Hadoop storage system.

#### 2. **Tables:**
- Data in Hive is organized into tables, similar to relational databases.
- Tables can be external or managed, defining how data is stored and managed.

#### 3. **HiveQL:**
- SQL-like query language for Hive, making it accessible to users familiar with SQL.
- Supports queries, data definition language (DDL) statements, and data manipulation language (DML) statements.

#### 4. **Partitions:**
- Enables the division of large datasets into smaller, more manageable parts.
- Improves query performance by allowing pruning of unnecessary data during queries.

#### 5. **SerDe (Serializer/Deserializer):**
- SerDe is a crucial component that defines how Hive serializes and deserializes data during input and output.
- It allows Hive to work with various data formats, including JSON, XML, and custom formats.

#### 6. **UDFs (User-Defined Functions):**
- Hive allows the creation of custom functions to extend its functionality.
- UDFs can be implemented in languages like Java, Python, or other supported languages.

#### 7. **Hive Execution Engine:**
- Responsible for executing HiveQL queries and generating query plans.
- Supports different execution engines, including MapReduce and Tez, offering flexibility in processing large-scale data.

#### 8. **Bucketing:**
- Technique to improve query performance by organizing data into buckets based on a hash function.
- Enables more efficient joins and queries on large datasets.

#### 9. **Dynamic Partition Pruning:**
- Optimizes query performance by dynamically excluding unnecessary partitions during query execution.
- Reduces the amount of data that needs to be processed.

#### 10. **Hive Views:**
- Similar to views in traditional databases, providing a virtual representation of data stored in one or more tables.
- Simplifies complex queries and enhances data abstraction.

### **Real-World Use Cases:**

- **Data Warehousing:** Hive is widely used for large-scale data warehousing tasks, enabling users to perform analytics on vast datasets.
- **ETL (Extract, Transform, Load):** Used for preprocessing and transforming raw data into a structured format.
- **Ad Hoc Querying:** Provides a familiar SQL-like interface for users to run ad hoc queries on Hadoop data.
- **Hive on Text:** Hive can be used to process and analyze text data, including log files and social media data.
To process and analyze text data in Hive, follow these steps:
   - Define Tables: Create Hive tables that match your text data structure.
   - Choose SerDe: Specify a Serializer/Deserializer (SerDe) for parsing text.
   - Load Data: Use LOAD DATA to import text data into Hive tables.
   - Query: Run HiveQL queries for text analysis, utilizing built-in functions.
   - Store Results: Save results in Hive or export as required.

## Chapter 6: Apache ZooKeeper
**Est. Time:** 2 hours
- [Apache ZooKeeper](https://zookeeper.apache.org/)

Apache ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. It's an essential component in distributed systems, often used in Hadoop ecosystems to coordinate and manage servers effectively.

### Core Concepts

#### 1. Coordination and Configuration Management
- **ZooKeeper:**
  - Provides a reliable, fast, and simple coordination service for distributed applications.
  - Manages common data in a centralized manner, which allows distributed nodes to coordinate with each other.

#### 2. Znodes - Data Nodes
- ZooKeeper's data model consists of znodes, which are similar to files and directories. Each znode can store data and have children.
- Znodes maintain a stat structure that includes version numbers for data changes, ACL changes, and timestamps to facilitate cache validations.

#### 3. Watches
- Clients can set watches on znodes. A watch will be triggered and a notification sent to the client if the znode changes.
- Watches are a simple mechanism that allows clients to get notified of changes without polling.

#### 4. Consistency
- Ensures a highly reliable data registry for distributed systems.
- Data is replicated over a set of hosts and all interactions happen in the primary server to maintain a consistent data model.

#### 5. Sessions
- Clients connect to ZooKeeper servers using sessions. Sessions are maintained by heartbeats (pings); if a heartbeat is not received within the specified time, the session is considered dead.

#### 6. Atomicity
- Operations in ZooKeeper are atomic. Either an operation is successfully executed, or no change is made to the state of the system.

#### 7. Ephemeral Nodes
- ZooKeeper supports the creation of ephemeral nodes which exist as long as the session that created them is active.
- Useful for locks and leader election in distributed systems.

#### 8. Sequence Nodes
- ZooKeeper can create sequence znodes which are automatically assigned a unique monotonic increasing number.
- Useful for implementing primitives like distributed counters.

### Real-World Examples:

#### 1. **Service Discovery in Microservices Architectures:**
   - *Use Case:* In a microservices architecture, ZooKeeper can be used for service discovery. Each service registers its address in ZooKeeper, and clients use ZooKeeper to look up the addresses dynamically, allowing for loose coupling and easy scaling.

#### 2. **Configuration Management:**
   - *Use Case:* Centralized configuration management allows distributed systems to change their behavior dynamically. Systems read configuration data from ZooKeeper and get notified instantly about the changes, ensuring consistency across the cluster.

#### 3. **Leader Election:**
   - *Use Case:* In distributed systems, leader election is essential for deciding the primary server. ZooKeeper's ephemeral and sequence nodes can be used to implement a robust leader election algorithm.

#### 4. **Distributed Locks:**
   - *Use Case:* ZooKeeper can be used to implement distributed locks that are essential for ensuring that only one node is executing a critical section of code at any point in time.

#### 5. **Cluster Management:**
   - *Use Case:* ZooKeeper is often used in distributed systems for cluster management. It can monitor the nodes joining and leaving the cluster dynamically and trigger necessary actions based on the cluster state changes.

ZooKeeper's ability to coordinate between nodes in a distributed system makes it an indispensable tool in complex, large-scale applications. It provides a simple interface to a powerful coordination mechanism, simplifying the development of distributed applications.
