#!/bin/bash

docker run --name elasticsearch -d -p 9200:9200 --name webserver elasticsearch
