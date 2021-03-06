'''
Created on Apr 7, 2017

@author: angel
3-5     DONE
6-8     DONE
9-10    
11-13    
14-16    
17-19
20-22    
23-25
'''

#The | is the pipe character, which means �use the output of the left 
#command as the input of the right command.� 
#You can build pretty elaborate data-processing pipelines this way
import math
# 'r' means read-only 
file_for_reading = open('reading_file.txt', 'r')
# 'w' is write -- will destroy the file if it already exists! 
file_for_writing = open('writing_file.txt', 'w')
# 'a' is append -- for adding to the end of the file 
file_for_appending = open('appending_file.txt', 'a')
# don't forget to close your files when you're done 
file_for_writing.close()

from bs4 import BeautifulSoup
import requests
html = requests.get("http://www.example.com").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')

first_paragraph_text = soup.p.text

from collections import defaultdict, Counter
#chapter 10
def bucketsize(point, bucket_size):
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
    return Counter(bucketsize(point, bucket_size) for point in points)

import matplotlib.pyplot as plt
def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()
import random

random.seed(0)

uniform = [200 * random.random() - 100 for _ in range(10000)]

#normal = [57 * inverse_normal_cdf(random.random()) for _ in range(10000)]
