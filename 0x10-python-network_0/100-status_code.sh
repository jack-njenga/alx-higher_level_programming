#!/bin/bash
# sends a req url and displays the status
curl -s -o /dev/null -w "%{http_code}" "$1"
