#!/usr/bin/python

import boto3
import os
import paramiko
from pprint import pprint


aws_mgmt_console = boto3.session.Session(profile_name="default",region_name="ap-south-1")

# Open Console Sessions on EC2
ec2_client = aws_mgmt_console.client(service_name="ec2",region_name="ap-south-1")

# Get Required Info from Instance
for each_item in ec2_client.describe_instances()['Reservations']
  for each_instance in each_item['Instances']:
    public_ip = each_instance['PublicIpAddress']
    public_dns_name = each_instance['PublicDnsName']


# Get list of Volume ID and its associated Instance ID
response = ec2_client.describe_volumes()['Volumes']

for each_item in response:

  # Get volume details attached to instance
  current_size = each_item['Size']
  az = each_item['AvailabilityZone']
  current_state = each_item['State']
  volume_type = each_item['VolumeType']
  
  # Get instance details from volume
  for each_instance in each_item['Attachments']:
    instance_id = each_instance['InstanceId']
    volume_state = each_instance['State']
    device = each_instance['Device']
    volume_id = each_instance['VolumeId']
    
print("Instance ID: ", instance_id)
print("Volume ID:", volume_id)
print("Device Name:", device)
print("Current Disk Size:", current_size)

print("Increasing volume size from AWS ...")
volumemodify = ec2_client.modify_volume(
  DryRun = False,
  VolumeId = volume_id,
  Size = 10,
  VolumeType = volume_type
)

print("Volume has been modified from AWS System..")
for each_item in volumemodify['VolumeModification']:
  print("Actual size",each_item['OriginalSize'], "Extending size", each_item['TargetSize'])

# Logging into the instance to get disk partitions using paramiko

key = paramiko.RSAKey.from_private_key_file("/home/samperay/MyLinuxEC2KeyPair.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="public_ip", username="ec2-user", pkey=key)

# Execute a command(cmd) after connecting/ssh to an instance
stdin, stdout, stderr = client.exec_command("/tmp/resize_xvda1.sh")
print(stdout.read())

# close the client connection once the job is done
client.close()