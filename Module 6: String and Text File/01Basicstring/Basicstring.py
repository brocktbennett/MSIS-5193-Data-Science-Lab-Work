# Initialize a string variable 's' with a greeting message.
s = 'Hello, OSU friends!'
print(f"Initialized string: {s}\n")

# Print the length of the string 's'.
print(f"The length of the string is: {len(s)} characters.\n")

# Extract and print the substring "Hello" from the string 's'.
hello_substring = s[:5]
print(f"Extracted substring from the start to the 5th character: {hello_substring}\n")

# Check if the substring 'OSU' is present within the string 's'.
if 'OSU' in s:
    print("'OSU' is present in the string.\n")
else:
    print("'OSU' is not found in the string.\n")

# Similarly, check if the substring 'OK' is present within the string 's'.
if 'OK' in s:
    print("'OK' is present in the string.\n")
else:
    print("'OK' is not found in the string.\n")

# Print the last character of the string 's'.
print(f"The last character of the string is: {s[-1]}\n")
