import boto3

aws_management_console = boto3.session.Session(profile_name="default")

# connector to all aws resources
iam_console = aws_management_console.resource('iam')

for user in iam_console.users.all():
    print(user.name)

# connector to all aws clients 
iam_console_client = aws_management_console.client('iam')

for user in iam_console_client.list_users()['Users']:
     print(user['UserName'])
