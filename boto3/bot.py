import boto3

# Create EC2 resource
ec2 = boto3.resource('ec2')

# Launch a new EC2 instance
instances = ec2.create_instances(
    ImageId='ami-0abcdef1234567890',  # Example AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='your-key-pair'
)

print('Launched instance ID:', instances[0].id)


)
import boto3

# Create EC2 client
ec2_client = boto3.client('ec2')

# Launch instance
response = ec2_client.run_instances(
    ImageId='ami-0abcdef1234567890',  # Replace with your AMI ID
    InstanceType='t2.micro',          # Free tier eligible
    KeyName='my-key-pair',           # Replace with your key pair name
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=['sg-0abc1234de56f7890'],  # Replace with your SG ID
    SubnetId='subnet-0abc1234de56f7890',        # Replace with your subnet ID
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'MyBoto3ClientInstance'}
            ]
        }
    ]
)

# Extract instance ID
instance_id = response['Instances'][0]['InstanceId']
print("Launched EC2 Instance ID:", instance_id)

