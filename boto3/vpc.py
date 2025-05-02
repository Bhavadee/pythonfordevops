import boto3

ec2 = boto3.client('ec2')

# 1. Create a VPC
vpc_response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc_id = vpc_response['Vpc']['VpcId']
print("Created VPC:", vpc_id)

# 2. Create a Subnet
subnet_response = ec2.create_subnet(
    VpcId=vpc_id,
    CidrBlock='10.0.1.0/24'
)
subnet_id = subnet_response['Subnet']['SubnetId']
print("Created Subnet:", subnet_id)

# 3. Launch an EC2 Instance inside the Subnet
instance_response = ec2.run_instances(
    ImageId='ami-053b0d53c279acc90',  # Replace with valid AMI ID for your region
    InstanceType='t2.micro',
    KeyName='your-keypair-name',      # Replace with your real key pair
    SubnetId=subnet_id,
    MinCount=1,
    MaxCount=1
)

instance_id = instance_response['Instances'][0]['InstanceId']
print("Launched Instance:", instance_id)
