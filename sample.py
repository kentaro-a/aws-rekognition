import os,sys
import boto3
from pprint import pprint

# Consts.
MaxLabels = 30      # Maximum amount of tags in Rekognition response.
MinConfidence=70    # Minimum confidence that tags to be fetched in Rekognition response.


# Create AWS-Rekognition client with my ~/.aws/credential.
#  -- Currently, Rekognition API isn't provided on the region of Asia/Pacific, So using "us-east-1".
client = boto3.client("rekognition", region_name="us-east-1")

# Upload dir path.
image_dir_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "images")

# Upload images.
files = os.listdir(image_dir_path)
for original_name in files:
	image = os.path.join(image_dir_path, original_name)
	with open(image, 'rb') as image:
		response = client.detect_labels(Image={'Bytes': image.read()}, MaxLabels=MaxLabels, MinConfidence=MinConfidence)
		# Dump response.
		pprint(response)


