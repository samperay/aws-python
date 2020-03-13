import boto3
import time

aws_con = boto3.session.Session(profile_name="default", region_name="ap-south-1")
aws_ec2_resource = aws_con.resource(service_name="ec2", region_name="ap-south-1")
aws_ec2_client = aws_con.client(service_name="ec2", region_name="ap-south-1")

rundeck_env_instances = []

filter1 = { 'Name':'tag:Project', 
            'Values': ['rundeck']
          }

for rundeck_env in aws_ec2_resource.instances.filter(Filters=[filter1]):
    rundeck_env_instances.append(rundeck_env.id)

print(rundeck_env_instances)

print("list of ec2 instances stopping..", rundeck_env_instances)
print('stopping rundeck environment instances  ..')
aws_ec2_resource.instances.stop()
waiter = aws_ec2_client.get_waiter('instance_stopped')
waiter.wait(InstanceIds=rundeck_env_instances)
print('all your rundeck environment instances stopped ..')