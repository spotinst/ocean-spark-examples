# User Data Startup Script for local ssd support

This folder contains a template of a user data script to enable local SSD support for Spark on the Ocean Spark platform.

## Usage
Add this bash script as userdata script to the Virtual Node Groups (VNGs) used for Spark executors.
In the Spot console, the user data script is configured in Ocean > Clusters > your cluster > Virtual Node Groups.

Make sure to replace the value of the variable `EKS_CLUSTER_NAME` by the name of the cluster.
This name can be found in the AWS console.


## Explanation
This script will create a folder "/data" for all nodes of the VNG.  
If the node is an instance using NVME volume (SSD), it will mount this volume into the above folder "/data".  
Otherwise, the folder will just use current volume.  

Ocean Spark will mount this folder as a volume for the spark application executors.  

Currently, it's enabled only for spark 3 and EKS.
