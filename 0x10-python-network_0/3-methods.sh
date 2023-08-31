#!/bin/bash
# takes url and displays all http methods the server accept
curl -sX --head OPTIONS "$1" | grep -o "Allow.*"|cut -c 8-
