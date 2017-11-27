# S3 Lifecycle Policy Compliance
Completion of this rule will require you to create a Lambda function and custom Config Rule using the yet-to-be complete code provided in [`rule.py`](./rule.py).  The method and process of creating a new Lambda function and new custom Config Rule will mirror Module 1, no additional or different permissions are required.  All that will differ are the code for the Lambda function, and the configuration of the Config Rule.

## The Purpose of This Rule
While the Config Rule in Module 1 was focused on security/compliance, you can also use Config Rules as a mechanism for enforcing organizational policies that are unrelated to security/compliance.  Cost Savings is another worthy pursuit for building automated compliance evaluations with Config Rules.

This rule focuses on driving cost savings, and data retention with Amazon S3. S3 allows you to create Lifecycle Policies so that the data you store is automatically moved between storage classes. **This rule should ensure that all buckets have a lifecylce policy to migrate older data to Amazon Glacier.** This enables you to realize cost savings while adhering to the data access requirements for the data you've stored.  S3 also enables the use of versioning so that previous versions of objects are retained if existing data is deleted or overwritten.  This enables additional confidence that data will not be unintentionally deleted or changed, and that previous versions of objects are retained should they need to be retrieved/restored. **This rule should also ensure that all S3 buckets have a versioning policy in place.**

### Hints for Completion
1. Remember to use the provided sample events to test your function rule. ...The test events may also provide a good reference for the evaluations your code should perform.
2. Take a look at the previous module for how the code was arranged, you might be able to use it as a reference replace the missing code!

Region| Launch
------|-----
EU (Ireland) | [![Launch Module 2 in eu-west-1](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=ConfigRules-Module-2-S3-Bucket-Lifecycle-and-Verisoning&templateURL=https://s3.amazonaws.com/config-rules-workshop-eu-west-1/module-2/template.yml)
