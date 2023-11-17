from bs4 import BeautifulSoup

# Open the HTML file for reading
with open('/Users/brocktbennett/GitHub/Project Data/Data Science Programming Data/test.html', 'r') as f:
    contents = f.read()  # Read the content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(contents, "html.parser")

# Print the names of all HTML elements in the document
for child in soup.descendants:
    if child.name:
        print(child.name)

# Print the content of the first 'h2' tag
print("Content in h2 tags:")
print(soup.h2)

# Print the content of the first 'ul' tag
print("Content in ul tags:")
print(soup.ul)

# Print the text content of the first 'h2' tag without tags
print("Text in h2 tags without tags:")
print(soup.h2.text)

# Print the text content of the first 'ul' tag without tags
print("Text in ul tags without tags:")
print(soup.ul.text)

# Find all 'li' tags and print their text content
print("Text content of all 'li' tags:")
for tag in soup.find_all('li'):
    print(tag.text)

# Find the 'ul' tag with id 'proxytypes'
print("Content of 'ul' tag with id 'proxytypes':")
print(soup.find('ul', id='proxytypes'))
