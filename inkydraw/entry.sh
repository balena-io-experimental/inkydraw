#!/bin/sh

echo "Running CMD..."
cd /usr/app/src/
uvicorn server:app --host 0.0.0.0 --port 8080
