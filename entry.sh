#!/bin/sh

# Run the display update once on container start
# python /usr/app/src/update-display.py

echo "Running CMD..."

# TODO: Run the server instead and draw based on HTTP request data.
# python /usr/app/src/update-display.py
cd /usr/app/src/
uvicorn server:app --port 80
