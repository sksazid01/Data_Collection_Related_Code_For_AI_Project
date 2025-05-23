# -*- coding: utf-8 -*-

# Read input.txt
with open("input.txt", "r", encoding="utf-8") as infile:
    text = infile.read()

# Split into sentences at Bangla full stop
raw_sentences = text.split('।')

# Clean, filter (min 8 words, max 17 words), and re-add full stop
sentences = []
for sentence in raw_sentences:
    cleaned = sentence.strip()
    words = cleaned.split()
    if 8 <= len(words) <= 17:
        sentences.append(cleaned + '।')

# Write output.txt
with open("output.txt", "w", encoding="utf-8") as outfile:
    for sentence in sentences:
        outfile.write(sentence + "\n")
