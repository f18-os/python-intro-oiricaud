#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re

try:
    my_file = sys.argv[1]
    my_output = sys.argv[2]
    input_file = open(my_file, "r+")
    output_file = open(my_output, 'w')
    wordcount = {}

    for word in input_file.read().replace('-', ' ').replace("‘", ' ').replace("’", ' ').replace("'", ' ').split():
        word = re.sub('[^A-Za-z0-9]+', '', word)
        word = word.lower()
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    for key in sorted(wordcount.keys()):
        output_file.write("%s %s " % (key, wordcount[key]) + "\n")
        input_file.close()
except IndexError:
    print('expected argument is invalid')

