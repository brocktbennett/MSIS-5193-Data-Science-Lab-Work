import re

# List of sample strings to test against regular expressions
sentences = [
    "aa",
    "ab",
    "abc",
    "abcabcabc",
    "a8qa",
    "abcca"
]

# Demonstrating the '*' quantifier: Matches 0 or more repetitions of the preceding pattern
print("===== quantifier * ====")

# Matches 'a' followed by 0 or more 'bc'
print("Matches 'a' followed by 0 or more 'bc':")
for s in sentences:
    if re.search('abc*', s):
        print(s)

# Matches 'a' followed by any character(s) and ending with 'a'
print("Matches 'a' followed by any character(s) and ending with 'a':")
for s in sentences:
    if re.search('a.*a', s):
        print(s)

# Matches 'a' followed by 0 or more 'bc'
print("Matches 'a' followed by 0 or more 'bc':")
for s in sentences:
    if re.search('a(bc)*', s):
        print(s)

# Matches a string starting with 'a', followed by any character(s), and ending with 'a'
print("Matches a string starting with 'a', followed by any character(s), and ending with 'a':")
for s in sentences:
    if re.search('a.*a$', s):
        print(s)

# Demonstrating the '+' quantifier: Matches 1 or more repetitions of the preceding pattern
print("\n===== quantifier + ====")

# Matches 'a' followed by 1 or more 'bc'
print("Matches 'a' followed by 1 or more 'bc':")
for s in sentences:
    if re.search('abc+', s):
        print(s)

# Matches 'a' followed by 1 or more of any character and ending with 'a'
print("Matches 'a' followed by 1 or more of any character and ending with 'a':")
for s in sentences:
    if re.search('a.+a', s):
        print(s)

# Matches 'a' followed by 1 or more 'bc'
print("Matches 'a' followed by 1 or more 'bc':")
for s in sentences:
    if re.search('a(bc)+', s):
        print(s)

# Matches a string starting with 'a', followed by 1 or more of any character, and ending with 'a'
print("Matches a string starting with 'a', followed by 1 or more of any character, and ending with 'a':")
for s in sentences:
    if re.search('a.+a$', s):
        print(s)

# Demonstrating the '?' quantifier: Matches 0 or 1 repetition of the preceding pattern
print("\n===== quantifier ? ====")

# Matches 'a' followed by 0 or 1 'bc'
print("Matches 'a' followed by 0 or 1 'bc':")
for s in sentences:
    if re.search('abc?', s):
        print(s)

# Matches 'a' followed by 0 or 1 of any character and ending with 'a'
print("Matches 'a' followed by 0 or 1 of any character and ending with 'a':")
for s in sentences:
    if re.search('a.?a', s):
        print(s)

# Matches 'a' followed by 0 or 1 'bc'
print("Matches 'a' followed by 0 or 1 'bc':")
for s in sentences:
    if re.search('a(bc)?', s):
        print(s)

# Matches a string starting with 'a', followed by 0 or 1 of any character, and ending with 'a'
print("Matches a string starting with 'a', followed by 0 or 1 of any character, and ending with 'a':")
for s in sentences:
    if re.search('a.?a$', s):
        print(s)

# Demonstrating the '{min, max}' quantifier: Matches between min and max repetitions of the preceding pattern
print("\n===== quantifier {min, max} ====")

# Matches 'a' followed by between 1 and 2 'bc'
print("Matches 'a' followed by between 1 and 2 'bc':")
for s in sentences:
    if re.search('abc{1,2}', s):
        print(s)

# Matches a string with 2 or more 'a'
print("Matches a string with 2 or more 'a':")
for s in sentences:
    if re.search('a{2,}', s):
        print(s)

# Matches a string with 0 or 1 'ab'
print("Matches a string with 0 or 1 'ab':")
