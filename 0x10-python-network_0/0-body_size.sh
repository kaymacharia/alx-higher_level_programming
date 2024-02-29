#!/bin/bash
# Use curl to get the response and save the body size
response_size=$(curl -s -o /dev/null -w "%{size_download}" "$url")
