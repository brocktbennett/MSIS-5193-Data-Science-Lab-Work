import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

r = requests.get('https://www3.uwsp.edu/infotech/Pages/Email/Faculty-Email-Address-Information.aspx')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# initialize an empty email list
emaillist = list()

# get all tag p
for tag in soup.find_all('p'):
    # assign text of tag p to new variable line
    line = tag.text

    # find all emails in the line
    stuff = re.findall('[a-zA-Z.]+@[a-zA-Z.]+', line)
    if len(stuff) >= 1:  # check if the returned list is not empty
        for i in range(len(stuff)):  # go through the returned list
            stuff[i] =stuff[i].rstrip('.')
            emaillist.append(stuff[i])  # add the emails to the final email list
print(emaillist)

df = pd.DataFrame({'email': emaillist})
df.to_csv('emails.csv', index=False, encoding='utf-8')



