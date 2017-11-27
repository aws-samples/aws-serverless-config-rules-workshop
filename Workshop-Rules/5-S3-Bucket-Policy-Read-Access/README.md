# S3 Bucket Policy Protection
Completion of this rule will require you to create a Lambda function and custom Config Rule using the yet-to-be complete code provided in [`rule.py`](./rule.py).  The method and process of creating a new Lambda function and new custom Config Rule will mirror Module 1, no additional permissions are required.  All that will differ are the code for the Lambda function, and the configuration of the Config Rule.

## The Purpose of This Rule
Access control for the objects stored in Amazon S3 buckets can be managed via a bucket policy.  Bucket policies allow you to define which identity principals have the ability to perform some or all of the available S3 API operations for that bucket and the data within it.  A change to a Bucket policy could change who has access to the data within the bucket, or even make it publicly available (which may be intended for many use cases, like public website assets). **For this scenario, we would like all buckets that allow read access to only provide that access to a specific IAM role with the name: ConfigRulesWorkshopTestRole.**  Any buckets that allow read access to Principals other than ConfigWorkshopTestRole are noncompliant.

### Hints for Completion
1. The Step Functions State Machine will create the ConfigRulesWorkshopTestRole as described in the above purpose. Because IAM roles must be uniquely named in each account, if you create this role during your testing, be sure to delete it before executing the State Machine.
2. Think about all the different S3 actions that would enable object read access to a bucket (http://docs.aws.amazon.com/IAM/latest/UserGuide/list_s3.html).  Limit your rule to evaluate Bucket policies, ACLs are out of scope.

Region| Launch
------|-----
EU (Ireland) | [![Launch Module 5 in eu-west-1](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=ConfigRules-Module-5-S3-Bucket-Policy-Whitelist&templateURL=https://s3.amazonaws.com/config-rules-workshop-eu-west-1/module-5/template.yml)
