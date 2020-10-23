#!/usr/bin/python

import boto3
from tabulate import tabulate

ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
print("instance-id", " "*10,
      "key_name", " "*10,
      "public_ip", " "*10,
      "private_ip", " "*10,
      "instance_type", " "*10,
     )

for instance in instances:
    print(instance.id,instance.key_name,instance.public_ip_address,instance.private_ip_address,instance.instance_type)

