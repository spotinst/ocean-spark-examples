# User Data Startup Script for local ssd support

This folder contains a template of a user data script to support local ssd on Ocean spark platform.

## Usage
On Spot Ocean Cluster  
Add the bash script on the VNGs used for spark executors.  
Replace the value of the variable EKS_CLUSTER_NAME by the name of the cluster.


## Explanation
This script will create a folder "/data" for all nodes of the VNG.  
If the node is an instance using NVME volume (SSD), it will mount this volume into the above folder "/data".  
Otherwise, the folder will just use current volume.  

Ocean Spark will mount this folder as a volume for the spark application executors.  

Currently, it's enabled only for spark 3 and EKS.
