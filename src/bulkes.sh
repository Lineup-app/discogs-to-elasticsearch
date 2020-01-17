echo "directory $1"
for entry in "$1"/*.json
do
  if [ -f "$entry" ];then
    echo "uploading: $entry"
    awscurl -XPOST --service es 'https://search-discogs-7rqowgsnruxdngtidx56le5vyy.eu-west-1.es.amazonaws.com/_bulk' --data @"$entry" -H 'Content-Type: application/json' --region eu-west-1    
    rm $entry
  fi
done