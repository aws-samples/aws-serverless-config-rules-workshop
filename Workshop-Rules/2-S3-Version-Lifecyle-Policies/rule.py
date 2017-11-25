import boto3
import json
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)
APPLICABLE_RESOURCES = ["AWS::S3::Bucket"]
config = boto3.client('config')


def evaluate_compliance(configuration_item):
    if configuration_item["resourceType"] not in APPLICABLE_RESOURCES:
        return {
            "compliance_type": "NOT_APPLICABLE",
            "annotation": "The rule doesn't apply to resources of type " +
            configuration_item["resourceType"] + "."
        }

    if configuration_item['configurationItemStatus'] == "ResourceDeleted":
        return {
            "compliance_type": "NOT_APPLICABLE",
            "annotation": "The configurationItem was deleted " +
                          "and therefore cannot be validated"
        }

    bucket_verConfig = configuration_item["##CHANGED##"].get("##CHANGED##")
    bucket_lifeConfig = configuration_item["##CHANGED##"].get("##CHANGED##")

    if bucket_verConfig is None:
        return {
            "compliance_type": "NON_COMPLIANT",
            "annotation": 'Bucket does not contain a Versioning Configuration.'
        }
    else:
        if bucket_verConfig['##CHANGED##'] == "Off":
            return {
                "compliance_type": "NON_COMPLIANT",
                "annotation": 'Bucket Versioning is disabled.'
            }

    if bucket_lifeConfig is None:
        return {
            "compliance_type": "NON_COMPLIANT",
            "annotation": 'Bucket does not contain a Lifecycle Management Policy'
        }

    if (bucket_lifeConfig['rules'][0]['noncurrentVersionTransitions'][0]['days'] > 0) and \
        (bucket_lifeConfig['rules'][0]['noncurrentVersionTransitions'][0]['storageClass'] == "##CHANGED##"):
        return {
            "compliance_type": "COMPLIANT",
            "annotation": 'Bucket Versioning is enabled and Lifecycle policy is set to archive older versions to Glacier'
        }
    else:
        return {
            "compliance_type": "NON_COMPLIANT",
            "annotation": 'Bucket Lifecycle policy is not configured to specification.'
        }


def lambda_handler(event, context):
    log.debug('Event %s', event)
    invoking_event = json.loads(event['##CHANGED##'])
    configuration_item = invoking_event['##CHANGED##']
    compliance = ##REMOVED##
    evaluation = {
        'ComplianceResourceType': invoking_event['configurationItem']['resourceType'],
        'ComplianceResourceId': invoking_event['configurationItem']['resourceId'],
        'ComplianceType': compliance["compliance_type"],
        "Annotation": compliance["annotation"],
        'OrderingTimestamp': invoking_event['configurationItem']['configurationItemCaptureTime']
    }

    log.debug('===== Compliance Status: %s', json.dumps(evaluation))
    if "dryRun" not in event:
        config.put_evaluations(
           Evaluations=[evaluation],
           ResultToken=event['resultToken']
        )

    return evaluation['ComplianceType']
