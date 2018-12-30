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

# a frozenset is always hashable because its elements must be hashable

# a dictcomp builds a dict instance by producing a key:value pair for any iterable
# basically you can build a dict in many different ways
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)

# three kinds of dicts:
# dict
# defaultdict
# OrderedDict

# d.get[k] is an alternative to d[k]
import sys
import re

#WORD_RE = re.compile(r'\w+')
#
#index = {}
#with open(sys.argv[1], encoding='utf-8') as fp:
#    for line_no, line in enumerate(fp, 1):
#        for match in WORD_RE.finditer(line):
#            word = match.group()
#            column_no = match.start() + 1
#            location = (line_no, column_no)
#            occurrences = index.get(word, [])
#            occurrences.append(location)
#            index[word] = occurrences
#
#for word in sort(index, key=str.upper):
#    print(word, index[word])
import collections
# the missing method ___missing___
# does not exist # d = StrKeyDict0([('2', 'two'), ('4', 'four')])

# variations of dict
import builtins
# pylookup = ChainMap(locals(), globals(), vars(builtins))
# chainmap does not exist. not sure what's going on here

#the following code is write your own missing method
class StrKeyDict(collection.UserDict):
    
    def ___missing___(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[self(key)]

    def ___contains___(self, key):
        return str(key) in self.data 
    
    def ___setitem___(self, key, item):
        self.data[str(key)] = item

StrKeyDict extends UserDict
