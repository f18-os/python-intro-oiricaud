import re
import sys


def countWordsInFile():
    file = open(sys.argv[1], "r+")
    blah = open(sys.argv[2], 'w')
    wordcount = {}

    for word in file.read().split():
        '-' in word
        '-' not in word

        word = re.sub('[^A-Za-z0-9]+', '', word)
        word = word.lower()

        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    for key in wordcount.keys():
        # print("%s %s " % (key, wordcount[key]))
        blah.write("%s %s " % (key, wordcount[key]) + "\n")
    file.close();


if __name__ == '__main__':
    print("This only executes when %s is executed rather than imported" % __file__)
    countWordsInFile()
