#!/bin/bash

echo "Checking files to format..."
black web --exclude '__pycache__' --exclude 'migrations' --ckeck --verbose

echo "Formatting ..."
black web --exclude '__pycache__' --exclude 'migrations'
echo "Done :)"