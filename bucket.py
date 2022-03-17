import pulumi
import pulumi_aws as aws

bucket = aws.s3.Bucket("bucketpulumitest",
    acl="private",
    tags={
        "Environment": "Dev",
        "Name": "My bucket",
    })
