#!/usr/bin/python

import boto3
client = boto3.client('ec2')
addresses_dict = client.describe_addresses()

for eip in addresses_dict['Addresses']:
    if "InstanceId" not in eip:
        if "NetworkInterfaceId" not in eip:
            print("Unused EIP:",eip['PublicIp'])
