#!/usr/bin/python

import boto3
import os
import paramiko
import sys
from pprint import pprint
from time import sleep

aws_mgmt_console = boto3.session.Session(profile_name="default",region_name="ap-south-1")

# Open Console Sessions on EC2
ec2_client = aws_mgmt_console.client(service_name="ec2",region_name="ap-south-1")

# Get Required Info from Instance
for each_item in ec2_client.describe_instances()['Reservations']:
  for each_instance in each_item['Instances']:
    instance_state = each_instance['State']['Name']
    instance_id = each_instance['InstanceId']
    if instance_state == 'running' and each_instance.get('PublicIpAddress') is not None:
      public_ip = each_instance.get('PublicIpAddress')
      print("Public_Ip:",public_ip)
      print('Instance_ID:', instance_id)

# Get list of Volume ID and its associated Instance ID
response = ec2_client.describe_volumes()['Volumes']

for each_item in response:

  # Get volume details attached to instance
  current_size = each_item['Size']
  az = each_item['AvailabilityZone']
  current_state = each_item['State']
  volume_type = each_item['VolumeType']

  print("Current Size: ",current_size)
  print("az:",az)
  print("current_state: ",current_state)
  print("volume_type: ",volume_type)
  
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


if current_size == 12:
  print("Disk already same size as target size.. exiting")
  sys.exit(0)
else:
  print("Attempting to increasing volume size from AWS ...")
  volumemodify = ec2_client.modify_volume(
    DryRun = False,
    VolumeId = volume_id,
    Size = 12,
    VolumeType = volume_type
  )
  print('Extending volume from AWS ......')
  sleep(300)
  print("Volume has been modified from AWS System..")

# Logging into the instance to get disk partitions using paramiko

key = paramiko.RSAKey.from_private_key_file("/home/samperay/MyLinuxEC2KeyPair.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=public_ip, username="ec2-user", pkey=key)

localfile = "/home/samperay/Documents/gitprojects/aws-python/getDiskInfo.py"
remotefile = "/tmp/getDiskInfo.py"

# Copy file locally to remote host
sftp = client.open_sftp()
sftp.put(localfile, remotefile)
sftp.close()

#Execute a command(cmd) after connecting/ssh to an instance
stdin,stdout,stderr = client.exec_command("chmod +x /tmp/getDiskInfo.py; python /tmp/getDiskInfo.py")
print(stdout.read())

# close the client connection once the job is done
client.close()

# ====== Windows testing =======

# key = paramiko.RSAKey.from_private_key_file("E:\\aws-keys\ebsdemo.pem")
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname=public_ip, username="ec2-user", pkey=key)

# localfile = "E:\\projects\\aws-python\getDiskInfo.py"
# remotefile = "/tmp/getDiskInfo.py"

# # Copy file locally to remote host
# sftp = client.open_sftp()
# sftp.put(localfile, remotefile)
# sftp.close()

# #Execute a command(cmd) after connecting/ssh to an instance
# stdin,stdout,stderr = client.exec_command("chmod +x /tmp/getDiskInfo.py; python /tmp/getDiskInfo.py")
# print(stdout.read())

# # close the client connection once the job is done
# client.close()