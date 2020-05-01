"""
Converts csv from https://www.vicinitas.io/ to markov-able text file
"""

import csv
import re
import string

INPUT_FILE = "../media/unprepared/text/tweet_data.csv"
OUTPUT_FILE = "../media/prepared/text/tweets.txt"

with open(INPUT_FILE) as tweet_data:
    with open(OUTPUT_FILE, 'w') as output:
        for csv_line in csv.DictReader(tweet_data):
            line = csv_line['Text']
            line = "".join(filter(lambda x: x in string.printable, line))
            line = re.sub(r'((@\w+)|(https?:\/\/\S+)) ?', "", line)
            if not re.search(r'(^RT)|(^\w*$)', line):
                output.write(line.replace("\n", " ") + "\n")