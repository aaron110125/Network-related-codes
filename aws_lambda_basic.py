#import all modules and libraries

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

pprint(list_users)

for user in list_users['Users']:
     print(user['UserName'])
