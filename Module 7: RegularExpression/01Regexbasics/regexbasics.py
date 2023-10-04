import re  # Importing regular expression library

# Filtering words based on a pattern
wordlist = ["color", "colour", "work", "working", "fox", "worker", "working"]  # Words list

print("Words containing '.or' pattern:")
for word in wordlist:
    if re.search('.or', word):
        print(word)
print("===================")

# Filtering sentences that start with 'The'
sentences1 = [
    "The sun is shining",
    "Apples are delicious",
    "The moon is bright",
    "Birds are singing"
]

print("Sentences starting with 'The':")
for s in sentences1:
    if re.search('^The', s):
        print(s)
print("===================")

# Filtering sentences that end with 'ing'
print("Sentences ending with 'ing':")
for s in sentences1:
    if re.search('ing$', s):
        print(s)
print("===================")

# Filtering sentences starting with 'Subject' or 'Date'
sentences2 = [
    "Subject: abc is here!",
    "Date: 2023-09-05",
    "The Subject to discuss...",
    "Action from Date ..."
]

print("Sentences starting with 'Subject' or 'Date':")
for s in sentences2:
    if re.search('^(Subject|Date)', s):
        print(s)
print("===================")

# Filtering sentences containing 'Subject to' or 'Date to'
sentences3 = [
    "Subject: abc is here!",
    "Date: 2023-09-05",
    "The Subject to discuss...",
    "Action from Date to..."
]

print("Sentences containing 'Subject to' or 'Date to':")
for s in sentences3:
    if re.search('(Subject|Date) to', s):
        print(s)
print("===================")

# Filtering sentences containing '!' or '?'
sentences4 = [
    "Subject: abc is here!",
    "Date: 2023-09-05",
    "The Subject to discuss...?",
    "Action from Date to..."
]

print("Sentences containing '!' or '?':")
for s in sentences4:
    if re.search('[!?]', s):
        print(s)
print("===================")
