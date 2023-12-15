""" A script that removes a scheduled action from all autoscaling groups in a given region.

If you find that you need to manually remove a scheduled action from all of your autoscaling groups, 
this script will do it for you. Simply configure your AWS credentials, I use environment variables, and then
run the script with your python interpreter. For example, `python3 removeAutoscalingGroupScheduledActions.py`. 

The script will find all of the autoscaling groups in the region, and then check to see if they have a scheduled 
action configured. If they do, it will remove the scheduled action you have specified.

Feel free to modify this script to suit your needs. For example, you could add a check list the named scheduled 
actions that the ASGs have and then remove the ones you want to remove.

"""
import boto3

# Enter the name of the scheduled action you want to remove
scheduled_action_name = 'EveningScaleDown'

def remove_scheduled_action():
    autoscaling = boto3.client('autoscaling')
    response = autoscaling.describe_auto_scaling_groups()
    asg_list = response['AutoScalingGroups']

    for asg in asg_list:
        asg_name = asg['AutoScalingGroupName']
        res = autoscaling.describe_scheduled_actions(
            AutoScalingGroupName=asg_name
        )
        r = res['ScheduledUpdateGroupActions']

        if r:
            print(f'Found scheduled action: {scheduled_action_name} for {asg_name}')
            try:
                autoscaling.delete_scheduled_action(
                    AutoScalingGroupName=asg_name,
                    ScheduledActionName=scheduled_action_name
                )
                print('Deleted ScaleUp for ' + asg_name)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    remove_scheduled_action()