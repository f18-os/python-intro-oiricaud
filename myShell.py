#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
import sys

from pip._vendor.distlib.compat import raw_input

myPath = os.path.dirname(os.path.realpath(__file__))

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
    dirpath = os.getcwd()
    print(os.listdir(dirpath))


def do_cd(arg1):
    print("in do_cd")
    print(arg1)
    os.chdir(arg1.split(' ')[1])
    myPath = os.path.dirname(os.path.realpath(__file__))
    return myPath


def command_valid(command):
    if 'cd' or 'cat' or '|' or 'ls' in command:
        return True
    return False


def do_command(command):
    num_of_spaces = command.count(' ')
    print('do_command: ', command)
    if command == 'quit' or command == 'q' or command == 'Q' or command == 'Quit':
        sys.exit(1)
    elif command == "help":
        print("$ commands you can run: \n >> quit \n >> help \n >> cat")
    elif command == 'cat' and num_of_spaces > 0:
        split_me = command.split(' ')
        do_cat_file(split_me[1], split_me[0])
    elif command == 'cat' and num_of_spaces == 0:
        do_cat()
    elif 'cd' in command:
        return do_cd(command)
    else:
        os.system(command)


def get_action(path):
    if not path:
        directory = myPath + "$ "
    else:
        directory = path + "$ "

    inp = input(directory)
    if command_valid(inp):
        directory = do_command(inp)
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
