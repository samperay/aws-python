import boto3

ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
  
def getec2_instances():
  for reservation in response["Reservations"]:
      for instance in reservation["Instances"]:
        print("instance_id:", instance["InstanceId"])
        print("instance_type:", instance["InstanceType"])
        print("ami_id", instance['ImageId'])
        print("instance_status", instance['State'])
        print('availability_zone', instance['Placement']['AvailabilityZone'])
        print('public_ip', instance['PublicIpAddress'])
        print('private_ip', instance['PrivateIpAddress'])
        print("instance_keypair:", instance["KeyName"])
        print("dns_public:", instance["PublicDnsName"])
        print("dns_private:", instance["PrivateDnsName"])

if __name__ == "__main__":
    getec2_instances()