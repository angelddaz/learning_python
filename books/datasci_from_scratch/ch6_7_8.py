'''
Created on Apr 1, 2017

@author: angelddaz
3-5     DONE
6-8     DONE
9-10    
11-13    
14-16    
17-19
20-22    
23-25    
'''
import math
import random

#CHAPTER 6:
def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

def normal_cdf(x, mu=0,sigma=1):    
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2 

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):    
    """find approximate inverse using binary search"""
    # if not standard, compute standard and rescale    
    if mu != 0 or sigma != 1:        
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10.0, 0            
    # normal_cdf(-10) is (very close to) 0    
    hi_z,  hi_p  =  10.0, 1            
    # normal_cdf(10)  is (very close to) 1    
    while hi_z - low_z > tolerance:        
        mid_z = (low_z + hi_z) / 2     
        # consider the midpoint        
        mid_p = normal_cdf(mid_z)      
        # and the cdf's value there        
        if mid_p < p:            
            # midpoint is still too low, search above it            
            low_z, low_p = mid_z, mid_p        
        elif mid_p > p:           
            #midpoint is still too high, search below it            
            hi_z, hi_p = mid_z, mid_p        
        else:            
            break
    return mid_z 

def bernoulli_trial(p):    
    return 1 if random.random() < p else 0

def binomial(n, p):    
    return sum(bernoulli_trial(p) for _ in range(n)) 

#There's not much here that wasn't covered in my multiple Stats/Prob courses.
#Still a good reference.

#CHAPTER 7: HYOPTHESIS AND INFERENCE

def normal_approximation_to_binomial(n, p):    
    """finds mu and sigma corresponding to a Binomial(n, p)"""    
    mu = p * n    
    sigma = math.sqrt(p * (1 - p) * n)    
    return mu, sigma

normal_probability_below = normal_cdf

def normal_probability_above(lo, mu=0, sigma=1):    
    return 1 - normal_cdf(lo, mu, sigma)

def normal_probability_between(lo, hi, mu=0, sigma=1):    
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

def normal_probability_outside(lo, hi, mu=0, sigma=1):    
    return 1 - normal_probability_between(lo, hi, mu, sigma) 

def normal_upper_bound(probability, mu=0, sigma=1):    
    """returns the z for which P(Z <= z) = probability"""    
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):    
    """returns the z for which P(Z >= z) = probability"""    
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):    
    """returns the symmetric (about the mean) bounds    
    that contain the specified probability"""    
    tail_probability = (1 - probability) / 2

#AB test
def estimated_parameters(N, n):    
    p = n / N    
    sigma = math.sqrt(p * (1 - p) / N)    
    return p, sigma 

#null hypothessis: Pa and Pb are the same
def a_b_test_statistic(N_A, n_A, N_B, n_B):    
    p_A, sigma_A = estimated_parameters(N_A, n_A)    
    p_B, sigma_B = estimated_parameters(N_B, n_B)    
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

#Chapter 8

def sum_of_squares(v):    
    """computes the sum of squared elements in v"""    
    return sum(v_i ** 2 for v_i in v) 

def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def square(x):    
    return x * x 

def derivative(x):    
    return 2 * x 

def partial_difference_quotient(f, v, i, h):    
    """compute the ith partial difference quotient of f at v"""    
    w = [v_j + (h if j == i else 0)    
         # add h to just the ith element of v         
         for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h

def estimate_gradient(f, v, h=0.00001):    
    return [partial_difference_quotient(f, v, i, h)            
            for i, _ in enumerate(v)]

def step(v, direction, step_size):    
    """move step_size in the direction from v"""    
    return [v_i + step_size * direction_i            
            for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):    
    return [2 * v_i for v_i in v]

v = [random.randint(-10,10) for i in range(3)]

def safe(f):    
    """return a new function that's the same as f,    
    except that it outputs infinity whenever f produces an error"""    
    def safe_f(*args, **kwargs):       
        try:            
            return f(*args, **kwargs)        
        except:            
            return float('inf') # this means "infinity" in Python    
    return safe_f 

def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):    
    """use gradient descent to find theta that minimizes target function"""
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    theta = theta_0             # set theta to initial value    
    target_fn = safe(target_fn) # safe version of target_fn    
    value = target_fn(theta)    # value we're minimizing
    while True:        
        gradient = gradient_fn(theta)        
        next_thetas = [step(theta, gradient, -step_size)                       
                       for step_size in step_sizes]
        # choose the one that minimizes the error function        
        next_theta = min(next_thetas, key=target_fn)        
        next_value = target_fn(next_theta)
        # stop if we're "converging"        
        if abs(value - next_value) < tolerance:            
            return theta        
        else:            
            theta, value = next_theta, next_value 


#to maximize a function, can be done by minimizing its negative
def negate(f):    
    """return a function that for any input x returns -f(x)"""    
    return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):    
    """the same when f returns a list of numbers"""    
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):    
    return minimize_batch(negate(target_fn),                          
                          negate_all(gradient_fn),                          
                          theta_0,                          
                          tolerance)

def in_random_order(data):    
    """generator that returns the elements of data in random order"""    
    indexes = [i for i, _ in enumerate(data)]  # create a list of indexes    
    random.shuffle(indexes) # shuffle them
    for i in indexes:                          
        # return the data in that order        
        yield data[i]


def vector_subtract(v, w):    
    """subtracts corresponding elements"""    
    return [v_i - w_i            
        for v_i, w_i in zip(v, w)] 

def scalar_multiply(c, v):    
    """c is a number, v is a vector"""    
    return [c * v_i for v_i in v] 

def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    data = zip(x, y)    
    theta = theta_0   # initial guess    
    alpha = alpha_0   # initial step size    
    min_theta, min_value = None, float("inf")   # the minimum so far    
    iterations_with_no_improvement = 0
    
    # if we ever go 100 iterations with no improvement, stop    
    while iterations_with_no_improvement < 100:        
        value = sum( target_fn(x_i, y_i, theta) for x_i, y_i in data )
        if value < min_value: 
            # if we've found a new minimum, remember it            
            # and go back to the original step size            
            min_theta, min_value = theta, value            
            iterations_with_no_improvement = 0            
            alpha = alpha_0        
        else: # otherwise we're not improving, so try shrinking the step size            
            iterations_with_no_improvement += 1            
            alpha *= 0.9
            # and take a gradient step for each of the data points        
            for x_i, y_i in in_random_order(data):            
                gradient_i = gradient_fn(x_i, y_i, theta)            
                theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))
    return min_theta 

def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):    
    return minimize_stochastic(negate(target_fn),                               
                               negate_all(gradient_fn),                              
                               x, y, theta_0, alpha_0)

#At this point, I really don't understand gradient descent
# I remember it from my quantitative economics class where
#it was all theory but I think taking the third calculus class this
#Fall will help a lot. As it is, multivariable calculus.

#Some more proof that I'm not a data scientist at this point
#and companies are fair to require a master's degree in STATISTICS
#or computer science. I'll get through this book because it will
#inform what I have fun with, in data analysis, but not because it will
#make me an awesome data scientist. 