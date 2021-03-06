'''
Created on Apr 23, 2017

@author: angel
3-5      DONE
6-8      DONE
9-10     DONE
11-13    DONE
14-16    DONE
17-19    HARD
20-22    HARDEST
23-25    EASIESTEST
'''

#Chapter 17: Decision Trees
import math
def entropy(class_probabilities):
    return sum(-p * math.log(p, 2)
               for p in class_probabilities
               if p)

from collections import Counter
from __future__ import division

def class_probabilities(labels):
    total_count = len(labels)
    return [count / total_count
            for count in Counter(labels).values()]

def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)

def partition_entropy(subsets):
    total_count = sum(len(subset) for subset in subsets)
    return sum(data_entropy(subset) * len(subset) / total_count
               for subset in subsets)

#def partition_by(inputs, attribute):
#    groups = defaultdict(list)
#    for input in inputs:
#        key = input[0][attribute]
#        groups[key].append(input)
#    return groups

'''
Given how closely decision trees can fit themselves to their training data, it's not 
surprising that they have a tendency to overfit. One way of avoiding this is a technique
called random forests
'''
# ok I'm not sure exactly what just happened in this chapter but I expected that

#CHAPTER 18: NEURAL NETWORKS
#definitely severely underqualified for this chapter

#CHAPTER 19 CLUSTERING
#again no worries.