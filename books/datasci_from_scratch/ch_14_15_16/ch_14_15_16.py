'''
Created on Apr 23, 2017

@author: angel
3-5      DONE
6-8      DONE
9-10     DONE
11-13    DONE
14-16    easiest
17-19    HARD
20-22    HARDEST
23-25    EASIESTEST
'''
from __future__ import division
from books.datasci_from_scratch.ch_6_7_8.ch6_7_8 import minimize_stochastic

#Chapter 14: Simple Linear Regression

'''def predict(alpha, beta, x_i):
    return beta * x_i + alpha

def error(alpha, beta, x_i, y_i):
    return y_i - predict(alpha, beta, x_i)'''

def dot(v, w):    
    """v_1 * w_1 + ... + v_n * w_n"""    
    return sum(v_i * w_i               
               for v_i, w_i in zip(v, w))

def sum_of_squares(v):    
    """v_1 * v_1 + ... + v_n * v_n"""    
    return dot(v, v) 

from __future__ import division

def mean(x):    
    return sum(x) / len(x)


def de_mean(x):    
    """translate x by subtracting its mean (so the result has mean 0)"""    
    x_bar = mean(x)    
    return [x_i - x_bar for x_i in x]


def sum_of_squared_errors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y))

def variance(x):    
    """assumes x has at least two elements"""    
    n = len(x)    
    deviations = de_mean(x)    
    return sum_of_squares(deviations) / (n - 1)

import math

def standard_deviation(x):    
    return math.sqrt(variance(x))

def covariance(x, y):    
    n = len(x)    
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):    
    stdev_x = standard_deviation(x)    
    stdev_y = standard_deviation(y)    
    if stdev_x > 0 and stdev_y > 0:        
        return covariance(x, y) / stdev_x / stdev_y    
    else:        
        return 0    # if no variation, correlation is zero

def least_squares_fit(x, y):
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta

def total_sum_of_squares(y):
    return sum(v ** 2 for v in de_mean(y))

def r_squared(alpha, beta, x, y):
    return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) / 
                  total_sum_of_squares(y))

#commented out so that methods are not repeated in chapter 15
'''def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2

def squared_error_gradient(x_i, y_i, theta):
    alpha, beta = theta
    return [-2 * error(alpha, beta, x_i, y_i), #alpha partial derivative
            -2 * error(alpha, beta, x_i, y_i) * x_i] #beta partial derivative'''

#chapter 15 MULTIPLE REGRESSION



def predict(x_i, beta):
    return dot(x_i, beta)

def error(x_i, y_i, beta):
    return y_i - predict(x_i, beta)

def squared_error(x_i, y_i, beta):
    return error(x_i, y_i, beta) ** 2

def squared_error_gradient(x_i, y_i, beta):
    return [-2 * x_ij * error(x_i, y_i, beta)
            for x_ij in x_i]

def multiple_r_squared(x, y, beta):
    sum_of_squared_errors = sum(error(x_i, y_i, beta) ** 2
                                for x_i, y_i in zip(x, y))
    return 1.0 - sum_of_squared_errors / total_sum_of_squares(y)

#the bootstrap
import random

def bootstrap_sample(data):
    return [random.choice(data) for _ in data]

def bootstrap_statistic(data, stats_fn, num_samples):
    return [stats_fn(bootstrap_sample(data))
            for _ in range(num_samples)]

close_to_100 = [9.5 + random.random() for _ in range(101)]
far_from_100 = ([99.5 + random.random()] +
                [random.random() for _ in range(50)] +
                [200 + random.random() for _ in range(50)])

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi] / 2)

bootstrap_statistic(close_to_100, median, 100)
bootstrap_statistic(far_from_100, median, 100)

#chapter 16 LOGISTIC REGRESSION

def logistic(x):
    return 1.0 / (1 + math.exp(-x))

def logistic_prime(x):
    return logistic(x) * (1 - logistic(x))

def logistic_log_likelihood_i(x_i, y_i, beta):
    if y_i == 1:
        return math.log(logistic(dot(x_i, beta)))
    else:
        return math.log(1 - logistic(dot(x_i, beta)))

def logistic_log_likelihood(x, y, beta):
    return sum(logistic_log_likelihood_i(x_i, y_i, beta)
               for x_i, y_i in zip(x, y))

def logistic_log_partial_ij(x_i, y_i, beta, j):
    return (y_i - logistic(dot(x_i, beta))) * x_i[j]

def logistic_log_gradient_i(x_i, y_i, beta):
    return [logistic_log_partial_ij(x_i, y_i, beta, j)
            for j, _ in enumerate(beta)]

def vector_add(v, w):    
        """adds corresponding elements"""    
        return [v_i + w_i            
            for v_i, w_i in zip(v, w)]


def logistic_log_gradient(x, y, beta):
    return reduce(vector_add,
                  [logistic_log_gradient_i(x_i, y_i, beta)
                   for x_i, y_i in zip(x, y)])

