import boto3

def lambda_handler(event, context):
    eb_client = boto3.client('elasticbeanstalk')
    response = eb_client.restart_app_server(
        EnvironmentName='your-env-name'  # or use EnvironmentId
    )
    print("Restart triggered:", response)
