# Cloud-Backup
Python Script to Backup data to AWS S3 
# S3 Backup Utility

This script performs a backup of a local directory to an Amazon S3 bucket. It recursively uploads files from the specified source directory to the S3 bucket, with an optional prefix for organizing files in the bucket.

## Requirements

- Python 3.x
- Boto3 (`pip install boto3`)
- AWS credentials configured on your system

## Configuration

1. **Set Up AWS Credentials**: Ensure you have AWS credentials configured. You can set these up using the AWS CLI or by manually creating a credentials file at `~/.aws/credentials`.

2. **Edit the Script**: Modify the following variables in the `backup_script.py` to suit your needs:
   - `SOURCE_DIR`: Path to the local directory you want to back up.
   - `BUCKET_NAME`: Name of the S3 bucket where the backup will be stored.
   - `S3_PREFIX`: Optional prefix for organizing files in the S3 bucket.

## Usage

1. Clone this repository or download the script.

2. Run the script:
   ```bash
   python backup_script.py
