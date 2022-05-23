# User Data Startup Script for local ssd support

This folder contains a template of a user data script to enable local SSD support for Spark on the Ocean Spark platform.

## Usage
Add this bash script as userdata script to the Virtual Node Groups (VNGs) used for Spark executors.
In the Spot console, the user data script is configured in Ocean > Clusters > your cluster > Virtual Node Groups.

Make sure to replace the value of the variable `EKS_CLUSTER_NAME` by the name of the cluster.
This name can be found in the AWS console.


## Explanation
This script will create a folder `/data` on the filesystem of all nodes in the VNG.  
If the EC2 instance underlying the node uses NVMe volumes (like `m5d`, `r5d`, or `i3` families), the script will mount these volumes into the above folder `/data`.  
Otherwise, the `/data` folder will just be transparently created on the instance boot disk.  

Ocean Spark will mount this folder as a volume in all Spark executor pods.  

Currently, local SSD support is enabled for Spark 3 and AWS only.
