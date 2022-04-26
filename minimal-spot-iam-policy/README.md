# Minimal IAM policy to grant the Spot role for use with Ocean Spark

This folder contains an IAM policy that contains a minimal set of permissions to support the Ocean Spark platform.

## How to use the policy?

The policy can be used as is, make sure to replace `{{ region }}` and `{{ account_id }}` with the correct value for your environment.

## General information

* All policy blocks are identified by a `Sid` (Statement ID).
* When a `Sid` starts with `Read...`, it grants only read access permissions. All other verbs mean the policy block grants permissions to create, update or delete.
* Most write actions on existing AWS resources (update or delete) are scoped down using tags: tag `spotinst:aws:ec2:group:createdBy: spotinst` must exist on the mutated AWS resource. This ensures that Spot can only mutate AWS resources it created

## Block by block

This section only detail policy blocks granting write permissions.

### CreateEC2Tags

Add tags to EC2 resources created by Spot.

### UpdateEC2InstancesScopedByTag

Spot manages EC2 instances and joins them to your EKS cluster on your behalf. Thus it needs the ability to start and stop instances, and to manage their networking configuration.

Note thatit can only do so for instances tagged with `spotinst:aws:ec2:group:createdBy: spotinst`.

### RunInstances*

Spot manages EC2 instances on your behalf. It can create a new EC2 instance (`ec2:RunInstances` in AWS parlance).

Note that the policy forces Spot to add the `spotinst:aws:ec2:group:createdBy: spotinst` tag to the EC2 instance.

## RequestSpotInstances*

Spot requests spot EC2 instances on your behalf.

Note that the policy forces Spot to add the `spotinst:aws:ec2:group:createdBy: spotinst` tag to the spot instance request.

## CancelSpotInstancesScopedByTag

Spot can cancel spot instance requests it previously initiated (see the condition on the `spotinst:aws:ec2:group:createdBy: spotinst` tag).

Spot can't cancel other spot instance requests.

## RegisterELBs

Ocean can register instances with load balancers on your behalf.

## PassRole

When an EC2 instance is created by Spot on your behalf for your EKS cluster, Spot needs to pass it the IAM role used by worker nodes.

If you would like to scope down this block further and know the exact ARN of the worker nodes IAM role, you can do the following:

```json
{
    "Sid": "PassRole",
    "Action": "iam:PassRole",
    "Effect": "Allow",
    "Resource": [
        "arn:aws:iam::{{ account_id }}:role/{{ role-name }}"
    ]
}
```

## CreateServiceLinkedRole

When creating an EC2 instance, we grant AWS itself to perform some operations on the EC2 instance through a service linked role.
This is a mandatory permission.

## UseKMSKey & WriteCrossAccountKMS

Ocean can be configured to [encrypt EBS volumes with a KMS key you own](https://docs.spot.io/elastigroup/tutorials/elastigroup-tasks/use-cross-account-kms-key-to-encrypt-ebs-volumes).

You can scope down these policy blocks to only use the KMS keys with a certain alias:

```json
{
    "Sid": "UseKMSKey",
    "Effect": "Allow",
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Condition": {
        "ForAnyValue:StringLike": {
        "kms:ResourceAliases": "{{ key_alias }}"
        }
    },
    "Resource": [
        "*"
    ]
}
```
