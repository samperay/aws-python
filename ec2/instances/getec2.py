#!/usr/bin/python

import boto3

ec2 = boto3.resource('ec2')
instance_iterator = ec2.instances.all()

for eachinstance in instance_iterator:
    print(eachinstance.id,
    eachinstance.state['Name'],
    eachinstance.key_name,
    eachinstance.public_ip_address,
    eachinstance.private_ip_address,
    eachinstance.instance_type,
    eachinstance.security_groups[0]['GroupName'],
    )

    
