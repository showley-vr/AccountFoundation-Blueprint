# AccountFoundation-Blueprint
This is the blueprint for a basic implementation of Vertical Relevance's Account Foundation solution.

TODO:
DONE -- CDK Script Deployment Project Structure -- Sean
  Acceptance Criteria: Deploy all of the files in the scps, stacksets, and supplementary_files directories to a S3 bucket for consumption.
  
**SCPs**
Top-Level SCPs (2 SCP Policy Docs) -- Sean
  Acceptance Criteria: Deploy baseline scps (e.g. no root access, etc). This should consist of 2 scp policies due to size restrictions
Business Unit SCP -- Unassigned
  Acceptance Criteria: Deploy an SCP with at least one business unit specific policy
DONE -- Prevent Creation of IGW -- Josh
  Acceptance Criteria: Create and test an SCP policy that prevents the creation of an IGW for the accounts in the OU it is attached to.
 
**StackSets**
DONE -- Delete Default Networking Components CFN Template -- Sean
  Acceptance Criteria: Create a CFN template that deploys and triggers a lambda function that deletes the default VPC and default security group
DONE -- 3-Tier VPC -- Josh
  Acceptance Criteria: Create a CFN template that deploys a VPC with a public subnet, private subnet, NAT gateway, route table, etc.
