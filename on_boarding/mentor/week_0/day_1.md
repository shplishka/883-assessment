# Q&A: Introduction to Hadoop Ecosystem

### Chapter 1: Introduction to Big Data and Hadoop

1. **Q:** What is Apache Hadoop?  
   **A:** Apache Hadoop is an open-source software framework used for distributed storage and processing of large datasets using the MapReduce programming model.

2. **Q:** Can you name a few vendor-specific distributions of Hadoop?  
   **A:** Yes, some vendor-specific distributions of Hadoop include Cloudera, Amazon EMR, and Microsoft Azure.

3. **Q:** What are the three modes in which Hadoop can run?  
   **A:** Hadoop can run in three modes: Standalone mode, Pseudo-distributed mode, and Fully-distributed mode.

4. **Q:** What is the primary role of the `hadoop-env.sh` configuration file?  
   **A:** The `hadoop-env.sh` file is used to configure environment variables for Hadoop, such as setting the Java home directory.

5. **Q:** What purpose does the `core-site.xml` file serve?  
   **A:** The `core-site.xml` file configures Hadoop core settings, including I/O settings and the default file system URL.

### Chapter 2: Hadoop Distributed File System (HDFS)

6. **Q:** What is HDFS?  
   **A:** HDFS, or Hadoop Distributed File System, is a distributed file system designed to run on commodity hardware. It is highly fault-tolerant and is designed to be deployed on low-cost hardware.

7. **Q:** What is the role of the NameNode in HDFS?  
   **A:** The NameNode is the master server that manages the file system namespace and regulates access to files by clients. It maintains the file system tree and the metadata for all the files and directories.

8. **Q:** What is a DataNode in HDFS?  
   **A:** A DataNode stores data in the HDFS. It serves read and write requests from the file system's clients and performs block creation, deletion, and replication upon instruction from the NameNode.

9. **Q:** How does HDFS achieve fault tolerance?  
   **A:** HDFS achieves fault tolerance by replicating data blocks across multiple DataNodes in the cluster, ensuring no single point of failure.

10. **Q:** Can you explain rack awareness in HDFS?  
    **A:** Rack awareness is the concept used in HDFS to improve network traffic while reading/writing data and also to improve the fault tolerance. The NameNode chooses DataNodes that are on different racks for data replication to ensure that even if an entire rack fails, the data is safe.

### Chapter 3: MapReduce Programming Model

11. **Q:** What is MapReduce?  
    **A:** MapReduce is a programming model and an associated implementation for processing and generating large datasets with a parallel, distributed algorithm on a cluster.

12. **Q:** What is the role of a Mapper in MapReduce?  
    **A:** A Mapper processes input data and creates key-value pairs for the Reducer to process.

13. **Q:** What is the role of a Reducer in MapReduce?  
    **A:** A Reducer takes the output from a Mapper as input and combines those data tuples into a smaller set of tuples.

14. **Q:** What is meant by "Shuffling" in MapReduce?  
    **A:** Shuffling in MapReduce is the process of transferring data from Mappers to Reducers, typically involving sorting and partitioning.

15. **Q:** Can a MapReduce job have zero Reducers?  
    **A:** Yes, a MapReduce job can have zero Reducers if no reduction is needed, and it is known as a "map-only" job.

### Chapter 4: Hadoop YARN

16. **Q:** What is YARN?  
    **A:** YARN (Yet Another Resource Negotiator) is a resource management layer of Hadoop that allows multiple data processing engines to handle data stored in a single platform, thus enabling resource sharing and cluster utilization.

17. **Q:** What are the main components of YARN?  
    **A:** The main components of YARN include the Resource Manager, Node Manager, Application Master, and Container.

18. **Q:** What is the Resource Manager in YARN?  
    **A:** The Resource Manager is the master service of YARN that manages the allocation of compute resources in the cluster.

19. **Q:** What is the role of the Node Manager in YARN?  
    **A:** The Node Manager is a per-node service that manages the lifecycle of containers on that node and reports the node's resource usage to the Resource Manager.

20. **Q:** How does YARN provide fault tolerance?  
    **A:** YARN provides fault tolerance by restarting failed tasks on different nodes and by storing application progress in a persistent store for recovery.

### Chapter 5: Apache Hive

21. **Q:** What is Apache Hive?  
    **A:** Apache Hive is a data warehouse software project built on top of Apache Hadoop for providing data query and analysis.

22. **Q:** What is the Hive Metastore?  
    **A:** The Hive Metastore is a central repository in Hive that stores metadata for Hive tables, such as the schema and location of data files.

23. **Q:** What is HiveQL?  
    **A:** HiveQL is a SQL-like query language used in Apache Hive for querying data stored in a Hadoop cluster.

24. **Q:** What are partitions in Hive?  
    **A:** Partitions in Hive are a way of dividing a table into different parts based on the values of a particular column to optimize query performance.

25. **Q:** Can you define SerDe in the context of Hive?  
    **A:** SerDe stands for Serializer/Deserializer. It's a component of Hive used to read and write data from tables and convert it into a format suitable for processing.

### Chapter 6: Apache HBase

26. **Q:** What is Apache HBase?  
    **A:** Apache HBase is an open-source, distributed, versioned, non-relational database modeled after Google's Bigtable and is written in Java.

27. **Q:** What is a Row Key in HBase?  
    **A:** A Row Key is a unique identifier for each row in an HBase table, determining the physical storage location of the data.

28. **Q:** What is a Column Family in HBase?  
    **A:** A Column Family is a collection of columns in an HBase table that are stored together on the disk.

