#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, time, re
import subprocess



def do_state_machine():
    try:
        command = sys.argv[1]
        if command == "cw":  # count words in a text file
            arg1 = input('Enter file you want to read \n $ ')
            print(arg1)
            arg2 = input('Name the file of the output \n $ ')
            print(arg2)
           # count_words_in_file(arg1, arg2)

        if command == "pipe":  # waits for process 1 to complete and use it's output for process 2
            arg1 = input('Enter first command you want to use e.g cat, cw, wc, ls etc. \n $ ')
            print(arg1)
            arg2 = input('Enter second command you want to use e.g cat, wc, ls etc. \n $ ')
            print(arg2)

    except IndexError:
        try:
            user_input = input('$ ').split(' ')
            text_file = user_input[1]
            my_command = user_input[0]
            if my_command == "cw":
                subprocess.call(['./shell/wordCount.py', text_file, my_command])
                do_state_machine()
            else:
                subprocess.call(['./shell/p3-exec.py', text_file, my_command])
                do_state_machine()

        except IndexError:
            do_state_machine()


if __name__ == '__main__':
    do_state_machine()