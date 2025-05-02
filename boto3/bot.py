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
