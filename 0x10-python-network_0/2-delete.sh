#!/bin/bash
#Sends a delete request to the URL passed as the first argument
curl -sX DELETE "$1"
