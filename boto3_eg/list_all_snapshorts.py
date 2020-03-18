import boto3
import datetime

aws_mgt_con = boto3.session.Session(profile_name="default",region_name="ap-south-1")
ec2_resource = aws_mgt_con.resource(service_name="ec2",region_name="ap-south-1")

sts_con = aws_mgt_con.client(service_name="sts",region_name="ap-south-1")
response = sts_con.get_caller_identity()
account_id = response.get('Account')

print("Snapshot-ID\t\t | Start_time")
print("-" * 70)
for each_snapshot in ec2_resource.snapshots.filter(OwnerIds=[account_id]):
    print(each_snapshot.id, "|", each_snapshot.start_time)
