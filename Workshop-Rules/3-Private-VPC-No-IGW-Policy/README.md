# No IGWs for Private VPCs
Completion of this rule will require you to create a Lambda function and custom Config Rule using the yet-to-be complete code provided in [`rule.py`](./rule.py).  The method and process of creating a new Lambda function and new custom Config Rule will mirror Module 1.  This Lambda function *will* require different permissions in the policy for its IAM role, and it's code requires completion as well.

## The Purpose of This Rule
Whether it be to build internal applications whose audiences should always be on a private network, or to reduce the attack surface of an application that stores highly sensitive data, not all applications need access to the Internet.  This Config Rule's purpose is to ensure that VPCs that have a tag key equal to `private` do not have an Internet Gateway (IGW) attached to them.  If a VPC is found to both contain a tag key of `private` and an IGW is attached, it is noncompliant.

### Hints for Completion
1. Because this rule requires a call to another AWS service for evaluation, **test events provided are inadequate on their own**. They have stubbed/non-existent VPCs listed within them for evaluation.  In order for the rule calls to other services to be successful, you will need to create compliant/noncompliant VPCs within the region you are testing (noncompliance means an IGW attached to a VPC tagged with the key `private`). Then replace the false VPC Ids of the provided events with the appropriate/existing VPC Ids for each respective test.
2. Remember to use the provided sample events to test your function rule. ...The test events may also provide a good reference for the evaluations your code should perform.
3. While AWS Config provides detailed configuration information for many resources, it may not provide all of the details you need to fully evaluate a resource within the event object passed to your Lambda function.  For cases like this, you may want to use the resource information that *is* passed within the event object, and then make request/s to other AWS services to gather more data to make a full evaluation.
4. When other AWS services need to be called by your Lambda function, remember to take those actions into account when creating an IAM role for your function.

Region| Launch
------|-----
EU (Ireland) | [![Launch Module 3 in eu-west-1](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=ConfigRules-Module-3-No-IGW-For-Private-VPCs&templateURL=https://s3.amazonaws.com/config-rules-workshop-eu-west-1/module-3/template.yml)
