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

# Create snapshot for the volume

snapshotids=[]

for each_volume_id in volume_list:
    print("taking snapshot", each_volume_id)
    response=ec2_client.create_snapshot(
        Description='snapshot rundeck production',
        VolumeId=each_volume_id,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {
                        'Key': 'DeleteOn',
                        'Value': '45'
                    },
                    {
                        'Key': 'Env',
                        'Value': 'Prodvols'
                    },
                    {
                        'Key': 'Name',
                        'Value': 'rundeckmaster'
                    },
                ] 
            },
        ],
    )
    snapshotids.append(response.get('SnapshotId'))
print('snapshots:',snapshotids)

waiter= ec2_client.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=snapshotids)
print('Snapsot completed for volumes ..',volume_list )