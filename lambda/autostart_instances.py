import json
import boto3

def lambda_handler(event, context):
    ec2_console = boto3.resource(service_name="ec2", region_name="ap-south-1")
    
    rundeck_env_instances = []

    filter1 = { 'Name':'tag:<Name>', 
                'Values': ['<Value>']
              }
    
    for rundeck_env in ec2_console.instances.filter(Filters=[filter1]):
        rundeck_env_instances.append(rundeck_env.id)
    ec2_console.instances.start()

    return '0'