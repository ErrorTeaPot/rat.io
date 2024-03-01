import os

# Open the suffixes file and read the suffixes into a list
with open('suffix/domainNames.txt', 'r') as f:
    suffixes = [line.strip() for line in f]

# Open the gutenberg file and read the words into a list
with open('dictionaries/dicFR.txt', 'r') as f:
    words = [line.strip() for line in f]

# Find the words that end with any of the suffixes and add a space between the word and the suffix
matched_words = [word + ' ' + suffix for word in words for suffix in suffixes if word.endswith(suffix)]

# Create /output directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

# Write the matched words to a new file
with open('output/matched_words.txt', 'w') as f:
    f.write('\n'.join(matched_words))
