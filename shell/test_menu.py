#!/usr/bin/env python
import sys
action_text = '''
5. Perform addition
6. Perform subtraction
Q. Quit
#: '''
sys.stdout.write(action_text); sys.stdout.flush()
inp = sys.stdin.read()
print(inp)