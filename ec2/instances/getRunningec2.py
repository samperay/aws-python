#!/usr/bin/python

import boto3
from tabulate import tabulate

ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

print('-'*70)
print('| {:{width}} | {:{width}} | {:{width}} |'.format(
    'instance_id',
    'instance_type',
    'key_name',
    width='20'))
print('-'*70)

for eachinstance in instances:
    print('|{:{width}}|{:{width}}|{:{width}}|'.format(eachinstance.id,eachinstance.instance_type,eachinstance.key_name,width='22'))
print('-'*70)
