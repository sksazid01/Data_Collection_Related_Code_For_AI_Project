# -*- coding: utf-8 -*-

# Define possible quote characters
QUOTE_CHARS = ["'", "‘", "’"]

# Read sentences from output.txt
with open("output.txt", "r", encoding="utf-8") as infile:
    lines = infile.readlines()

filtered_sentences = []

for line in lines:
    sentence = line.lstrip()  # Remove leading spaces
    # Remove leading single quote if present
    if sentence and sentence[0] in QUOTE_CHARS:
        sentence = sentence[1:].lstrip()
    # After cleaning, skip if less than 8 words
    if len(sentence.split()) < 8:
        continue
    filtered_sentences.append(sentence.strip())

# Write to output2.txt
with open("output2.txt", "w", encoding="utf-8") as outfile:
    for sentence in filtered_sentences:
        outfile.write(sentence + "\n")
