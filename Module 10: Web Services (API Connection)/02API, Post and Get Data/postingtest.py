import tweepy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv("/Users/brocktbennett/GitHub/MSIS-5193-Data-Science-Lab-Work/Module 10: Web Services (API Connection)/gitignore/.env")  # Adjust this path to your .env file's location

# Use environment variables
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_SECRET')

# Authenticate to Twitter
try:
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
except Exception as e:
    print(f"Error during authentication: {e}")

def post_tweet(tweet_text):
    try:
        api.update_status(tweet_text)
        print("Tweet posted successfully.")
    except Exception as e:
        print(f"Error posting tweet: {e}")

# Example usage
post_tweet("Hello Twitter!")