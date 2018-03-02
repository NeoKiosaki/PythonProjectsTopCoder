import sys

def isWhiteLine(s):
    return not bool(s and s.strip())

f = open(sys.argv[1],"r")
s = f.readlines()
for line in s:
    if not isWhiteLine(line):
        print(line,end='')