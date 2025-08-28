#!/bin/sh
# exit when any command fails
set -e

# install dependencies
pip install --no-cache-dir -r requirements.txt

# run the main application
exec uvicorn main:app --host 0.0.0.0 --port 80 --reload
