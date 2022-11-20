# AWS services List

#1. The list should be empty intially.
#2. Populate the list using append or insert. 
#3. Print the list and the length of the list.
#4. Remove two specific services from the list by name or by index.
#5. Print the new list and the new length of the list.

List = []

List.append('SQS')
List.append('OpsWorks')
List.append('IAM')
List.append('RDS')
List.append('VPC')
List.append('Route53')
List.append('CouldTrial')
List.append('Kinesis')

print('AWS Services (8):', List)
List_length = str(len(List))

 
del List [0:2]
print('AWS Services (6):', List)


List_length = str(len(List))
print('Available Services #:', List_length)
