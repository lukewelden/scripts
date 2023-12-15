"""A script that saves a list of all autoscaling groups in a given region to a csv file.

This script lists all of the autosclaing groups in a given region and saves their name, desired capacity, 
min, max, and current capacity to a csv file. 

To run the script, first configure your AWS credentials, I use environment variables, and then run the script 
using your chosen python interpreter. For example, `python3 listASG.py`.

Feel free to modify this script to suit your needs. For example, you could list more information about the ASGs. 
"""
import boto3


def list_asgs():
    # Create an autoscaling client
    asg_client = boto3.client('autoscaling')

    # Get all of the autoscaling groups in the region
    asg_response = asg_client.describe_auto_scaling_groups()

    # Save the name, desired capacity, min, max, and current capacity of each autoscaling group to a csv file. If the ASG has
    # a tag called 'Name' then that will be used as the name of the ASG, otherwise the ASG's name will be used.
    with open('asg_list.csv', 'w') as file:
        file.write('Name, TagName, Desired Capacity,Min Size,Max Size,Current Size\n')
        for asg in asg_response['AutoScalingGroups']:
            file.write(asg['AutoScalingGroupName'] + ',' + asg['Tags'][1]['Value'] + ',' + str(asg['DesiredCapacity']) + ',' + str(asg['MinSize']) + ',' + str(asg['MaxSize']) + '\n')

if __name__ == '__main__':
    list_asgs()