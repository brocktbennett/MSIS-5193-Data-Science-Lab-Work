import os
from dotenv import load_dotenv
import tweepy

# Load environment variables
load_dotenv("/Users/brocktbennett/GitHub/MSIS-5193-Data-Science-Lab-Work/Module 10: Web Services (API Connection)/TweetAPItest/gitignore/donotopen.gitignore")

# Use environment variables
api_key = os.getenv('API_KEY')
api_secrets = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secrets)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')


