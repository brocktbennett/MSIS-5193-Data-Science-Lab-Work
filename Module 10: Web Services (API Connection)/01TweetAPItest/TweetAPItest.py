import os
from dotenv import load_dotenv
import tweepy

# Load environment variables
# Update the path to where your .env file is located
load_dotenv("/Users/brocktbennett/GitHub/MSIS-5193-Data-Science-Lab-Work/Module 10: Web Services (API Connection)/gitignore/.env")  # Adjust this path to your .env file's location

# Use environment variables
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')  # Renamed from api_secrets for consistency
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_SECRET')

# Authenticate to Twitter (x.com)
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print('Successful Authentication from Twitter(X.com)')
except Exception as e:  # Catching a general exception, specify if needed
    print(f'Failed authentication: {e}')
