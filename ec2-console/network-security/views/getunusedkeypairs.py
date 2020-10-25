#!/usr/bin/python

import boto3

ec2 = boto3.resource('ec2')

# Fetch all keypairs from AWS account
key_pairs = ec2.key_pairs.all()

# Create list of key pairs from AWS account
all_keypairs = set([keypair.name for keypair in key_pairs])
#print(all_keypairs)

# Fetch all EC2 instances in AWS account
instances = ec2.instances.all()

# Get all the AWS keypairs associated with the instances

instance_associated_keypairs = []

for eachinstance in instances:
    instance_associated_keypairs.append(eachinstance.key_name)

unused_keypairs = all_keypairs - set(instance_associated_keypairs) 

print("Un-Used Keypairs in AWS:")
print("-"*20)
for eachkey in unused_keypairs:
    print(eachkey)


