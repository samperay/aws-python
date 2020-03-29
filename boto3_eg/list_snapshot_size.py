import boto3
aws_con = boto3.session.Session(profile_name="default")
ec2 = aws_con.resource(service_name="ec2",region_name="ap-south-1")

sts_con = aws_con.client(service_name="sts",region_name="ap-south-1")
response = sts_con.get_caller_identity()
my_own_id = response.get('Account')
f_size={"Name":"volume-size","Values":['8']}
for each_snap in ec2.snapshots.filter(OwnerIds=[my_own_id],Filters=[f_size]):
	print(each_snap.id)