# chapter two is the start of part 2: data structures
# Chapter 2. An Array of Sequences

# list comprehensions opens the door to generator expressions
# list comprehensions AKA listcomps
# generator expressions AKA genexps

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# generating the cartesian product of two lists.
# tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts)

# now with a nested for loop
# for color in colors:
#     for size in sizes:
#         print((color, size))

# listcomps build lists. to fill up other sequence types, genexps is the way to go

# genexps - Generator Expressions
# to build tuples, arrays, and other types of sequences.

import array
symbols = '$¢£¥€'
print(array.array('I', (ord(symbol) for symbol in symbols)))

# now to get the cartesian product with genexp
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    hi = 1
    #print(tshirt)
# so you don't have to generate lists for each for loop this way

# tuples are not just immutable lists. They can serve as records without field names too.
# given that tuples order of data is immutable, we can use it for records in which the ordering
# of data is critical to the definition of the data itself
# for example: coordinates or traveler ids

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport) # the %s is a string variable we can pass in to the print

# not interested in the second variable so the underscore is a dummy variable
for country, _ in traveler_ids:
    print(country)

# the for loop knows how to retrieve the items of a tuple separately - unpacking

# tuple unpacking

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
# print(latitude, longitude)
# swapping variables
# a, b = b, a

a, b, *rest = range(5)
print(a, b)

from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo.population)
print(tokyo[2])

# slicing
l = [10, 20, 30, 40, 50, 60]
print(l[:2])
print(l[2:])
print(l[3:])

# printing every third char
s = 'bicycle'
print(s[::3])
print(s[::-1]) # reversed
print(s[::-2]) # every second char reversed

l = list(range(10))
print(l)
l[2:5] = [20, 30] # replace spaces 2 to 4 with 20, 30
print(l)
del l[5:7] # delete spaces 5 to 6
print(l)
l[3::2] = [11, 22] # replace the third index and every 2nd with these two values in order
print(l)

l = [1, 2, 3]
print(l * 5)

# lists of lists yay
# example
board = [['_'] * 3 for i in range(3)] # a list of 3 lists. each of length 3
# the for loop creates 3 of the lists. the multiplication expands the list that the for loop
# is working with.
board = [['_'] * 2 for i in range(3)] # a list of 3 lists. each of length 2

weird_board = [['_'] * 3] * 3 

weird_board[1][2] = '0' # this does not mean list row, index 2
print(weird_board)
# it actually means row 1, column 2
# as the start of each new list is a new row
# list 1 = row 1
# list 2 = row 2
# .
# .
# .
# list n = row n

board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print(board)

board[2][0] = 'X' # so what this means is row 3 and column 1 with 0 indexing
# is changed to X
print(board)

# and that is it for lists of lists. pretty cool.

# Augmented Assignment with Sequences
# this means plus equals and times equals.

# the special method or dunder method that makes += work is __iadd__
# it stands for in-place addition
# if a in a += b does not have __iadd__ available to it, then it will use __add__ as normal
# it seems like generally mutable sequences have iadd available to them and immutable ones
# do not

# example of imul with a mutable sequence
l = [1, 2, 3]
print(id(l))
l *= 2
print(l)
print(id(l))

# example of imul with an immutable sequence
l = (1, 2, 3)
print(id(l))
l *= 2
print(l)
print(id(l))
# a new tuple was created, and the location in memory is different for second sequence
# this immutable sequence is a tuple

# t = (1, 2, [30, 40])
# t[2] += [50, 60]
# print(t)
# the above three lines do not work in python 3.6.6
# putting mutable items inside of tuples is not a good idea

# list.sort and the sorted built-in function
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits)) # abc order
# two extra parameters
print(sorted(fruits, key=len, reverse = True))

# Managing Ordered Sequences with bisect
# two main functions from the bisect module; bisect and insort.
# they use the binary search algorithm to find and insert items in an ordered sequence

# must be an ordered sequence
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  | '
        print(ROW_FMT.format(needle, position, offset))
from os import sys
import bisect

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    
    print('DEMO:', bisect_fn.__name__)
    print('haystack - >', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

# bisect can take in arguments 'lo' and 'hi'
# bisect is an implicit name for bisect_right

def grade(score, breakpoints = [60, 70, 80, 90], grades = 'FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

# applying the function grade for each of the values inside of this list
# note the index name used in the for loop is the same name as the value passed into
# the grade funciton 'score' == 'score'
print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100, -12]])

# now to insert with bisect.insort
import random
SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

# like bisect, insort takes optional lo, hi args to limit the search to a sub-sequence

# sequences include lists, tuples, and arrays.
# if you are handling lists of numbers, arrays are the way to go
# the rest of the chapter is dedicated to arrays

# When a list is not the answer
# if you are constantly adding and removing data, FIFO, a deque works faster
# deque is a double-ended queue

# sets are good for fast membership cecking, they are not sequences as they are unordered
''' # commented out so it stops creating a new file every time
from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats2 == floats)
'''
# time for memory views
# the built in memoryview class lets you handle slices of arrays without copying bytes

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))

# deques and other queues
from collections import deque
dq = deque(range(10), maxlen = 10)
dq.rotate(3) # no need for assignment. rotate moves right three to front
# like a snake's tail entering the mouth of 0 in that direction
print(dq)
dq.rotate(-4)
print(dq) # and then back again almost to normal but one step further.
# snake head is on the very right of the queue
dq.appendleft(-1)
print(dq)
dq.extend([11, 22, 33])
print(dq)
dq.extendleft([10, 20, 30, 40])
print(dq)

# chapter summary
'''
standard library sequence types is great fundamentals for writing concise, effective,
and idiomatic python code. Not sure what idiomatic means but sure. I think it means
within the expected dialect or practices of python. Pythonic I guess?

Tuples play two roles: records with unnamed fields and as immutable lists
When a tuple is used as a record, tuple unpacking is the safest, most readable way
of getting at the data or fields.
THe * syntax allows us to ignore tuple fields which we wish to ignore
'''
