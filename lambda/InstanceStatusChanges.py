import json
import boto3

# This below code will be executed from the cloudwatch by selecting Event Pattern from Rules. 
# CloudWatch Event Pattern

'''
{
  "source": [
    "aws.ec2"
  ],
  "detail-type": [
    "EC2 Instance State-change Notification"
  ],
  "detail": {
    "state": [
      "terminated"
    ],
    "instance-id": [
      "i-0e80d2995af469239"
    ]
  }
}

'''

def lambda_handler(event, context):
    aws_ec2_console = boto3.resource("ec2", "ap-south-1")
    sns_client = boto3.client("sns","ap-south-1")
    sns_client.publish(TargetArn="TopicARN",Message="Instance Status Changed")