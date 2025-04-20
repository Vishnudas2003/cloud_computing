import boto3

# Use Ohio region
ecr_client = boto3.client("ecr", region_name="us-east-2")

repository_name = "my-cloud-native-repo"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response["repository"]["repositoryUri"]
print("Repository URI:", repository_uri)
