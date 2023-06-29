#!/bin/bash
# Displays the byte size of the HTTP response header for a giver URL

curl -s "$1" | wc -c
