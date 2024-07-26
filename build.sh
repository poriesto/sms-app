#!/bin/bash

#wget https://1drv.ms/u/s!Aic8RIOhSb1wo6drmG62SULxVeQSDQ?e=FAb8GM
docker load -i astra-python.tar
docker build -f web-app/Dockerfile -t sms:175 .
docker build -f sms-db/Dockerfile -t sms-db:175 .

docker-compose up -d