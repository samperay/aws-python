#!/usr/bin/python

import boto3
import botocore
import re
import os
import sys
import urllib2
import subprocess
from pprint import pprint
from time import sleep
from glob import glob
from os.path import basename, dirname

aws_mgmt_console = boto3.session.Session(region_name="ap-south-1")
ec2_client = aws_mgmt_console.client(service_name="ec2",region_name="ap-south-1")

instanceid = urllib2.urlopen("http://169.254.169.254/latest/meta-data/instance-id").read()

disk_threshold = 80

# Get Current Disk Details 

df = subprocess.Popen(["df", "-hT", '/dev/xvda1'], stdout=subprocess.PIPE)
output = df.communicate()[0]
device, Type, size, used, available, percent, mountpoint = output.split("\n")[1].split()

percent_int = int(percent.split('%')[0])
size_int = int(re.search(r'\d+', size).group())

if percent_int <= disk_threshold:
    print('Disk utilization below threshold, no action required ..')
    pass
    sys.exit(0)
else:
    print('Disk utilizaton above threshold, increasing disk ..')

        # Get instance details
    for each_item in ec2_client.describe_instances(InstanceIds=[instanceid])['Reservations']:
        for each_instance in each_item['Instances']:
            public_ip = each_instance.get('PublicIpAddress')

    # Get Volume ID from Instance
    for each_item in ec2_client.describe_instances(InstanceIds=[instanceid])['Reservations']:
        for each_instance in each_item['Instances']:
            for each_block_device in each_instance['BlockDeviceMappings']:
                devicename = each_block_device['DeviceName']
                volume_id = each_block_device['Ebs']['VolumeId']
                volume_status = each_block_device['Ebs']['Status']

    # Get volume details from volume id
    for each_item in ec2_client.describe_volumes(VolumeIds=[volume_id])['Volumes']:
        current_size = each_item['Size']
        az = each_item['AvailabilityZone']
        current_state = each_item['State']
        volume_type = each_item['VolumeType']
      
    size = current_size + 2

    #Extending volume from AWS
    try:
      volumemodify = ec2_client.modify_volume(DryRun = False, VolumeId = volume_id, Size = size, VolumeType = volume_type)
      print('Extending volume from AWS ......')
      sleep(300)
      print("Volume has been modified from AWS System..")
    except botocore.exceptions.ClientError:
      print('Error: Youve reached the maximum modification rate per volume limit')
      sys.exit(1)
      
    root_partition = devicename+'1'

    df = subprocess.Popen(["df", "-hT", root_partition], stdout=subprocess.PIPE)
    output = df.communicate()[0]
    device, Type, size, used, available, percent, mountpoint = output.split("\n")[1].split()

    if Type == 'xfs':
      os.system('sudo growpart '+ devicename+' 1')
      os.system('sudo xfs_growfs -d '+ mountpoint)
      print('file system has been extended')
    elif Type == 'ext3' or 'ext4':
      print('Need to work on ext file systems')

    sys.exit(0)