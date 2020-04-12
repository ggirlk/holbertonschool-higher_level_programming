#!/bin/bash
#cURL body size
curl -sI $1 | grep "HTTP/1.1" | cut -d " " -f2
