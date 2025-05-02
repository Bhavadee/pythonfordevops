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

import boto3

# Create EC2 resource
ec2 = boto3.resource('ec2')

# Launch EC2 instance
instances = ec2.create_instances(
    ImageId='ami-0abcdef1234567890',  # Replace with your AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',          # Eligible under free tier
    KeyName='my-key-pair',            # Replace with your key pair name
    SecurityGroupIds=['sg-0abc1234de56f7890'],  # Replace with your SG ID
    SubnetId='subnet-0abc1234de56f7890',       # Replace with your Subnet ID
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'MyBoto3Instance'}
            ]
        }
    ]
)

# Output instance ID
print("Launched EC2 Instance ID:", instances[0].id)

