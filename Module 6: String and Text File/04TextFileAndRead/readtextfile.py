# Open the text file
xfile = open('/Users/brocktbennett/GitHub/Project Data/mbox.txt')

# Read and print lines from the text file, showing the length including the newline character
print("Reading file lines including newline character length:\n")
for line in xfile:
    print(line, end='')  # To avoid double spacing when printing
    print(len(line))  # The length includes the newline character

# Since file objects are iterators, we need to reset the pointer to the beginning to read it again
xfile.seek(0)

print("\nReading file lines excluding newline character length:\n")
# Read and print lines from the text file, showing the length excluding the newline character
for line in xfile:
    stripped_line = line.strip("\n")  # Remove the newline character at the end
    print(stripped_line)
    print(len(stripped_line))

# Close the file after reading
xfile.close()
