#import all modules and libraries
# https://www.youtube.com/watch?v=dMLvgvJ23LI&list=PLjl2dJMjkDjlcI3SQErSq4UMX3okzafvO&index=12
"""
import boto3
from pprint import pprint

aws_management_console = boto3.session.Session(profile_name="default")  #Management console information

# connector to all aws resources
iam_console = aws_management_console.resource(service_name ='iam')    #IAM console information

for user in iam_console.users.all():
    print(user.name)

# connector to all aws clients 
iam_console_client = aws_management_console.client('iam')

list_users = iam_console_client.list_users()

#pprint(list_users)

for user in list_users['Users']:
     print(user['UserName'])


# Open Ec2 Console information
ec2_console = aws_management_console.resource(service_name ='ec2')
try:
    result = ec2_console.describe_instances()['Reservations']
    for every_instance in result:
        for value in every_instance['Instances']:
            print(value['InstanceId'])
except:
    print("No instances to be found")
"""

import boto3

aws_management_console = boto3.session.Session(profile_name ="default")
ec2_console = aws_management_console.client('ec2')

response = ec2_console.run_instances(
	ImageId = 'ami-0230bd60aa48260c6',
	InstanceType = 't2.micro',
	MaxCount = 1,
	MinCount = 1

)

# response = ec2_console.start_instances(   
#      InstanceIds = ['i-Enter your instance Id here']
# )




