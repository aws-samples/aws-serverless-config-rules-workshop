# No VPC Overlap with On Premises Network
Completion of this rule will require you to create a Lambda function and custom Config Rule using the yet-to-be complete code provided in `rule.py`.  The method and process of creating a new Lambda function and new custom Config Rule will mirror Module 1, with no additional permissions required.  All that will differ are the code for the Lambda function, and the configuration of the Config Rule.

## The Purpose of This Rule
One of the more foundational and rigid implementation decisions that you make while building applications on AWS is the CIDR block/IP range of a new VPC.  Creating a VPC that has an overlapping IP range with an existing network could prevent future integration of the networks without using potentially complex Network Address Translation.  **The purpose of this rule is to ensure that no VPCs have an overlapping IP range with existing on-premises networks.**  There are two on premises networks that VPC IP ranges should not overlap with - 10.218.0.0/24, and 10.218.1.0/24.  

### Hints for Completion
1. Remember to use the provided sample events to test your function rule. ...The test events may also provide a good reference for the evaluations your code should perform.
2. In order to leverage a Python library within your function code, make sure you import it first.

Region| Launch
------|-----
EU (Ireland) | [![Launch Module 4 in eu-west-1](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=ConfigRules-Module-4-No-Overlapping-IP-Ranges&templateURL=https://s3.amazonaws.com/config-rules-workshop-eu-west-1/module-4/template.yml)
