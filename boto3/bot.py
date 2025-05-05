import boto3

# Create EC2 client
ec2_client = boto3.client('ec2', region_name='us-east-1')  # specify your region

# Launch a new EC2 instance
response = ec2_client.run_instances(
    ImageId='ami-0c2b8ca1dad447f8a',  # Replace with a real AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='nv123',  # Replace with your actual key pair name
)

# Get the instance ID
instance_id = response['Instances'][0]['InstanceId']
print('Launched instance ID:', instance_id)
