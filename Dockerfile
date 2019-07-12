FROM nikolaik/python-nodejs:python3.7-nodejs10
RUN pip3 install awscli --upgrade --user
RUN pip3 install xmltodict
COPY ./src /src

RUN /src/download.sh 20190601 artists