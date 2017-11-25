import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

APPLICABLE_RESOURCES = ["AWS::EC2::SecurityGroup"]
config = boto3.client("config")


def evaluate_compliance(configuration_item, whitelist_ip):
    compliance_status = "COMPLIANT"

    if configuration_item["resourceType"] not in APPLICABLE_RESOURCES:
        return "NOT_APPLICABLE"

    for perms in configuration_item["configuration"]["ipPermissions"]:
        if "toPort" in perms and perms["toPort"] == 22:
            for range in perms["ipRanges"]:
                if range != whitelist_ip:
                    compliance_status = "NON_COMPLIANT"

    return compliance_status


def lambda_handler(event, context):
    logger.info("Event: " + json.dumps(event))
    invoking_event = json.loads(event["invokingEvent"])
    rule_parameters = json.loads(event["ruleParameters"])
    configuration_item = invoking_event["configurationItem"]
    result_token = "No token found."
    if "resultToken" in event:
        result_token = event["resultToken"]

    evaluation = {
        "ComplianceResourceType":
            configuration_item["resourceType"],
        "ComplianceResourceId":
            configuration_item["resourceId"],
        "ComplianceType":
            evaluate_compliance(configuration_item, rule_parameters["ipAddress"]),
        "Annotation":
            "SSH Access is allowed to not allowed IP addess range",
        "OrderingTimestamp":
            configuration_item["configurationItemCaptureTime"]
    }
    if "dryRun" not in event:
        config.put_evaluations(
            Evaluations=[evaluation],
            ResultToken=result_token
            )

    return evaluation['ComplianceType']
