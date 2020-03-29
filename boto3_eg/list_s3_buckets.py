import boto3

session = boto3.session.Session(profile_name="default",region_name="aps-south-1")
s3 = session.client(service_name="s3",region_name="ap-south-1")

for each_bucket in s3.list_buckets()['Buckets']:
    print(each_bucket["Name"])
