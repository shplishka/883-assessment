# HDFS Deep Dive

Read [HDFS Architecture](https://hadoop.apache.org/docs/r3.3.0/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html) and answer the following questions:

**Est. Time:** 4 hour

### 1. **What are the differences between regular FileSystem and HDFS?**

***Regular FileSystem:*** In regular FileSystem, data is maintained in a single system. If the machine crashes, data recovery is challenging due to low fault tolerance. Seek time is more and hence it takes more time to process the data.

***HDFS:*** Data is distributed and maintained on multiple systems. If a DataNode crashes, data can still be recovered from other nodes in the cluster. Time taken to read data is comparatively more, as there is local data read to the disc and coordination of data from multiple systems.

### 2. **Why is HDFS fault-tolerant?**

HDFS is fault-tolerant because it replicates data on different DataNodes. By default, a block of data is replicated on three DataNodes. The data blocks are stored in different DataNodes. If one node crashes, the data can still be retrieved from other DataNodes. 

![Alt text](/on_boarding/assets/fault_tolerant.png)

### 3. **Explain the architecture of HDFS?**

the HDFS architecture consists of the following components:
![Alt text](/on_boarding/assets/hdfs_architecture.png)

For an HDFS service, we have a NameNode that has the masterprocess running on one of the machines and DataNodes, whichare the slave nodes.
***NameNode***
NameNode is the master service that hosts metadata in diskand RAM. It holds information about the various DataNodes,their location, the size of each block, etc. 

***DataNode***
DataNodes hold the actual data blocks and send block reportsto the NameNode every 10 seconds. The DataNode stores andretrieves the blocks when the NameNode asks. It reads andwrites the client’s request and performs block creation,deletion, and replication based on instructions from theNameNode.
- Data that is written to HDFS is split into blocks,depending on its size. The blocks are randomly distributedacross the nodes. With the auto-replication feature, theseblocks are auto-replicated across multiple machines with thecondition that no two identical blocks can sit on the samemachine. 
- As soon as the cluster comes up, the DataNodes startsending their heartbeats to the NameNodes every threeseconds. The NameNode stores this information; in otherwords, it starts building metadata in RAM, which containsinformation about the DataNodes available in the beginning.This metadata is maintained in RAM, as well as in the disk.

### **4. What are the two types of metadata that a NameNode server  holds?**
    
The two types of metadata that a NameNode server holds are:

***Metadata in Disk*** - This contains the edit log and the *FSImage*
***Metadata in RAM*** - This contains the information about DataNodes

### **5. What is the difference between a federation and high availability?**

	
| HDFS Federation | HDFS High Availability |  
| :---------------- | :------: | 
|     There is no limitation to the number of NameNodes and the NameNodes are not related to each other |   There are two NameNodes that are related to each other. Both active and standby NameNodes work all the time   |
|     All the NameNodes share a pool of metadata in which each NameNode will have its dedicated pool |  One at a time, active NameNodes will be up and running, while standby NameNodes will be idle and updating its metadata once in a while   | 
|     Provides fault tolerance, i.e., if one NameNode goes down, it will not affect the data of the other NameNode |  It requires two separate machines. First, the active NameNode will be configured, while the secondary NameNode will be configured on the other system   

### **6. If you have an input file of 350 MB, how many input splits would HDFS create and what would be the size of each input split?**

By default, each block in HDFS is divided into 128 MB. The size of all the blocks, except the last block, will be 128 MB. For an input file of 350 MB, there are three input splits in total. The size of each split is 128 MB, 128MB, and 94 MB.

![Alt text](/on_boarding/assets/split_data.png)

### **7. What is the default replication factor in HDFS?**
the default replication factor in HDFS is 3.

### **8.How does rack awareness work in HDFS?**

HDFS Rack Awareness refers to the knowledge of different DataNodes and how it is distributed across the racks of a Hadoop Cluster.

![Alt text](/on_boarding/assets/block_distributing.png)

By default, each block of data is replicated three times on various DataNodes present on different racks. Two identical blocks cannot be placed on the same DataNode. When a cluster is “rack-aware,” all the replicas of a block cannot be placed on the same rack. If a DataNode crashes, you can retrieve the data block from different DataNodes.   

### **9.How can you restart NameNode and all the daemons in Hadoop?**

The following commands will help you restart NameNode and all the daemons:

You can stop the NameNode with `./sbin /Hadoop-daemon.sh` stop NameNode command and then start the NameNode using `./sbin/Hadoop-daemon.sh` start NameNode command.

You can stop all the daemons with `./sbin /stop-all.sh` command and then start the daemons using the `./sbin/start-all.sh` command.

### **10.Which command will help you find the status of blocks and FileSystem health?**

To check the status of the blocks, use the command:

`hdfs fsck <path> -files -blocks`

To check the health status of FileSystem, use the command:

`hdfs fsck / -files –blocks –locations > dfs-fsck.log`

### **11.What would happen if you store too many small files in a cluster on HDFS?**

Storing several small files on HDFS generates a lot of metadata files. To store these metadata in the RAM is a challenge as each file, block, or directory takes 150 bytes for metadata. Thus, the cumulative size of all the metadata will be too large.

### **12. How do you copy data from the local system onto HDFS?**
The following command will copy data from the local file system onto HDFS:

`hadoop fs –copyFromLocal [source] [destination]`

Example: `hadoop fs –copyFromLocal /tmp/data.csv /user/test/data.csv`

In the above syntax, the source is the local path and destination is the HDFS path. Copy from the local system using a -f option (flag option), which allows you to write the same file or a new file to HDFS. 

### **13. Who takes care of replication consistency in a Hadoop cluster and what do under/over replicated blocks mean?**

In a cluster, it is always the NameNode that takes care of the replication consistency. The fsck command provides information regarding the over and under-replicated block. 

***Under-replicated blocks:***

These are the blocks that do not meet their target replication for the files they belong to. HDFS will automatically create new replicas of under-replicated blocks until they meet the target replication.

Consider a cluster with three nodes and replication set to three. At any point, if one of the NameNodes crashes, the blocks would be under-replicated. It means that there was a replication factor set, but there are not enough replicas as per the replication factor. If the NameNode does not get information about the replicas, it will wait for a limited amount of time and then start the re-replication of missing blocks from the available nodes. 

***Over-replicated blocks:***

These are the blocks that exceed their target replication for the files they belong to. Usually, over-replication is not a problem, and HDFS will automatically delete excess replicas.

Consider a case of three nodes running with the replication of three, and one of the nodes goes down due to a network failure. Within a few minutes, the NameNode re-replicates the data, and then the failed node is back with its set of blocks. This is an over-replication situation, and the NameNode will delete a set of blocks from one of the nodes. 