# amazons3cmdlinetools
Command-Line Amazon S3 Bucket Uploader, Downloader and Bucket Creator

Change The Following Lines As Needed Within The Script:

# Access Id here
access_id = "xxx" 
# Access Key here
access_key = "yyyyyy"

# Check that your region, endpoint and service area match.  That is >> "s3" below match your settings
region = "us-east-2"

endpoint = "s3-{}.amazonaws.com".format(region)

auth = aws4auth.AWS4Auth(access_id, access_key, region, "s3")

# Example:

./bucketCMD.py create_bucket s3bucketnamehere

./bucketCMD.py upload_file  s3bucketnamehere myFileOnAmazonServer.jpg ./path/to/file/locally/myFileOnAmazonServer.jpg public-read

/bucketCMD.py download_file s3bucketnamehere myFileOnAmazonServer.jpg ./path/to/saved/locally/myFileOnAmazonServer.jpg
