#!/bin/bash
# Sends json POST request to a URL with a JSON file.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
