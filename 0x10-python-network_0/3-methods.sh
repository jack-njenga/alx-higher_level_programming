#!/bin/bash
# takes url and displays all http methods the server accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
