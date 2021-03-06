#!/usr/bin/python

import boto3

ec2 = boto3.resource('ec2')
instance_iterator = ec2.instances.all()

print('-'*90)
print('| {:{width}} | {:{width}} | {:{width}} | {:{width}} | {:{width}} | {:{width}} | {:{width}} |'.format(
    'instance_id',
    'instance_state',
    'key_name',
    'public_ip',
    'private_ip',
    'instance_type',
    'security_group',
    width='9'))
print('-'*90)

for eachinstance in instance_iterator:
    print("|",eachinstance.id,
    "|",eachinstance.state['Name'],
    "|",eachinstance.key_name,"\t",
    "|",eachinstance.public_ip_address,
    "|",eachinstance.private_ip_address,
    "|",eachinstance.instance_type,
    "|",eachinstance.security_groups[0]['GroupName'],"|",
    )

    
