import boto3

# Incase of any custom session

aws_mag_con = boto3.session.Session(profile_name="default")
iam_con=aws_mag_con.resource(service_name='iam',region_name="ap-south-1")

for each_user in iam_con.users.all():
  print(each_user.name)