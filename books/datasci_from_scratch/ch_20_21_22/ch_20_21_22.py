'''
Created on Apr 23, 2017

@author: angel
3-5      DONE
6-8      DONE
9-10     DONE
11-13    DONE
14-16    DONE
17-19    DONE
20-22    HARDEST
23-25    EASIESTEST
'''

#chapter 20 NATURAL LANGUAGE PROCESSING

def fix_unicode(text):
    return text.replace(u"\u2019", "'")

from bs4 import BeautifulSoup
import requests
url = "http://radar.oreilly.com/2010/06/what-is-data-science.html"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')
content = soup.find("div", "entry-content") # find entry-content div
regex = r"[\w']+|[\.]" # matches a word or a period
document = []

import re
for paragraph in content("p"):
    words = re.findall(regex, fix_unicode(paragraph.text))
    document.extend(words)

from collections import defaultdict

bigrams = zip(document, document[1:])
transitions = defaultdict(list)
for prev, current in bigrams:
    transitions[prev].append(current)

import random

def generate_using_bigrams():
    current = "." # this means the next word will start a sentence
    result = []
    while True:
        next_word_candidates = transitions[current] # bigrams (current, _)
        current = random.choice(next_word_candidates) # choose one at random
    result.append(current) # append it to results
    if current == ".": return " ".join(result) # if "." we're done

#CHAPTER 21 NETWORK ANALYSIS
