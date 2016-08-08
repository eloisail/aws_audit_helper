# -*- encoding: utf-8 -*-
import time
import boto3
print (r"-------¡Hola!")
time.sleep(1)
print (r"Este script usa Boto 3.")
print (r"Antes de ejecutarlo se deben configurar las credenciales de autenticación para el cliente de aws.")
print (r"Suelen estar en ~/.aws/credentials")
print (r"Para más información: https://boto3.readthedocs.io/en/latest/guide/quickstart.html#configuration")
print (r"-------")
time.sleep(3)

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

vpcs_dict = vpcs_json['Vpcs']
vpcs_size = len(vpcs_dict)

instances_dict = instances_json['Reservations']
instances_size = len(instances_dict)

subnets_dict = subnets_json['Subnets']
subnets_size = len(subnets_dict)

for vpc in vpcs_dict:
    print("--------Vpc-----------")
    if 'Tags' in vpc:
        print(vpc['Tags'][0]['Value'] +" "+vpc['VpcId']+ " "+vpc['CidrBlock'])
    else:
        print(vpc['VpcId']+" "+vpc['CidrBlock'])

    print("----------------------")

    for instance in instances_dict:
#        print instance['Instances']
#        print instance['Instances'][0]['InstanceId']
        for inst in instance['Instances']:
            if (inst['VpcId'] == vpc['VpcId']):
                print("    "+ "---------Instancias----------")
                print("    " + inst['InstanceId'])
                print("    " + inst['InstanceType'])
                print("    " + inst['PublicIpAddress'])



        

