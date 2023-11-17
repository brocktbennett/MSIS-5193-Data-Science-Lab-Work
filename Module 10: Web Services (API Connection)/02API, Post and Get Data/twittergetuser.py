import tweepy
from dotenv import load_dotenv
import os

# Load environment variables
# Update the path to where your .env file is located
load_dotenv("/Users/brocktbennett/GitHub/MSIS-5193-Data-Science-Lab-Work/Module 10: Web Services (API Connection)/gitignore/.env")  # Adjust this path to your .env file's location

# Use environment variables
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')  # Renamed from api_secrets for consistency
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

# initialize API
api = tweepy.API(auth, wait_on_rate_limit=True)

# get user information
user = api.get_user(screen_name='President Biden')
print(user)

# show user information
print(f"user.name: {user.name}")
print(f"user.screen_name: {user.screen_name}")
print(f"user.location: {user.location}")
print(f"user.description: {user.description}")
print(f"user.followers_count: {user.followers_count}")
print(f"user.listed_count: {user.listed_count}")
print(f"user.statuses_count: {user.statuses_count}")
print(f"user.id: {user.id}")
