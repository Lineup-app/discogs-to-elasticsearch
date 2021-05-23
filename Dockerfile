FROM nikolaik/python-nodejs:python3.7-nodejs10
RUN pip3 install awscli --upgrade --user
RUN pip3 install xmltodict
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

COPY ./src /src

RUN /src/download.sh 20200501 artists
RUN /src/bulkes.sh artists