29. **Q:** How does HBase ensure data availability and fault tolerance?  
    **A:** HBase ensures data availability and fault tolerance through data replication across different nodes in the cluster and automatic failover capabilities.

30. **Q:** What is the role of ZooKeeper in an HBase environment?  
    **A:** ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and group services. In HBase, it's used for master election, server lease management, bootstrapping, and coordination between servers.

### Chapter 7: Apache Spark

31. **Q:** What is Apache Spark?  
    **A:** Apache Spark is an open-source, distributed computing

 system that provides an interface for programming entire clusters with implicit data parallelism and fault tolerance.

32. **Q:** What are RDDs in Spark?  
    **A:** RDDs (Resilient Distributed Datasets) are a fundamental data structure of Spark that represent an immutable collection of objects that can be split across a computing cluster.

33. **Q:** What are Transformations and Actions in Spark?  
    **A:** Transformations are operations on RDDs that return a new RDD, like `map` and `filter`. Actions are operations that return a value after running a computation on an RDD, like `count` and `collect`.

34. **Q:** What is Lazy Evaluation in Spark?  
    **A:** Lazy Evaluation means that the execution will not start until an action is triggered. In Spark, RDDs are lazily evaluated, improving the system's efficiency and optimizing the overall data processing pipeline.

35. **Q:** Can you explain the role of Executors in Spark?  
    **A:** Executors are worker nodes' processes in charge of running individual tasks in a given Spark job. They are responsible for executing code sent by the driver and reporting the state of the computation back to the driver.

### Chapter 8: Apache Kafka

36. **Q:** What is Apache Kafka?  
    **A:** Apache Kafka is a distributed streaming platform that is used for building real-time data pipelines and streaming applications.

37. **Q:** What are Topics in Kafka?  
    **A:** Topics are categories or feed names to which records are published. Topics in Kafka are multi-subscriber; they can be consumed by multiple consumers.

38. **Q:** What are Partitions in Kafka?  
    **A:** Partitions are ordered, immutable sequences of records that are continually appended. A topic may have multiple partitions to allow the data to be scaled.

39. **Q:** What is the role of a Broker in Kafka?  
    **A:** A Broker is a Kafka server that stores data and serves client requests. Each broker can handle a certain load of data, and together they form the entire Kafka cluster.

40. **Q:** What is the difference between a Kafka Producer and a Consumer?  
    **A:** A Kafka Producer is responsible for publishing records to Kafka topics. A Kafka Consumer subscribes to topics and processes the feed of published records.


### Chapter 9: Impala

41. **Q:** What is Apache Impala?

    **A:** Apache Impala is an open-source, massively parallel processing (MPP) SQL query engine for processing and analyzing data stored in Hadoop Distributed File System (HDFS) and HBase. It provides real-time, interactive SQL queries for data stored in these distributed storage systems, making it easier to perform analytics on large datasets.

42. **Q:** What is an Impala Daemon?
    
    **A:** An Impala Daemon, often referred to as an Impalad, is a process that runs on each node of an Impala cluster. These daemons are responsible for executing queries and processing data in parallel. Impala Daemons communicate with each other and with other components like the Impala Catalog Service to coordinate query execution and retrieve metadata.

43. **Q:** What is the role of a Catalog Service in Impala?

    **A:** The Catalog Service in Impala serves as a centralized metadata repository for the cluster. It stores metadata information about tables, partitions, schemas, and data locations, making it accessible to all Impala Daemons and Query Coordinators. This service helps in query planning and execution by providing essential metadata information.

44. **Q:** What is the role of a Query Coordinator in Impala?

    **A:** A Query Coordinator in Impala is responsible for managing the overall execution of a query. When a SQL query is submitted to Impala, the Query Coordinator receives the query, develops a query plan, coordinates its execution across multiple Impala Daemons, and ensures the results are returned to the user or application. It plays a crucial role in optimizing query execution.

45. **Q:** What is the difference between Refresh and Invalidate in Impala?

    **A:** In Impala, "Refresh" and "Invalidate" are commands used to update the metadata about tables and partitions in the Catalog Service:

    - **Refresh:** When you issue a "Refresh" command, Impala reloads the metadata information for a specific table or partition from the underlying storage system (e.g., HDFS or HBase). This command is used when you want Impala to recognize new data or changes to existing data in a table.

    - **Invalidate:** The "Invalidate" command, on the other hand, is used to invalidate the cached metadata for a specific table or for the entire catalog. It marks the metadata as stale, and the next time a query is executed on that table or catalog, Impala will refresh the metadata to ensure it is up-to-date. This is useful when external changes are made to the underlying data, and Impala needs to be aware of these changes.

    These commands help in maintaining metadata consistency and ensuring that Impala's query execution plans are accurate based on the latest information about the data.

### Chapter 10: Partitioning

46. **Q:** What is Partitioning in databases and data storage?  
    **A:** Partitioning is the process of dividing a database or its elements into discrete parts to improve manageability, performance, and availability.

47. **Q:** What are some common partitioning criteria?  
    **A:** Common partitioning criteria include numerical ranges, alphabetical ranges, hash values, and datetime intervals.

48. **Q:** What is a Partition Key?  
    **A:** A Partition Key is a column or a set of columns that determines how the data is partitioned and stored in the database.

49. **Q:** Can you explain Partition Pruning?  
    **A:** Partition Pruning is an optimization technique used in query processing where the query optimizer eliminates unnecessary partitions and only scans the relevant ones.

50. **Q:** How is datetime-based partitioning used in real-world scenarios?  
    **A:** Datetime-based partitioning is used to organize and manage time-series data efficiently, like financial transactions or event logs, allowing for faster access and analysis of data based on time intervals.

