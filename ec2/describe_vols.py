#!/usr/bin/python 

# Describe volumes on EC2 instances 

import boto3

client = boto3.client('ec2')

response = client.describe_volumes()
print(response)


