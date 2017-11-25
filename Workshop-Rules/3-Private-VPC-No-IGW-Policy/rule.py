# Import libraries - Lambda will require ipaddress to be uploaded

import json
import logging
import boto3

config_service = boto3.client('config')
ec2_service = boto3.client('##CHANGED##');

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# This is where it's determined whether the resource is compliant or not.
def evaluate_compliance(configuration_item):
    logger.info('CONFIGURATION: ' + json.dumps(configuration_item['configuration']))

    vpc_id = configuration_item['configuration']['##CHANGED##']
    logger.info('VPC_ID: ' + vpc_id)

    tags = configuration_item['configuration']['tags']
    logger.info('TAGS: ' + json.dumps(tags))

    ##checks if the list of tags includes a tag with a key set to private
    tags_private = list(filter((lambda x: x['key'] == '##CHANGED##'), tags))
    logger.info('TAGS_PRIVATE: ' + json.dumps(tags_private))

    if tags_private:
        tag_private = tags_private[0]
        logger.info('TAG_PRIVATE: ' + json.dumps(tag_private))

        if tag_private['value'] == 'true':
            response = ec2_service.##CHANGED: what ec2 boto3 operation needs to be called to gather existing IGWs?##(
                Filters = [
                    {
                        'Name': 'attachment.vpc-id',
                        'Values': [ ##CHANGED: what parameter will filter the service response to just check if IGWs are attached to the VPC being evaluated?## ]
                    }
                ]
            )
            logger.info('response: ' + json.dumps(response))

            ##check if the VPC does have an IGW attached.
            if response['##CHANGED: the presence of what non-empty member in the response will indicate if an IGW is attached?##']:
                return False

    logger.info('RESULT: True')
    return True

# Lambda Function Handler filename.handler -
# Creates AWS Config Rule connection and parses event object to find VPC CIDR's
def lambda_handler(event, context):

    logger.info("Event: " + json.dumps(event))

    event_item = json.loads(event['invokingEvent'])
    config_item = event_item['configurationItem']
    resource_type = config_item['resourceType']

    logger.info(json.dumps(event_item))


# Make sure config_item is not deleted and of the correct type
    if config_item['configurationItemStatus'] == 'ResourceDeleted' or \
       resource_type != 'AWS::EC2::VPC':
        return "NOT_APPLICABLE"

# Setup the Evaluation object and set its variables to the event object
    evaluation = {
        'ComplianceResourceType': config_item['resourceType'],
        'ComplianceResourceId': config_item['resourceId'],
        'ComplianceType': 'NON_COMPLIANT',
        'OrderingTimestamp': config_item['configurationItemCaptureTime']
    }
# Execute evaluation
    result = evaluate_compliance(config_item)

    if result is True:
        evaluation['ComplianceType'] = '##CHANGED##'
    else:
        evaluation['ComplianceType'] = '##CHANGED##'
# Return the evaluation status to the AWS Config Rule service
    if "dryRun" not in event:
        config_service.put_evaluations(
           Evaluations=[##CHANGED##], ResultToken=event['resultToken']
        )
    return evaluation['ComplianceType']
