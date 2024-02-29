#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept
curl -s -o /dev/null -I -w "%{header[Allow]}" "$1"
