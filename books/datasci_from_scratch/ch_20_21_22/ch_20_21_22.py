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
import path
from sgmllib import interesting

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
from collections import deque
def shortest_paths_from(from_user):
    shortest_paths_to = { from_user["id"] : [[]] }
    frontier = deque((from_user, friend)
                     for friend in from_user["friends"])
    while frontier:
        prev_user, user = frontier.popleft()
        user_id = user["id"]
        paths_to_prev_user = shortest_paths_to[prev_user["id"]]
        new_paths_to_user = [path + [user_id] for path in paths_to_prev_user]
        
        old_paths_to_user = shortest_paths_to.get(user_id, [])
        
        if old_paths_to_user:
            min_path_length = len(old_paths_to_user[0])
        else:
            min_path_length = float('inf')
        
        new_paths_to_user = [path
                             for path in new_paths_to_user
                             if len(path) <= min_path_length
                             and path not in old_paths_to_user]
        
        shortest_paths_to[user_id] = old_paths_to_user + new_paths_to_user
        
        frontier.extend((user, friend)
                        for friend in user["friends"]
                        if friend["id"] not in shortest_paths_to)
    return shortest_paths_to

users = []

for user in users:
    user["shortest_paths"] = shortest_paths_from(user)

for user in users:
    user["betweenness_centrality"] = 0.0

for source in users:
    source_id = source["id"]
    for target_id, paths in source["shortest_paths"].iteritems():
        if source_id < target_id:
            num_paths = len(paths)
            contrib = 1 / num_paths
            for path in paths:
                for id in path:
                    if id not in [source_id, target_id]:
                        users[id]["betweenness_centrality"] += contrib

#There's a good reason I suspected these would be the hardest chapters to
#understand.

#CHAPTER 22 RECOMENNDER SYSTEMS

users_interests = [
    ["Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra"],
    ["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"],
    ["Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas"],
    ["R", "Python", "statistics", "regression", "probability"],
    ["machine learning", "regression", "decision trees", "libsvm"],
    ["Python", "R", "Java", "C++", "Haskell", "programming languages"],
    ["statistics", "probability", "mathematics", "theory"],
    ["machine learning", "scikit-learn", "Mahout", "neural networks"],
    ["neural networks", "deep learning", "Big Data", "artificial intelligence"],
    ["Hadoop", "Java", "MapReduce", "Big Data"],
    ["statistics", "R", "statsmodels"],
    ["C++", "deep learning", "artificial intelligence", "probability"],
    ["pandas", "R", "Python"],
    ["databases", "HBase", "Postgres", "MySQL", "MongoDB"],
    ["libsvm", "regression", "support vector machines"]
]

from collections import Counter

popular_interests = Counter(interest
                            for user_interests in user_interests
                            for interest in user_interests).most_common()
print popular_interests

