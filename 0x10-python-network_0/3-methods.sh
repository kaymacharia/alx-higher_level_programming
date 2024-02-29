#!/bin/bash
#takes in a URL and displays all HTTP methods
curl -sI $1 | header Allow | cut -d ' ' -f2-
