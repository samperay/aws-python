#!/usr/bin/python

import boto3
from tabulate import tabulate

ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
print("instance-id", " "*7,
      "instance_type", " "*2,
     )
print("-"*30)

for instance in instances:
    print(instance.id,instance.instance_type)

