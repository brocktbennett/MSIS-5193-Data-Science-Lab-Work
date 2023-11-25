import json
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
# Update the path to your .env file if necessary
load_dotenv("/Users/brocktbennett/GitHub/MSIS-5193-Data-Science-Lab-Work/Module 11: Web Services for Data Analytics/.env")

# Retrieve API key and other details from environment variables
api_key = os.getenv('api_key')
serviceurl = os.getenv('serviceurl')
address = os.getenv('address')

# Print out the retrieved values for verification only (comment out if needed)
print("API Key:", api_key)
print("Service URL:", serviceurl)
print("Address:", address)

# Construct the full request URL
requrl = serviceurl + address + '&key=' + api_key

# Printing out the requested URL for testing
print(requrl)

# Perform the web request
response = requests.get(requrl)

# Check if response is successful
if response.status_code != 200:
    print(f"Error fetching geolocation data: {response.status_code}")
    exit(1)

# Decode the content and convert to JSON format
geolocation = response.content.decode()
jsonlocation = json.loads(geolocation)

# Check if results are available
if not jsonlocation["results"]:
    print("No results found for the given address.")
    exit(1)

# Extract address components
addresscomponentslist = jsonlocation["results"][0]["address_components"]
print(addresscomponentslist)

# Initialize variable to store county name
county = ''

# Loop through the address components to find the county name
for component in addresscomponentslist:
    if 'administrative_area_level_2' in component['types']:
        county = component['long_name']
        break

# Print the county name or a message if not found
if county:
    print("County:", county)
else:
    print("County name not found in address components.")
