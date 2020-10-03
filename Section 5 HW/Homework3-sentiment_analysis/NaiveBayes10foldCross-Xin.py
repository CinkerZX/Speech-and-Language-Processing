# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 00:39:54 2020

@author: Cinker
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:57:16 2020

@author: Cinker
"""
# Read dataset
import pandas as pd
import re # string processing
import string
import nltk
# nltk.download()
from nltk.corpus import stopwords

# Deal with abbrevation
replacement_patterns = [
(r'won\'t', 'will not'),
(r'can\'t', 'cannot'),
(r'i\'m', 'i am'),
(r'ain\'t', 'is not'),
(r'(\w+)\'ll', '\g<1> will'),
(r'(\w+)n\'t', '\g<1> not'),
(r'(\w+)\'ve', '\g<1> have'),
(r'(\w+)\'s', '\g<1> is'),
(r'(\w+)\'re', '\g<1> are'),
(r'(\w+)\'d', '\g<1> would')]


class RegexpReplacer(object):
    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]
    def replace(self, text):
        s = text
        for (pattern, repl) in self.patterns:
            (s, count) = re.subn(pattern, repl, s)
        return s

# Read the TXT documents
import numpy as np 
import os
os.getcwd()
# get positive dataset
os.chdir('/Users/Cinker/Documents/doc fist year/Course/CS124 Speech and Language Processing/Section 5 HW/Homework3-sentiment_analysis/train/pos')  
path = '/Users/Cinker/Documents/doc fist year/Course/CS124 Speech and Language Processing/Section 5 HW/Homework3-sentiment_analysis/train/pos'
#os.listdir(path)

datalist = [] # Save the name of the txt documents
for i in os.listdir(path):
    if os.path.splitext(i)[1] == '.txt':   
        datalist.append(i)

pos_data = []
for txt in datalist:
    whole_path = {path, txt}
    data_path = path+'/'+txt  
    txt_content = pd.read_csv(data_path,sep='\n', header = None)
    pos_data.append(' '.join(txt_content.iloc[:,0]))

# get negative dataset
os.chdir('/Users/Cinker/Documents/doc fist year/Course/CS124 Speech and Language Processing/Section 5 HW/Homework3-sentiment_analysis/data/train/neg')  
path = '/Users/Cinker/Documents/doc fist year/Course/CS124 Speech and Language Processing/Section 5 HW/Homework3-sentiment_analysis/data/train/neg'
#os.listdir(path)

datalist = [] # Save the name of the txt documents
for i in os.listdir(path):
    if os.path.splitext(i)[1] == '.txt':   
        datalist.append(i)

neg_data = []
for txt in datalist:
    whole_path = {path, txt}
    data_path = path+'/'+txt  
    txt_content = pd.read_csv(data_path,sep='\n', header = None)
    neg_data.append(' '.join(txt_content.iloc[:,0]))


# deal with abbrevation
# didn't like this movie, => did not NOT_like NOT_this Not_movie.
# delite the punctuation

# Training
train_aid = pd.read_csv('Train/aid.txt', header = None) # datatype: framework
train_not = pd.read_csv('Train/not.txt', header = None)
# Priors
n_aid = len(train_aid)
n_not = len(train_not)
n = n_aid + n_not
P_aid = n_aid/n
P_not = n_not/n

# Conditional prob
# text clean process
# Replace abbrevation
replacer = RegexpReplacer()
train_aid_2 = []
#.iloc locate the item by index[row, column]
for i in range(len(train_aid)):
    train_aid_2.append(replacer.replace(train_aid.iloc[i,0]))

train_not_2 = []
for i in range(len(train_not)):
    train_not_2.append(replacer.replace(train_not.iloc[i,0])) 
    

#words in aid
# the object for 'nltk.word_tokenize' need to be string, thus here merge all the documents
tokens_aid = nltk.word_tokenize(' '.join(train_aid_2))
#The frequency of words in aid
words_aid_fre = nltk.FreqDist(tokens_aid)
# delete the stop words
stop_words = stopwords.words('english')

#dict_filter = lambda Words_aid_fre, Stop_words: dict((word,Words_aid_fre[word]) for word in Words_aid_fre[word] if word not in Stop_words)
#dict_filter = lambda words_aid_fre, Stop_words: dict((k,v) for k,v in words_aid_fre.items() if k not in Stop_words)
filtered_words_aid_fre = words_aid_fre
n_aid = len(filtered_words_aid_fre)
acc_fre_aid = sum(list(filtered_words_aid_fre.values()))

#words in not
tokens_not = nltk.word_tokenize(' '.join(train_not_2))
#The frequency of words in not
words_not_fre = nltk.FreqDist(tokens_not)
# delete the stop words
filtered_words_not_fre = words_not_fre
n_not = len(filtered_words_not_fre)
acc_fre_not = sum(list(filtered_words_not_fre.values()))

n_all = n_aid + n_not


def classify(doc):
    # Deal abbrevation
    replacer = RegexpReplacer()
    doc = replacer.replace(doc)
    # Get words in doc
    tokens_doc = nltk.word_tokenize(doc)
    words_doc_fre = nltk.FreqDist(tokens_doc)
    
    # delete the stopwords
    #stop_words = stopwords.words('english')
    # dict_filter = lambda words_aid_fre, Stop_words: dict((k,v) for k,v in words_aid_fre.items() if k not in Stop_words)
    # words_doc_fre = dict_filter(words_doc_fre, stop_words)
    words_doc = list(words_doc_fre.keys())
    power = list(words_doc_fre.values())
    
    # P(doc|aid)
    P_doc_aid = P_aid
    # P(word|aid)
    for i in range(len(words_doc)):
        fre = list(dict((k,v) for k, v in filtered_words_aid_fre.items() if k == words_doc[i]).values())
        if fre == []:
            P_word_aid = 1/(acc_fre_aid+n_all)
        else:
            P_word_aid = (int(fre[0])+1)/(acc_fre_aid+n_all)
    
        P_doc_aid = P_doc_aid * pow(P_word_aid,power[i])
    
    # P(doc|not)
    P_doc_not = P_not
    # P(word|not)
    for i in range(len(words_doc)):
        fre = list(dict((k,v) for k, v in filtered_words_not_fre.items() if k == words_doc[i]).values())
        if fre == []:
            P_word_not = 1/(acc_fre_not+n_all)
        else:
            P_word_not = (int(fre[0])+1)/(acc_fre_not+n_all)
        
        P_doc_not = P_doc_not * pow(P_word_not,power[i])
    
    if P_doc_aid >= P_doc_not:
        return 1
    else:
        return 0

# This function is to evaluate the classifier
def evaluation():
    # input the development set
    dev_aid = pd.read_csv('Dev/aid.txt', header = None)
    dev_not = pd.read_csv('Dev/not.txt', header = None)
    
    # save the result in 'class_out_aid'
    T = len(dev_aid) # correct
    F = len(dev_not) # not correct
    class_out_aid_1 = []
    for i in range(T):
        class_out_aid_1.append(classify(dev_aid.iloc[i,0]))
    
    class_out_aid_2 = []
    for i in range(F):
        class_out_aid_2.append(classify(dev_not.iloc[i,0]))
    
    # evaluation
    # Precision
    tp = sum(class_out_aid_1) # true positive
    #fn = T-tp # false negative
    fp = sum(class_out_aid_2) # false positive
    # tn = F-fp # true negative
    
    Precision = tp/(tp+fp)
    Recall = tp/T
    
    print('Precision', Precision, sep = ': ')
    print('Recall', Recall, sep = ': ')
    
    F =  2*Precision*Recall/(Precision+Recall)
    print('F value', F, sep = ': ')