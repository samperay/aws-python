import boto3
aws_mgt_con = boto3.session.Session(profile_name="default",region_name="ap-south-1")
ec2_resource = aws_mgt_con.resource(service_name="ec2",region_name="ap-south-1")

filer_unsed_ebs = { "Name":"status", "Values": ["available"] }

for each_volume in ec2_resource.volumes.all():
    if not each_volume.tags:
        print(each_volume.id,each_volume.state,each_volume.tags)
        print("Deleting un-used and un-tagged volumes..")
        each_volume.delete()

print("Deleted un-used/untagged instance")