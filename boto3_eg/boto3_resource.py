#!/usr/bin/python

import boto3

aws_mgmt_console = boto3.session.Session(profile_name="default",region_name="ap-south-1")

# Open Console Sessions on EC2, IAM and S3.

aws_iam_console = aws_mgmt_console.resource(service_name="iam",region_name="ap-south-1")
aws_ec2_console = aws_mgmt_console.resource(service_name="ec2",region_name="ap-south-1")
aws_s3_console = aws_mgmt_console.resource(service_name="s3",region_name="ap-south-1")

# List IAM Users 
print(" ----------------------- ")
print("List of IAM Users")

for each_item in aws_iam_console.users.all():
  print(each_item.name)

# List S3 Buckets 
print(" ----------------------- ")
print("List of all S3 Buckets")

for each_bucket in aws_s3_console.buckets.limit(2):
  print(each_bucket.name)


# List EC2 Instances 
print(" ----------------------- ")
print("Listing EC2 Instacnes ")

for each_instance in aws_ec2_console.instances.all():
  print(each_instance.id)

print(" ----------------------- ")