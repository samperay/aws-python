import boto3
from pprint import pprint

# Getting OwnerID for AWS account

aws_mgt_con = boto3.session.Session(profile_name="default",region_name="ap-south-1")
sts_con = aws_mgt_con.client(service_name="sts",region_name="ap-south-1")
response = sts_con.get_caller_identity()
accountId = response.get('Account')

# EC2 
ec2 = boto3.resource('ec2',region_name="ap-south-1")
filters = { 'Name': 'tag:DeleteOn', 'Values': ['45'] }

# Get list of snapshot from your AWS account based on the filters defined. 

snapshot_iterator = ec2.snapshots.filter(Filters=[filters], OwnerIds=[accountId])
print("List of all snapshots ownerby you: ")
for each_snap in snapshot_iterator:
    print(each_snap.id)
