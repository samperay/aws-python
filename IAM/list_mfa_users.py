#!/usr/bin/python
import boto3
client = boto3.client('iam')
users = client.list_users()
user_list = []
for eachuser in users['Users']:
    result = {}
    Policies = []
    Groups=[]

    result['userName']= eachuser['UserName']
    List_of_Policies =  client.list_user_policies(UserName=eachuser['UserName'])

    result['Policies'] = List_of_Policies['PolicyNames']

    List_of_Groups =  client.list_groups_for_user(UserName=eachuser['UserName'])

    for Group in List_of_Groups['Groups']:
        Groups.append(Group['GroupName'])
    result['Groups'] = Groups

    List_of_MFA_Devices = client.list_mfa_devices(UserName=eachuser['UserName'])

    if not len(List_of_MFA_Devices['MFADevices']):
        result['isMFADeviceConfigured']=False
    else:
        result['isMFADeviceConfigured']=True
    user_list.append(result)

for eachuser in user_list:
    print(eachuser)

