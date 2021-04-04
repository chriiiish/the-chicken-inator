from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
from aws_cdk import aws_s3 as s3


class TheChickenInatorStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The S3 bucket that stores the files
        S3_BUCKET = s3.Bucket(self, 'big-ol-bucket-of-files', public_read_access=False)

        # Access Point
        ACCESS_POINT_CONFIGURATION = s3.CfnAccessPoint.PublicAccessBlockConfigurationProperty(
            block_public_acls=False
        )
        ACCESS_POINT = s3.CfnAccessPoint(self, 'access-point', bucket=S3_BUCKET.bucket_name, public_access_block_configuration=ACCESS_POINT_CONFIGURATION)

        #TODO: So it turns out CDK, indeed CloudFormation doesn't support this so I guess I'm going to wait here
