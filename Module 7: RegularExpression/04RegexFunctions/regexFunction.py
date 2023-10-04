import re

# Searching within a string
x = 'My 2 favorite numbers are 19 and 42'

# Find all numbers in the string and return as a list
y = re.findall('[0-9]+', x)
print("All numbers:", y)

# Find words containing an uppercase letter followed by one or more non-whitespace characters
y = re.findall('[A-Z]\S+', x)
print("Words with uppercase followed by non-whitespace:", y)

# Find all uppercase characters A, B, or C in the string
y = re.findall('[ABC]', x)
print("Uppercase characters [ABC]:", y)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# Find the email address in the string
y = re.findall('\S+@\S+', x)
print("Email address:", y)

# Extract the domain from the email address
y = re.findall('@([^ ]*)', x)
print("Email domain:", y)

# Process file to extract email addresses
filename = 'mbox-short.txt'
print(f"Processing file: {filename}")

emaillist = list()

try:
    with open(filename, 'r') as hand:
        for line in hand:
            line = line.rstrip()

            # Find email addresses in each line
            stuff = re.findall('[a-zA-Z.]+@[a-zA-Z.]+', line)

            # If any email addresses were found, add them to the final email list
            if stuff:
                emaillist.extend(stuff)

    print("Extracted email addresses:", emaillist)

except FileNotFoundError:
    print(f"Error: File {filename} not found.")
