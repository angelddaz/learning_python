'''
Created on Apr 23, 2017

@author: angel
3-5      DONE
6-8      DONE
9-10     DONE
11-13    
14-16    
17-19    
20-22    
23-25    
'''
#CHAPTER 11
#machine learning chapter
from books.datasci_from_scratch.ch_9_10.line_count import count
from sympy.utilities.autowrap import _validate_backend_language

'''
What is a model? It�s simply a specification of a mathematical 
(or probabilistic) relationship that exists between different variables. 
'''
import random

def split_data(data, prob):
    #split data into fraction [prob, 1 - prob]
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results

def train_test_split(x, y, test_pct):
    data = zip(x, y)
    train, test = split_data(data, 1 - test_pct)
    x_train, y_train = zip(*train)
    x_test, y_test = zip(*test)
    return x_train, x_test, y_train, y_test

#chapter 12: k-nearest neighbors
from collections import defaultdict, Counter 
def majority_vote(labels):
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])
    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1])

def knn_classify(k, labeled_points, new_point):
    by_distance = sorted(labeled_points, key=lamba (point, _):distance(point, new_point))
    k_nearest_labels = [label for _, label in by_distance[:k]]
    return majority_vote(k_nearest_labels)

#chapter 13
#It's pretty clear to me that I don't understand Baye's theorem as well as I should

