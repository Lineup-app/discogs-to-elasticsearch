### Discogs to Elasticsearch

this library creates a docker file which then downloads and parses a data dump from discogs
and uploads the output to elastic search

required parameters:

AWS_ACCESS_KEY
AWS_SECRET
AWS_REGION
AWS_ES_URL


libraries used in this repo

xml parser https://github.com/martinblech/xmltodict
aws header sign https://github.com/riboseinc/aws-authenticating-secgroup-scripts
aws curl https://github.com/okigan/awscurl