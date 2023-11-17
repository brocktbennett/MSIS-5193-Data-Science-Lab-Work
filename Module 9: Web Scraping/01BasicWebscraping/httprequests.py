import requests
from bs4 import BeautifulSoup

# Sent HTTP get request and return a response
rep = requests.get('http://www.columbia.edu/~fdc/sample.html')

# Print requested URL
print(rep.url)

# print response status code
print(rep.status_code)

# print response HTML content
print(rep.content)

# parsing the HTML
soup = BeautifulSoup(rep.content, 'html.parser')
print(soup.prettify())