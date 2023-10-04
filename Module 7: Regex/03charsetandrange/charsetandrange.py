import re

# List of sentences for the character set search
Sentences = ["aa", "ab*", "abc", "abcabcabc", "a8qa", "abcca"]

# Searching for sentences that contain a 'c' preceded by 'a' or 'b'
print("===== Searching for character set [ab]c ====")
for s in Sentences:
    if re.search('[ab]c', s):
        print(s)

# Searching for sentences that contain one or more 'q' or 'p' characters
print("=========================")
print("===== Searching for character set [qp]+ ====")
for s in Sentences:
    if re.search('[qp]+', s):
        print(s)

# Searching for sentences that contain zero or more digits from '1' to '3'
print("=========================")
print("===== Searching for character set [123]* ====")
for s in Sentences:
    if re.search('[123]*', s):
        print(s)

# Searching for sentences that contain 'b' or '*' one or more times
print("=========================")
print("===== Searching for character set [b*]+ ====")
for s in Sentences:
    if re.search('[b*]+', s):
        print(s)

# List of sentences for the character range search
Sentences = ["aA", "ab*", "aBc", "XYZ", "a8qA", "-990"]

# Searching for sentences that contain a capital letter
print("=========================")
print("===== Searching for character range [A-Z] ====")
for s in Sentences:
    if re.search('[A-Z]', s):
        print(s)

# Searching for sentences that contain a digit from '1' to '9'
print("=========================")
print("===== Searching for character range [1-9] ====")
for s in Sentences:
    if re.search('[1-9]', s):
        print(s)

# Searching for sentences that contain characters in the range a-b, A-Z, or 1-9
print("=========================")
print("===== Searching for character range [a-bA-Z1-9] ====")
for s in Sentences:
    if re.search('[a-bA-Z1-9]', s):
        print(s)

# Searching for sentences that have a '+' or '-' followed by a digit
print("=========================")
print("===== Searching for pattern [+\-]+[0-9] ====")
for s in Sentences:
    if re.search('[+\-]+[0-9]', s):
        print(s)

# List of sentences for the negate set search
Sentences = ["aA", "ab*", "aBc", "XYZ", "a8qA", "cca"]

# Searching for sentences that contain any character other than capital letters
print("=========================")
print("===== Searching for negate set [^A-Z] ====")
for s in Sentences:
    if re.search('[^A-Z]', s):
        print(s)

# Searching for sentences that contain any character other than 'a', 'c', or 'B'
print("=========================")
print("===== Searching for negate set [^acB] ====")
for s in Sentences:
    if re.search('[^acB]', s):
        print(s)
