import sys
import re

finame = sys.argv[1]
foname = sys.argv[2] if sys.argv[2] else sys.stdout

with open(finame, 'rb') as fi:
    text = fi.read()
    L = re.sub('^\s*- .*(\n).*```', '\n\n')
