import boto3

# since no custom session reqired, comenting 
#aws_mgmt_con=boto3.session.Session(profile_name="default")

s3_con=boto3.resource(service_name='s3',region_name="ap-south-1")

for each_bucket in s3_con.buckets.all():
  print(each_bucket.name)