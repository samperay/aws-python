import boto3

session = boto3.session.Session(profile_name="default")
iam = session.resource(service_name="iam")

user_iterator = iam.users.all()
for each_user in user_iterator:
    print(each_user.user_name, each_user.user_id)
    