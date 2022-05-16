#!/bin/bash -x

set -euxo pipefail

EKS_CLUSTER_NAME="my_cluster_name"
DATADIR=${DATADIR:-"/data"}
NVMES=""
START=1

echo -e "EC2 NVME Setup Script\n\n"
echo "Starting..."

echo "Creating Data DIR"
mkdir -p ${DATADIR}

echo "Checking instance type: $(ec2-metadata --instance-type)"
if [ `ec2-metadata --instance-type | sed -e "s/^instance-type: //" | awk '{split($0, a, "."); print a[1]}'` == "i3" ]; then
  START=0
fi

echo "Checking for NVME devices"
if ls /dev/nvme? &>/dev/null; then
  END=`ls /dev/nvme? | wc -l`
  for i in `seq ${START} ${END}`; do
    if [ -e /dev/nvme${i}n1 ]; then
        NVMES+=("/dev/nvme${i}n1")
    fi
  done
else
  echo "- No NVMEs"
fi

echo "Content of NVMEs: $NVMES"
echo "Content of NVMEs: ${NVMES[*]}"

if [ ! -z "${NVMES[*]}" ]; then
  echo "Setting up NVME Logical Volume"
  if ! lvs nvmevg/nvmelv &>/dev/null; then
    echo -e "- NVMEs: ${NVMES[@]}\n"
    pvcreate -y ${NVMES[@]}
    vgcreate -y nvmevg ${NVMES[@]}
    lvcreate -y -l 100%FREE nvmevg -n nvmelv
    echo -e "\n- Formatting...\n"
    mkfs.ext4 /dev/nvmevg/nvmelv
    echo -e "- Mounting NVME volume\n"
    mount /dev/nvmevg/nvmelv ${DATADIR}
    sed -i '$ a /dev/nvmevg/nvmelv ${DATADIR} ext4 defaults 0 2' /etc/fstab
  else
    echo "- NVME Logical Volume already exists"
  fi
fi

echo "Setting Data DIR Permissions"
chmod 777 ${DATADIR}

echo "Bootstrapping eks"
/etc/eks/bootstrap.sh "${EKS_CLUSTER_NAME}" ""

