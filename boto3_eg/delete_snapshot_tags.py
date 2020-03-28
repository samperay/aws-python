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

snapshot_deletion = []

snapshot_iterator = ec2.snapshots.filter(Filters=[filters], OwnerIds=[accountId])
for each_snap in snapshot_iterator:
    snapshot_deletion.append(each_snap.id)

print("List of snapshot for deletion: ", snapshot_deletion)

# Delete snapshots for those which have retention period of 45 days

for each_snap in snapshot_deletion:
    snapshot = ec2.Snapshot(each_snap)
    response = snapshot.delete(each_snap, DryRun=False)
print('snapshots deleted ..', snapshot_deletion)