# aws_audit_helper
Pequeño script para conseguir información de una cuenta de aws.

# Antes de ejecutar

Este script usa Boto 3. <br />
<br />
Antes de ejecutarlo se deben configurar las credenciales de autenticación para el cliente de aws. <br />
<br />
Suelen estar en ~/.aws/credentials <br /> 
<br />
Para más información: https://boto3.readthedocs.io/en/latest/guide/quickstart.html#configuration <br />
<br />
La ejecución devuelve los datos seguidos por "," para que se pueda importar como hoja de cálculo: <br />
<br />
Ejemplo de salida del comando: python aws_auditor.py<br /> 
<br />
Vpc Tag,Vpc Id,Vpc Cidr Block,Instance Name,Instance Id,Instance Type,Public Ip Address,Private Ip Address,Security Group Name,Subnet Id,Availability Zone<br />
vpcTag1,vpcId1,vpcCidr1<br />
 , , ,nombreInstancia1,idInstancia1,tipoInstancia1,IpPublica,IpPrivada<br />
 , , , , , , , ,nombresecgroup<br />
 , , , , , , , , ,subnetId,AzName-p.e.-eu-west-1b<br />
 ,Security Group Name, IpProtocol, IpRanges, FromPort, ToPort<br />
 ,nombresecgroup,tcp,0.0.0.0/0,22,22<br />
  
