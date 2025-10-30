#!/bin/bash

# Start virtual environment
source .venv/bin/activate

# Set environment variables
export AWS_ACCESS_KEY_ID=AKIASHHGUSVQQYAY52SW
export AWS_SECRET_ACCESS_KEY=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
export AWS_REGION=us-east-1

# Start the Flask application
python app.py