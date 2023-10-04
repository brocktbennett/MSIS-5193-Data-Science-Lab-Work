# Define a function to count the number of lines in a file.
def count_lines(file_path):
    # Use a context manager to automatically handle file closure.
    with open(file_path, 'r') as f:
        # Return the sum of lines by iterating over each line in the file.
        return sum(1 for _ in f)

# Define a function to read the entire content of a file.
def read_file_content(file_path):
    with open(file_path, 'r') as f:
        # Return the complete content of the file as a single string.
        return f.read()

# Define a function to print lines from the file that start with a given prefix.
def print_lines_starting_with(file_path, prefix):
    with open(file_path, 'r') as f:
        for line in f:
            # Check if the line starts with the given prefix.
            if line.startswith(prefix):
                # Remove trailing whitespaces and newlines and print the line.
                print(line.rstrip())

# Define a function to print lines from the file containing a given substring.
def print_lines_containing(file_path, substring):
    with open(file_path, 'r') as f:
        for line in f:
            # Check if the line contains the specified substring.
            if substring in line:
                # Remove trailing whitespaces and newlines and print the line.
                print(line.rstrip())

# Define a constant file path for reuse.
# This ensures that the file path is consistent across all function calls.
FILE_PATH = '/Users/brocktbennett/GitHub/Project Data/mbox.txt'

# Call the function to count lines in the file and print the result.
print('Line Count:', count_lines(FILE_PATH))

# Call the function to read the entire file.
# Display the total number of characters in the content and the first 20 characters.
content = read_file_content(FILE_PATH)
print(len(content))
print(content[:20])

# Call the function to print lines starting with 'From:'.
print_lines_starting_with(FILE_PATH, 'From:')

# Call the function to print lines containing the domain 'uct.ac.za'.
print_lines_containing(FILE_PATH, 'uct.ac.za')
