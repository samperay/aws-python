#!/usr/bin/python

# Would be listing all IAM users, EC2 Instances, S3 Buckets from Client Session

import boto3

aws_mgmt_console = boto3.session.Session(profile_name="default",region_name="ap-south-1")

# Open Console Sessions on EC2, IAM and S3.

aws_iam_console = aws_mgmt_console.client(service_name="iam",region_name="ap-south-1")
aws_ec2_console = aws_mgmt_console.client(service_name="ec2",region_name="ap-south-1")
aws_s3_console = aws_mgmt_console.client(service_name="s3",region_name="ap-south-1")

# List IAM Users 
print(" ----------------------- ")

print("Listing all the IAM users")
response = aws_iam_console.list_users()
for each_user in response['Users']:
    print(each_user['UserName'])

print(" ----------------------- ")

# Listing all EC2 Instances

print("Listing all the EC2 instances")
response = aws_ec2_console.describe_instances()
for each_item in response["Reservations"]:
  for each_instance in each_item["Instances"]:
    print(each_instance["InstanceId"])

print(" ----------------------- ")

# List all the S3 Buckets

print("listing all S3 buckets")
response = aws_s3_console.list_buckets()
for each_bucket in response["Buckets"]:
    print(each_bucket["Name"])

print(" ----------------------- ")