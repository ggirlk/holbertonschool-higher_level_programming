#!/bin/bash
#cURL body size
curl -sI "$1" --write-out "%{http_code}" --silent --output /dev/null
