# Import libraries - Lambda will require ipaddress to be uploaded

import json
import ipaddress
import logging
import boto3

config_service = boto3.client('##CHANGED##')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# This function uses the ipaddress library to compre the 'onprem' list with AWS Account VPC's
def cidrcheck(net1, net2):
    noOverlaps = True
    prem = map(str, net1)
    for i in prem:
        n1 = ipaddress.IPv4Network(i, strict=False)
        n2 = ipaddress.IPv4Network(net2)
        if ##CHANGED##.overlaps(##CHANGED##):
            logger.info("Found Overlap!")
            ##LINE_REMOVED##

    return noOverlaps

# Lambda Function Handler filename.handler -
# Creates AWS Config Rule connection and parses event object to find VPC CIDR's
def lambda_handler(event, context):
    event_item = json.loads(event['invokingEvent'])
    config_item = event_item['configurationItem']
    resource_type = config_item['resourceType']

    logger.info(json.dumps(event_item))
    logger.info(json.dumps(rules_item))


# Make sure config_item is not deleted and of the correct type
    if config_item['configurationItemStatus'] == 'ResourceDeleted' or \
       resource_type != '##CHANGED##':
        return

# Setup the Evaluation object and set its variables to the event object
    evaluation = {
        'ComplianceResourceType': config_item['resourceType'],
        'ComplianceResourceId': config_item['resourceId'],
        'ComplianceType': 'NON_COMPLIANT',
        'OrderingTimestamp': config_item['configurationItemCaptureTime']
    }
# Execute evaluation
    rules_item = json.loads(event['ruleParameters'])
    onprem = rules_item['##CHANGED##'].split('##CHANGED##')
    cidr = config_item['configuration']['##CHANGED##']

    result = ##LINED_REMOVED##

    if result is True:
        evaluation['ComplianceType'] = 'COMPLIANT'
    else:
        evaluation['ComplianceType'] = 'NON_COMPLIANT'
# Return the evaluation status to the AWS Config Rule service
    if "dryRun" not in event:
        config_service.put_evaluations(
           Evaluations=[evaluation], ResultToken=event['resultToken']
        )

    return evaluation['ComplianceType']
