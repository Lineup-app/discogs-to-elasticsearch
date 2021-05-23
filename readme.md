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

# manual curls

awscurl -XPOST --service es 'https://search-discogs-7rqowgsnruxdngtidx56le5vyy.eu-west-1.es.amazonaws.com/_bulk' --data @artists0.json -H 'Content-Type: application/json' ---region eu-west-1
