# Read the contents of input.txt
with open('input.txt', 'r') as file:
    content = file.readlines()

# Count the number of words
word_count = sum(len(line.split()) for line in content)

# Convert all text to uppercase
uppercase_content = [line.upper() for line in content]

# Write the processed text and the word count to output.txt
with open('output.txt', 'w') as file:
    file.write("".join(uppercase_content))
    file.write(f"\nWord Count: {word_count}\n")

# Print a success message
print(
    "Successfully created output.txt with processed content "
    "and word count.\n"
)
# Display the processed content and word count
print("Processed content:")
# print the uppercase content
print(f"{''.join(uppercase_content)}")
# print the word count
print(f"Total words counted: {word_count}")
