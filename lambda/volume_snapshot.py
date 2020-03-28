import json
import boto3

def lambda_handler(event, context):

    ec2_client = boto3.client(service_name="ec2",region_name="ap-south-1")
    volume_list = []
    filters = { 'Name': 'tag:Env', 'Values': ['Prod'] }

    paginator = ec2_client.get_paginator('describe_volumes')
    for each_page in paginator.paginate(Filters=[filters]):
        for each_volume in each_page['Volumes']:
            volume_list.append(each_volume['VolumeId'])
    
    # Create snapshot for the volume
    
    snapshotids=[]
    
    for each_volume_id in volume_list:
        print("crating snapshot ..", each_volume_id)
        response=ec2_client.create_snapshot(
            Description='snapshot from lambda,cloudwatch for rundeck production',
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
    return 'success'