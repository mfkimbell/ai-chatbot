#!/bin/bash
set -e

# Run AWS Configure with Environment Variables
aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
aws configure set region $AWS_DEFAULT_REGION

# Run Streamlit
streamlit run chatbot_frontend.py
