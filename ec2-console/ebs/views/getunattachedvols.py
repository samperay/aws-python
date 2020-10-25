#!/usr/bin/python 

import boto3

ec2 = boto3.resource('ec2')
volume_iterator = ec2.volumes.all()


available_volumes = []

for eachvolume in volume_iterator:
    if eachvolume.state == "available":
        available_volumes.append(eachvolume.id)


print("| Available Volumes |") 
print('-'*19)

for vol in available_volumes:
    print(vol)
