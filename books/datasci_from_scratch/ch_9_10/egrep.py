'''
Created on Apr 7, 2017

@author: angel
'''
import sys, re

regex = sys.argv[1]

for line in sys.stdin: #for every line passed in
    if re.search(regex, line): #match the regex and write it out
        sys.stdout.write(line)