#!/usr/bin/python
import boto3 

ec2=boto3.resource('ec2')
snapshot_iterator = ec2.snapshots.all()

for eachsnap in snapshot_iterator:
    print(eachsnap.id)
