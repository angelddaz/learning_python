# CH3: Dictionaries and Sets
# in this chapter we will cover: dictionary methods, special handling for missing keys, variations of dict in std library
# sets and frozenset types
# implications of hash tables (key type limitations, unpredictable ordering, etc.)

# Generic Mapping Types
import collections
from collections import abc
my_dict = {}
print(isinstance(my_dict, abc.Mapping))

# a tuple is only hashable if all of it's elements are hashable
tt = (1, 2, (30, 40)) # does not work if third element is a list, instead of a tuple
print(hash(tt))
# however, a frozenset works
tf = (1, 3, frozenset([30, 40]))
print(hash(tf))

