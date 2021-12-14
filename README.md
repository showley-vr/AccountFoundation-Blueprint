# AWS Account Foundation - Account Vending Machine
This is the Account Foundation repository for Vertical Relevance's AWS Account Foundation blueprint. The code in this repository deploys our Account Vending Machine product which configures baseline SCPs and deploys baseline infrastructure into newly created accounts based on their classification within the organization. The steps below outline the process to deploy this solution.

# Prior to starting the setup of the environment, ensure that you have cloned this repo.

## Configure Control Tower

  1. Create a new account to serve as the organization's Management Account.
  2. Use the Management Account to deploy a default Control Tower Landing Zone. Once started, this will take approximately 45 minutes to complete. The result will be an AWS Organization with some basic configurations completed. For instance, there will be some baseline Organizational Units, SCP guardrails, and SSO configured.
  3. Set up Customizations for Control Tower (CfCT) by launching the following CloudFormation Template 
     (https://console.aws.amazon.com/cloudformation#/stacks/new?stackName=CustomizationsForCTSolution&templateURL=https://s3.amazonaws.com/solutions-reference/customizations-for-aws-control-tower/latest/custom-control-tower-initiation.template)
      For "CodePipeline Source" select CodeCommit. Otherwise, leave all parameters as the default.

## Use CDK App Code to Deploy Scripts to Bucket
### Follow the instructions below to setup CDK environment.
Follow the setup steps below to properly configure the environment and first deployment of the infrastructure.
To manually create a virtualenv on MacOS and Linux:

$ python3 -m venv .venv
After the init process completes and the virtualenv is created, you can use the following step to activate your virtualenv.

$ source .venv/bin/activate
If you are on a Windows platform, you would activate the virtualenv like this:

% .venv\Scripts\activate.bat
Once the virtualenv is activated, you can install the required dependencies.

$ pip install -r requirements.txt

Bootstrap the cdk app.

cdk bootstrap
At this point you can deploy the CDK app for this blueprint.

$ cdk deploy

Now that you have depl

## Update manifest.yml
