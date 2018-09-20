#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import subprocess
import sys

from pip._vendor.distlib.compat import raw_input

my_path = os.path.dirname(os.path.realpath(__file__))


def do_cat():
    inp = input("")
    print(inp)
    if inp != 'quit':
        do_cat()
    else:
        sys.exit(1)


def do_cat_file(file_name, my_command):
    if not os.path.isfile(file_name):
        print("file does not exist")
        get_action(None)
    else:
        subprocess.call(['./shell/p3-exec.py', file_name, my_command])


def do_ls():
    dir_path = os.getcwd()
    print(os.listdir(dir_path))


def do_cd(arg1):
    print("in do_cd")
    print(arg1)
    os.chdir(arg1.split(' ')[1])
    return os.path.dirname(os.path.realpath(__file__))


def command_valid(command):
    if 'cd' or 'cat' or '|' or 'ls' or '>' or '<' or '>>' or '<<' in command:
        return True
    return False


def do_command(command):
    num_of_spaces = command.count(' ')
    print('do_command: ', command)
    if command == 'quit' or command == 'q' or command == 'Q' or command == 'Quit':
        sys.exit(1)
    elif command == "help":
        print("$ commands you can run: \n >> quit \n >> help \n >> cat")
    elif command == 'cat' and num_of_spaces == 0:
        do_cat()
    elif 'cd' in command:
        return do_cd(command)
    else:
        os.system(command)
    get_action(my_path)

# parses the user input to a valid command string. Lets say the user types in 'cd' myShell will interpret this as cd.
def parse_user_input(inp):
    try:
        input_file = inp
        output_file = open("shell_input.txt", 'w')
        wordcount = {}

        for word in input_file.replace('-', ' ').replace("‘", ' ').replace("’", ' ').replace("'", ' ').split():
            word = re.sub('[^A-Za-z0-9]+', '', word)
            word = word.lower()
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

        for key in sorted(wordcount.keys()):
            output_file.write("%s %s " % (key, wordcount[key]) + "\n")
    except IndexError:
        print('expected argument is invalid')

    return inp


def get_action(path):
    if not path:
        directory = my_path + "$ "
    else:
        directory = path + "$ "

    inp = input(directory)
    parsed_input = parse_user_input(inp)
    if command_valid(parsed_input):
        directory = do_command(parsed_input)
    else:
        print(">> command ", inp, "is invalid type [help] to view commands you can run")
    get_action(directory)


if __name__ == "__main__":
    get_action(None)


cmd = ["./myShell.py"]

process = subprocess.Popen(cmd,
                           shell=False,
                           bufsize=0,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

for line in iter(process.stdout.readline, ""):
    print(line)
    if line.rstrip() == "$ ":
        r = raw_input()
        process.stdin.write(r)
