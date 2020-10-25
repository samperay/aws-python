#!/usr/bin/python

import boto3

ec2 = boto3.resource('ec2')
security_group_iterator = ec2.security_groups.all()

# fetch all sg in AWS account 
sgs = ec2.security_groups.all() 

# Create list of sg groups
all_sgs = set([sg.group_name for sg in sgs])

# Fetch all EC2 instances in AWS account 
instances = ec2.instances.all()

# Get all the sg attached to insatances 
instance_attached_sg = set([sg['GroupName'] for ins in instances for sg in ins.security_groups])

# Remove duplicate sg to get un-used sg in AWS account 
unused_sgs = all_sgs - instance_attached_sg


print("Total Un-used SG group in AWS account:")
for each_sg in unused_sgs:
    print(each_sg)



