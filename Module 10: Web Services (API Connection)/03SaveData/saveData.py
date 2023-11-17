import json
import pandas as pd
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

# initialize API
api = tweepy.API(auth, wait_on_rate_limit=True)

# get user information
user = api.get_user(screen_name='BillGates')

# Flatten data
df_nested_list = pd.json_normalize(user._json)

# show results
print(df_nested_list)

# export dataframe to CSV file
df_nested_list.to_csv("twitteruser.csv")