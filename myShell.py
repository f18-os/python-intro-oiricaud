#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
import sys

from pip._vendor.distlib.compat import raw_input


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
        get_action()
    else:
        subprocess.call(['./shell/p3-exec.py', file_name, my_command])


def do_ls():
    dirpath = os.getcwd()
    print(os.listdir(dirpath))


def get_action():
    inp = input("$ ")
    num_of_spaces = inp.count(' ')
    if num_of_spaces > 0:
        split_me = inp.split(' ')
        do_cat_file(split_me[1], split_me[0])
    if inp == 'cat' and num_of_spaces == 0:
        do_cat()
    elif inp == 'ls':
        do_ls()
    elif inp == 'quit' or inp == 'q' or inp == 'Q' or inp == 'Quit':
        sys.exit(1)
    elif inp == "help":
        print("$ commands you can run: \n >> quit \n >> help \n >> cat")
    else:
        print(">> command ", inp, "is invalid type [help] to view commands you can run")
    get_action()


if __name__ == "__main__":
    get_action()


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
