import requests
from bs4 import BeautifulSoup
import re

print("Making a GET request")
r = requests.get('http://www.columbia.edu/~fdc/sample.html')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Getting the title tag
print(soup.title)

print("Getting the name of the tag")
print(soup.title.name)

# Getting the name of parent tag
print(soup.title.parent.name)

print("=====================")
# get all text in h3 - the header of the sections
for tag in soup.find_all('h3'):
    print(tag.text)

print("=====================")
# get all tag a
for tag in soup.find_all('a'):

    # check if tag a had ref link
    if tag.has_attr('href'):

        # get the content of the ref link
        reflink = tag['href']

        # check if it is an external link, use regex
        if re.search('(http)', reflink):
            print(reflink)

