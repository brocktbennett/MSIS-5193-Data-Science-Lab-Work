import json
import requests

# If you have a Google Places API key, enter it here
api_key = 'AIzaSyBtIk8oI03aB6aYkhIvhZI6qhsJLlKjdTQ'

# set the service url regular part
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?address='

# specify the address
address = '370%20Business%20Building%20Stillwater%20OK%2074078'

# get the full url by putting all the string together
requrl = serviceurl+address+'&key='+api_key

# web request
r = requests.get(requrl)


# get the content and convert to string
geolocation = r.content.decode()

# convert the string to JSON format
jsonlocation = json.loads(geolocation)


# get the address component out as a list
addresscomponentslist= jsonlocation["results"][0]["address_components"]

print(addresscomponentslist)

county=''

# loop through the address components list to find county name
for i in range(0,len(addresscomponentslist)):
    if addresscomponentslist[i]['types'][0] == 'administrative_area_level_2':
        county = addresscomponentslist[i]['long_name']

print(county)