#! /usr/bin/env python3
import sys
current_word = ''
current_count = 0
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)
    if current_word == word:
        current_count += count
    else:
        if current_word != '':
            print(current_word + '\t' + str(current_count))
        current_word = word
        current_count = count
if current_word == word:
        print(current_word + '\t' + str(current_count))