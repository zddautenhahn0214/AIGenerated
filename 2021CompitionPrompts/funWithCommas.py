# Create an empty list to store the words
words = []

# Loop until the user enters "quit"
while True:
    # Read a word from the user
    word = input()

    # If the word is "quit", stop looping
    if word == "quit":
        break

    # Add the word to the list
    words.append(word)

# Initialize the result string with the first word in the list
result = words[0]

# Loop through the rest of the words in the list
for i in range(1, len(words)):
    # If this is the second-to-last word, add it to the result
    # with the word "and" before it
    if i == len(words) - 1:
        result += " and " + words[i]
    # Otherwise, add it to the result with a comma before it
    else:
        result += ", " + words[i]

# Print the result
print(result)
