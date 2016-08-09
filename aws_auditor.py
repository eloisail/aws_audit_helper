# -*- encoding: utf-8 -*-
import time
import boto3

# Una forma de hacerlo sin el cliente
# Directamente cogiendo los recursos
#

# ec2 = boto3.resource('ec2')

# for ec2_vpc in ec2.vpcs.all():
#     print (ec2_vpc.id)
#     for ec2_instance in ec2.instances.all():
#         if ec2_vpc.id == ec2_instance.vpc.id:
#             print ("    " + ec2_instance.id)

#
# Otra forma de hacerlo
# Usando el cliente
#


client = boto3.client('ec2')

vpcs_json = client.describe_vpcs()
subnets_json = client.describe_subnets()
instances_json = client.describe_instances()
sec_groups_json = client.describe_security_groups()

vpcs_dict = vpcs_json['Vpcs']
vpcs_size = len(vpcs_dict)

instances_dict = instances_json['Reservations']
instances_size = len(instances_dict)

subnets_dict = subnets_json['Subnets']
subnets_size = len(subnets_dict)

sec_groups_dict = sec_groups_json['SecurityGroups']
sec_groups_size = len(sec_groups_dict)

print("Vpc Tag,Vpc Id,Vpc Cidr Block,Instance Name,Instance Id,Instance Type,Public Ip Address,Private Ip Address,Security Group Name,Subnet Id,Availability Zone")


for vpc in vpcs_dict:
    if 'Tags' in vpc:
        print(vpc['Tags'][0]['Value'] +","+vpc['VpcId']+ ","+vpc['CidrBlock'])
    else:
        print(" ,"+vpc['VpcId']+","+vpc['CidrBlock'])

    for instance in instances_dict:
        for inst in instance['Instances']:
            if (inst['VpcId'] == vpc['VpcId']):
                tags=inst['Tags']
                for tag in tags:
                    if (tag['Key']=='Name'):
                        print(" , , ,"+tag['Value']+","+inst['InstanceId']+","+inst['InstanceType']+","+ inst['PublicIpAddress']+","+inst['PrivateIpAddress'])
                        secGroupId = inst['SecurityGroups']
                        for group in secGroupId:
                            print(" , , , , , , , ,"+group['GroupName'])
                            networkIf = inst['NetworkInterfaces']
                            for network in networkIf:
                                for subnet in subnets_dict:
                                    if network['SubnetId'] == subnet['SubnetId']:
                                        print(" , , , , , , , , ,"+network['SubnetId']+","+subnet['AvailabilityZone'])
    print(" ,Security Group Name, IpProtocol, IpRanges, FromPort, ToPort")
    for sec_group in sec_groups_dict:
        if (vpc['VpcId'] == sec_group['VpcId']):
            for i in sec_group['IpPermissions']:
                for element in i['IpRanges']:
                    print (" ,"+sec_group['GroupName']+","+i.get('IpProtocol')+","+element['CidrIp']+","+str(i.get('FromPort'))+","+str(i.get('ToPort'))) 
