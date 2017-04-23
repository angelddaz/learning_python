'''
Created on Mar 31, 2017

@author: angelddaz
3-5     DONE
6-8
9-10
11-13
14-16
17-19
20-22
23-25
'''

from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"] 
num_oscars = [5, 11, 3, 8, 10]

#interesting way of making sure each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]
plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-', label='bias^2')
plt.plot(xs, total_error, 'b:', label='total error')
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()
#to equalize axes:
#plt.axis("equal")

#CHAPTER 4: LINEAR ALGEBRA

#vector addition. Making functions
def vector_add(v, w):    
        """adds corresponding elements"""    
        return [v_i + w_i            
            for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):    
        """subtracts corresponding elements"""    
        return [v_i - w_i            
            for v_i, w_i in zip(v, w)] 

def vector_sum(vectors):    
    return reduce(vector_add, vectors) 

def scalar_multiply(c, v):    
    """c is a number, v is a vector"""    
    return [c * v_i for v_i in v] 

def vector_mean(vectors):    
    """compute the vector whose ith element is the mean of the    
    ith elements of the input vectors"""    
    n = len(vectors)    
    return scalar_multiply(1/n, vector_sum(vectors)) 

def dot(v, w):    
    """v_1 * w_1 + ... + v_n * w_n"""    
    return sum(v_i * w_i               
               for v_i, w_i in zip(v, w))

def sum_of_squares(v):    
    """v_1 * v_1 + ... + v_n * v_n"""    
    return dot(v, v) 

import math

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):    
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""    
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):    
    return magnitude(vector_subtract(v, w)) 

#functions for matrices
def shape(A):    
    num_rows = len(A)    
    num_cols = len(A[0]) if A else 0  
    # number of elements in first row    
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j]
            for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]

def is_diagonal(i, j):
    return 1 if i ==j else 0
#All of these functions are included in numpy but it's good to see the guts

'''CHAPTER 5'''
#Chapter 5: statistics
from __future__ import division

def mean(x):    
    return sum(x) / len(x)


def de_mean(x):    
    """translate x by subtracting its mean (so the result has mean 0)"""    
    x_bar = mean(x)    
    return [x_i - x_bar for x_i in x]


def variance(x):    
    """assumes x has at least two elements"""    
    n = len(x)    
    deviations = de_mean(x)    
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):    
    return math.sqrt(variance(x))

def covariance(x, y):    
    n = len(x)    
    return dot(de_mean(x), de_mean(y)) / (n - 1)
'''a “large” positive covariance means 
that x tends to be large when y is large and small when y is small. '''

def correlation(x, y):    
    stdev_x = standard_deviation(x)    
    stdev_y = standard_deviation(y)    
    if stdev_x > 0 and stdev_y > 0:        
        return covariance(x, y) / stdev_x / stdev_y    
    else:        
        return 0    # if no variation, correlation is zero