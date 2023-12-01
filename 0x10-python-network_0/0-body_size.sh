#!/bin/bash
# This script takes a URL as an argument, and sends a request using curl,
# and displays the size of the response body in bytes.

curl -sI "$url" | grep -i 'Content-Length:' | cut -d' ' -f2