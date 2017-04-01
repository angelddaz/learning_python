'''
Created on Jan 29, 2017

@author: angelddaz
'''

#Implementation:
#creating a spam filter with Naive Bayes
#Convert to lowercase, extracting words, and removing duplicates

def tokenize(message):
    message = message.lower()
    all_words = re.findall("[a-z0-9']+", message)
    return set(all_words)
    
def count_words(training_set):
    """training set consists of pairs (message, is_spam)"""
    counts = defaultdict(lambda: [0,0])
    