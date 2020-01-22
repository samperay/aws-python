import boto3
import csv

ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
 
def getec2_instances():
  with open('./ec2_inventory.csv', 'w') as csvfile:
    # Write Header for csv file 
    fields = [ 'instance_id', 
               'instance_type', 
               'ami_id',
               'instance_status',
               'availability_zone',
               'public_ip',
               'private_ip',
               'instance_keypair',
               'dns_public',
               'dns_private',
             ]

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

    # get each instance deatils from response. 
    # response return type is dict, so get each key from dict and place in a list

    for reservation in response["Reservations"]:
      for instance in reservation["Instances"]:

        instance_details = [  instance["InstanceId"], 
                              instance["InstanceType"], 
                              instance["ImageId"],
                              instance["State"]["Name"],
                              instance["Placement"]["AvailabilityZone"],
                              instance["PublicIpAddress"],
                              instance["PrivateIpAddress"],
                              instance["KeyName"],
                              instance["PublicDnsName"],
                              instance["PrivateDnsName"],
                          ]
        csvwriter.writerow(instance_details)

if __name__ == "__main__":
    getec2_instances()