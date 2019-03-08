passwords = {'email':'dsfakljskdjf:LKJ:LJK',
             'blog':'sfasdDFASDfsf12'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('usage:py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
