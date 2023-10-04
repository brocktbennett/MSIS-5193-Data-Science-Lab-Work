import re

# Display type of variable
stuff = 'Hello world'
print(f"Type of 'stuff': {type(stuff)}\n")

# List all functions in the string library
print("All functions available in the string library for 'stuff':")
print(dir(stuff))
print("\n")

greet = 'Hello Bob'
print(f"Original string: {greet}\n")

# Convert all characters to uppercase
nnn = greet.upper()
print(f"Uppercase: {nnn}")

# Convert all characters to lowercase
www = greet.lower()
print(f"Lowercase: {www}\n")

# Replace 'Bob' with 'Jane'
nstr = greet.replace('Bob', 'Jane')
print(f"Replaced 'Bob' with 'Jane': {nstr}")

# Replace 'o' with 'X'
nstr = greet.replace('o', 'X')
print(f"Replaced 'o' with 'X': {nstr}\n")

# Strip spaces
greet = ' Hello Bob '
print(f"Original string with spaces: '{greet}'")
print(f"After left strip: '{greet.lstrip()}'")
print(f"After right strip: '{greet.rstrip()}'")
print(f"After stripping both sides: '{greet.strip()}'\n")

# Split into list of words
line = 'Hello Bob'
print(f"Original line: {line}")
words = line.split(' ')
print(f"Split by space: {words}")

line = 'Hello, Bob'
print(f"\nOriginal line: {line}")
words = line.split(',')
print(f"Split by comma: {words}")

words = re.split(", | ", line)
print(f"Split by space or comma: {words}\n")

# String operations with 'abracadabra'
s = 'abracadabra'
print(f"String: {s}")
print(f"First index of 'a': {s.index('a')}")
print(f"Index of 'rac': {s.index('rac')}")
print(f"Count of 'a': {s.count('a')}")
print(f"Count of 'b': {s.count('b')}")
print(f"Count of 'x': {s.count('x')}")
