#!/usr/bin/env python3

import sys
import requests
import requests_aws4auth as aws4auth
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import mimetypes

# Access Id here
access_id = "xxx" 
# Access Key here
access_key = "yyyyyy"

# Check that your region, endpoint and service match area below match
region = "us-east-2"
endpoint = "s3-{}.amazonaws.com".format(region)
auth = aws4auth.AWS4Auth(access_id, access_key, region, "s3")
ns = "http://s3.amazonaws.com/doc/2006-03-01"

def xml_pprint (xml_string):
	print (minidom.parseString (xml_string).toprettyxml() )

def display_error (xml_object):

	print ( "Status code : {}".format( xml_object.status_code) )
	for element in ET.fromstring ( xml_object.text ) :
		print ( "{} : {}".format ( element.tag, element.text ) )

def create_bucket (bucket):
	print ("Bucket name : {}".format (bucket))
	XML = ET.Element ("CreateBucketConfiguration")
	XML.attrib["xmlns"] = ns
	location = ET.SubElement (XML, "LocationConstraint")
	location.text = auth.region
	data = ET.tostring (XML, encoding="utf-8")
	url = "http://{}.{}".format (bucket, endpoint)
	r = requests.put (url, data=data, auth=auth)
	if r.ok:
		print ("Created bucket {} OK".format(bucket) )
	else :

		display_error ( r )

def upload_file (bucket, s3_name, local_path, acl="private" ):
	data = open (local_path, "rb").read()
	url = "http://{}.{}/{}".format(bucket, endpoint, s3_name)
	headers = {"x-amz-acl": acl}
	mimetype = mimetypes.guess_type(local_path)[0]

	r = requests.put (url, data=data, headers=headers, auth=auth)
	if mimetype:
		headers["Content-Type"]= mimetype
	if r.ok :
		print ("Uploaded {} OK".format(local_path))
	else :
		xml_pprint(r.text)

def download_file (bucket, s3_name, local_path ):
	url = "http://{}.{}/{}".format ( bucket, endpoint, s3_name)
	print ("Using The Following URL : {}".format (url) )
	r = requests.get (url, auth=auth)
	if r.ok:
		open (local_path, "wb").write(r.content)
		print ("Downloaded {} OK as {}".format(s3_name, local_path ))
	else:
		display_error (r)


if __name__ == "__main__" :
	cmd, *args = sys.argv[1:]
	globals () [cmd] (*args)


