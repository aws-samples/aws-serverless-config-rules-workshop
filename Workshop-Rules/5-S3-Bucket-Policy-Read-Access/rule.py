import ##CHANGED##
import ##CHANGED##
import logging


APPLICABLE_RESOURCES = ["##CHANGED##"]
config = boto3.client("##CHANGED##")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def evaluate_compliance(invoking_event, whitelisted_role):

    if invoking_event['configurationItem']['resourceType'] not in APPLICABLE_RESOURCES:
        return "##CHANGED##"

    if invoking_event['configurationItem']['configurationItemStatus'] == "ResourceDeleted":
        return "##CHANGED##"

    compliance_status = "COMPLIANT"

    configuration_diff = invoking_event['configurationItemDiff']
    account_id = ##LINED_REMOVED: where can this be retrieved from?##
    policy_text = ##LINE_REMOVED: where can this be retrieved from?##

    #Convert the string policy above to JSON
    b = bytes(policy_text, encoding='ascii')
    policy = json.loads(b.decode('unicode-escape'))
    logger.info("POLICY: " + json.dumps(policy))

    if 'Statement' in policy:
        for statement in policy['##CHANGED##']:
            if 'Action' in statement and 'Principal' in statement:
                if ##LINE_REMOVED: does this Action give permission to perform read actions?##:
                    if 'AWS' not in statement['Principal'] or statement['Principal']['AWS'] != ##LINE_REMOVED: what is the principal value allowed to be?##:
                        compliance_status = "NON_COMPLIANT"

    return compliance_status


def lambda_handler(event, context):

    logger.info("Event: " + json.dumps(event))

    invoking_event = json.loads(event["invokingEvent"])
    rule_parameters = json.loads(event["ruleParameters"])
    whitelisted_role = rule_parameters["##CHANGED##"]
    configuration_item = invoking_event['configurationItem']
    if not invoking_event['##CHANGED##']:
        return "Nothing to check, resource didn't change."

    result_token = "No token found."
    if "resultToken" in event:
        result_token = event["resultToken"]


    compliance = evaluate_compliance(invoking_event, whitelisted_role)

    evaluation = {
        ##LINES_REMOVED: how do we create the evaluation object that Config requires?##
    }

    if "dryRun" not in event:
        ##LINES_REMOVED: how do we inform config that this evlauation has completed?##

    return evaluation['ComplianceType']
