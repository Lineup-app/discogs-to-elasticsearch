YEAR=$(date +'%Y')
BASEDIR=$(dirname "$0")

EXCTRACTED=$BASEDIR/source/$2
FILENAME=$BASEDIR/source/$2.xml.gz 

rm -rf $BASEDIR/source/
mkdir $BASEDIR/source/

curl https://discogs-data.s3-us-west-2.amazonaws.com/data/$YEAR/discogs_$1_$2.xml.gz --output $FILENAME
python $BASEDIR/xmlsplit.py $2 $FILENAME
