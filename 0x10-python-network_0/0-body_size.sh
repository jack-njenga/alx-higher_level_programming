#!/bin/bash
# takes in url sends a request and displays the size of th body of the responce
curl -sL "$1" | wc -c
