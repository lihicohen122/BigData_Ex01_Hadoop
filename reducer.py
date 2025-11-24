#!/usr/bin/env python
"""reducer.py"""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    word_totals = {}
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all [current_word, count] items
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            word_totals[current_word] = total_count
        except ValueError:
            # count was not a number, so silently discard this item
            pass

    top_three = sorted(word_totals.items(), key=lambda x: x[1], reverse=True)[:3]

    for word, count in top_three:
        print("%s%s%d" % (word, separator, count))

if __name__ == "__main__":
    main()