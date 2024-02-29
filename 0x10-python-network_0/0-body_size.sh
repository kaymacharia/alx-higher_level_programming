#!/bin/bash
# Use curl to get the response and save 
curl -s -o /dev/null -w '%{size_download}n' $1
