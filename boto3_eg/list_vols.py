#!/usr/bin/python

import boto3
from pprint import pprint

session = boto3.session.Session(profile_name="default",region_name="ap-south-1")
ec2_client = session.client(service_name="ec2",region_name="ap-south-1")

volume_list = []
filters = { 'Name': 'tag:Env', 'Values': ['Prod'] }

# works when the volumes < 50, else you need to use paginators

# for each_volume in ec2_client.describe_volumes(Filters=[filters])["Volumes"]:
#     volume_list.append(each_volume['VolumeId'])
# print(volume_list)

paginator = ec2_client.get_paginator('describe_volumes')
for each_page in paginator.paginate(Filters=[filters]):
    for each_volume in each_page['Volumes']:
        volume_list.append(each_volume['VolumeId'])

print(volume_list)