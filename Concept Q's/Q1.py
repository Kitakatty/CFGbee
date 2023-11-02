def is_isogram(input_string):
    # Convert input to lowercase to make the comparison case-insensitive
    input_string = input_string.lower()

    # Use a set to keep track of seen characters
    seen_chars = set()

    for char in input_string:
        # If the character is already in the set, it's a repeat, so return False
        if char in seen_chars:
            return False
        # Otherwise, add the character to the set
        seen_chars.add(char)

    # If the loop completes without returning False, it means it's an isogram
    return True

print(is_isogram("isogram"))  # Output: True
print(is_isogram("uncopyrightable"))  # Output: True
print(is_isogram("ambidextrously"))  # Output: True
print(is_isogram("hello"))  # Output:False

