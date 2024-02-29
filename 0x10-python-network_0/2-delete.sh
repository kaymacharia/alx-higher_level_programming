#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Define the URL from the argument
url="$1"

# Use curl to send a DELETE request and display the response body
curl -X DELETE -s "$url"
