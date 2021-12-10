# AWS Account Foundation - Account Vending Machine
This is the Account Foundation repository for Vertical Relevance's AWS Account Foundation blueprint. The code in this repository deploys our Account Vending Machine product which configures baseline SCPs and deploys baseline infrastructure into newly created accounts based on their classification within the organization. The steps below outline the process to deploy this solution.

## Configure Control Tower

  1. Create a new account to serve as the organization's Management Account.
  2. Use the Management Account to deploy a default Control Tower Landing Zone. Once started, this will take approximately 45 minutes to complete. The result will be an AWS Organization with some basic configurations completed. For instance, there will be some baseline Organizational Units, SCP guardrails, and SSO configured.
  3. 

## Use CDK App Code to Deploy Scripts to Bucket


## Update manifest.yml
