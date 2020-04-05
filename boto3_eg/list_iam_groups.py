import boto3

session = boto3.session.Session(profile_name="default")
iam = session.resource(service_name="iam")


group_iterator = iam.groups.all()
for each_group in group_iterator:
    print(each_group.group_name, each_group.group_id)


