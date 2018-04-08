#!/usr/bin/env python
"""reducer.py"""

#References: http://www.michael-noll.com/tutorials

from operator import itemgetter

import sys
import csv

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print '%s\t%s' % (current_word, current_count)
	    with open("wc1.csv", 'a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([current_word,current_count])
        current_count = count
        current_word = word

if current_word == word:
    print '%s\t%s' % (current_word, current_count)
    with open("wc1.csv", 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([current_word,current_count])