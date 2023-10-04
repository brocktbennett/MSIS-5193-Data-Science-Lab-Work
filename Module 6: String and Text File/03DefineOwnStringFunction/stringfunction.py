def middle(text):
    """
    Returns the middle third of the provided text.

    Parameters:
    - text: a string

    Returns:
    - string: middle third of the input text
    """
    # Get length of text
    size = len(text)

    # Calculate the start and end indices of the middle third
    start = size // 3
    end = 2 * size // 3

    # Extract the middle third of the text
    result = text[start:end]

    return result


def firstparens(text):
    """
    Returns the substring enclosed by the first set of parentheses.

    Parameters:
    - text: a string with ()

    Returns:
    - string: content inside the first set of parentheses
    """
    # Find the index of the opening parenthesis
    start = text.index('(')

    # Extract the portion of the text AFTER the opening parenthesis
    tail = text[start + 1:]

    # Find the index of the closing parenthesis in the tail
    end = tail.index(')')

    # Return the substring inside the parentheses
    return tail[:end]


# Test the middle function
s = 'aabbcc'
print(f"Original string: {s}")
print(f"Middle third: {middle(s)}\n")

# Test the firstparens function
s = 'Hello, Welcome to OSU (Spears) School of Business (Stillwater)!'
print(f"Original string: {s}")
print(f"Content inside the first set of parentheses: {firstparens(s)}")
