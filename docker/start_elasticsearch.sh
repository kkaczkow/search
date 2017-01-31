#!/bin/bash
docker run -p 9200:9200 -e "http.host=0.0.0.0" -e "transport.host=127.0.0.1" docker.elastic.co/elasticsearch/elasticsearch:5.2.0
#docker run --name docker.elastic.co/elasticsearch/elasticsearch:5.2.0 -d -p 9200:9200 --name webserver elasticsearch
