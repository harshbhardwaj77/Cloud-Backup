import boto3
import os
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Configure logging
logging.basicConfig(filename='backup_report.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Define backup parameters
SOURCE_DIR =  '/path/to/source_directory' # Local directory to back up
BUCKET_NAME = 'your_bucket_name'  # S3 bucket name
S3_PREFIX = 'backup/'  # Optional: Prefix for files in the bucket

def upload_to_s3():
    s3 = boto3.client('s3')
    try:
        for root, dirs, files in os.walk(SOURCE_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                s3_key = os.path.join(S3_PREFIX, os.path.relpath(file_path, SOURCE_DIR))
                print(f"Uploading {file_path} as s3://{BUCKET_NAME}/{s3_key}")  # Debug output
                s3.upload_file(file_path, BUCKET_NAME, s3_key)
                logging.info(f"Uploaded {file_path} to s3://{BUCKET_NAME}/{s3_key}")
        logging.info("Backup completed successfully.")
    except NoCredentialsError:
        logging.error("AWS credentials not found.")
    except PartialCredentialsError:
        logging.error("Incomplete AWS credentials.")
    except Exception as e:
        logging.error(f"Backup failed: {e}")


if __name__ == "__main__":
    upload_to_s3()
