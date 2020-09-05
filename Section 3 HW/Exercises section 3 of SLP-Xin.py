# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:21:43 2020

@author: Cinker
"""

# 3.8 Write a program to compute unsmoothed unigrams and bigrams.

import re # string processing
# n: regulate the order of the gram
# aim_string the string that you want to estimate
def n_gram(corpora, n, aim_string):
    # split the corpora by '.' ****Escape character is needed*****
    lines = re.split('\.|\. |\? |\? |\,', corpora)
    lines = list(filter(None, lines))
    pro_str = []
    pro_str.append((aim_string,pro(lines,aim_string,n)))
    return pro_str

def pro(words, aim_string, n):
    p = 1
    str_list = aim_string.split()
    k = len(str_list) # the aim-string has k words
    for i in range(k-n+1): #windows needs to move k-n+1 times
        #if k == 2:
        #    p = p*words.count(str_list[n-1+i])/words.count(" ".join(str_list[0:1]))
        #else:
        count_1 = 0
        count_2 = 0
        # calculate the frequency of the aimed string; depends on the regulated n
        for j in range(len(words)): # check the aim-string in each lines
            if n+i == i+1: # if unigram 要改
                words_single = words[j].split()
                count_1 = count_1 + words_single.count(" ".join(str_list[i:n+i]))
            else:
                count_1 = count_1 + words[j].count(" ".join(str_list[i:n+i]))
            if n == 2: # if 2-gram
                words_single = words[j].split()
                count_2 = count_2 + words_single.count(" ".join(str_list[i:n+i-1]))
            else:
                count_2 = count_2 + words[j].count(" ".join(str_list[i:n+i-1]))
        # print(" ".join(str_list[i:n+i]))
        # print("count_1",count_1)
        # print("count_2",count_2)
        if count_2 == 0 or count_1 == 0:
            p = 0;
        else:
            p = p*count_1/count_2
        #k = k - 1
    return p

n_gram('I am Sam. Sam I am. I do not like Sam', 2 , "am Sam")
n_gram('I am Sam. Sam I am. I do not like Sam', 2 , "I am")
n_gram('I am Sam. Sam I am. I do not like Sam', 2 , "I am Sam")

n_gram('I am Sam. Sam I am. I do not like Sam', 3 , "I am Sam")
n_gram("you got one eventually. yeah, should be good for the start. sure, feeling ok. hahaha, clever. Awesome, great you are learning to swim. Doing.okay. work is going good. Also I do the beekeping stuff at the free time. Runa mountain run i told you about. Went pretty good. Cool. During what. What kind of running. So the first 20 was a warmup. Then it\'s not a warmup. The profile of your run looks like you pushed yourself too much. Besides if the subsequent repotitions of the faster run were with a lower he than the 1st one, it tells me you pushed too much. And you were too tired to repeat with a good speed. I see. Perfect. And don't go over 155. If it's higher you should slow down. This is to be done during things like competition or preparation just before the competition. If you push like that during normal training days you will get overtrained. Besides I told you one day, I recommend you get a running watch. Yes I get a running watch. + hr chest sensors. Then you should consult it more often ;). What kind of watch did you buy. Ok, not familiar with Huawei offer of sport watxhes. Sounds more like a smart watch. Then it should be good. So you have a sensor? What sensor. Chest sensor. For hr. Does it have the option to use a chest sensor too? The wrist sensors are nice for everyday use but indeed not accurate for sport. I bet they make Garmin in.china too. Thats a pitty. I have Garmin fr245. It\'s not perfect but so far it\'s fine. You buy the one supported by your watch. There is usually only one. Good. Cool. Wow, great. Afaik it\'s present in most smartwatches. Cool instrument. Why? Yes, i did. How did you see Gleb git it? *got. Ok. what? nice. crayons? whats the difference? ok, got it. #awesome. ok, will do. Think that the best guys run a marathon with this pace. Kick her ass. You know what you need to.do. Something like that. Hopefully I find sth in my collection. So far these slides are hmmm. Not even mentioning Gleb. I don\'t get what kind of kindness so you see there. That\'s it. Aha. Where will he work? Ok. That\'s normal. While he did not actually get a job. I think Paola or fees will recommend whenever he needs to etc. *Cees. Not sure where are your assumptions coming from. So? I see, fair enough. Cool, hopefully she gets sth. No bicep here. Looks more like your arm. #yes. I don\'t have this sort of dillemas. What happened. Then text her, once she calms.down it should be fine. Then calm down, let the time pass. She will be fine. What choice. I see.", 2, 'If you')

# 3.10 Add an option to your program to generate random sentences.
import string
import nltk
# nltk.download()
from nltk.corpus import stopwords
from itertools import combinations
import numpy as np # generate random int



# n: regulate the order of the gram
# aim_string the string that you want to estimate
# n_sen is the number of words in the sentence, n_sen > n
def n_gram_2(corpora, n, n_sen):
    # change into lower case
    corpora = corpora.lower()
    
    # split the corpora by '.' ****Escape character is needed*****
    lines = re.split('\.|\. |\? |\? |\, |\;', corpora)
    lines = list(filter(None, lines))
    pro_str = []
    nwords = []
    generate_sentence = ""
        
    # Remove all the punctuations
    remove = str.maketrans('','',string.punctuation)
    without_punctuation = corpora.translate(remove)
    # get all the words
    tokens = nltk.word_tokenize(without_punctuation)
    all_words = set(tokens) #delete the repeating words
    stop_words = stopwords.words('english')
    words_fre = nltk.FreqDist([x for x in all_words if x not in stop_words]) # check the frequency of words
    
    # get words out of the corpora with the wide of the window of n words
    all_lines = " ".join(lines) # combine all lines
    words_in_lines = all_lines.split()
    k = len(words_in_lines)
    for i in range(k-n+1):
        nwords.append(" ".join(words_in_lines[i:i+n]))
    # delete the repeat
    nwords = list(set(nwords))
    for i in range(len(nwords)):
        pro_str.append((nwords[i],pro(lines,nwords[i],n)))
    
    # pro_str.sort(key=takeSecond, reverse =True)
    order_str = sorted(pro_str, key=takeSecond, reverse =True)
    # save the splited phrases into "corups_order"
    corups_order = [x[0].split() for x in order_str if x[1] > 0]
    generate_sentence = order_str[0][0]
    
    # need to add n_sen-n words
    for i in range(n_sen - n):
        last_words = nltk.word_tokenize(generate_sentence)
        last_words = last_words[-(n-1):]
        if n == 2:
            # last_words = last_words[-1]; s[0] is string, but "last_words" is list, so we need to change the format of last_words
            matching = [s for s in corups_order if ''.join(last_words) == s[0]]
        else:
            # last_words = last_words[-(n-1):len(last_words)]
            # matching with the front n-1 words
            matching = [s for s in corups_order if last_words == s[:(n-1)]]
        # if there is no match in the corups_order, then add the most frequent word
        if matching == []:
            r = np.random.randint(1,int(len(words_fre)/3)) # random int
            generate_sentence = generate_sentence + ' ' + words_fre.most_common(r)[r-1][0]
        else:
        # else add the last word in the matching list
            generate_sentence = generate_sentence + ' ' + matching[0][-1]
            
    return generate_sentence
    
def takeSecond(elem):
    return elem[1]

# test:
corpora = "Phase 3 trials can confirm whether the vaccine actually prevents illness with Covid-19. The data on the Russian vaccine studies reported in The Lancet are encouraging, said Brendan Wren, professor of microbial pathogenesis, London School of Hygiene and Tropical Medicine. In the study, half of the participants developed fevers and 42% developed headaches. In addition, about 28% experienced weakness and 24% had joint pain. The article did not say how long these side effects lasted but said most adverse events were mild. The vaccine was registered in Russia in August, before it had gone through large-scale trials. The researchers at the Gamaleya National Research Centre for Epidemiology and Microbiology in Russia received approval on August 26 to do a Phase 3 trial, which is expected to have 40,000 volunteers, according to a press release from The Lancet. The researchers are already distributing the vaccine to high-risk groups, according to Kirill Dmitriev, head of the Russian Direct Investment Fund (RDIF), which is financing Russian vaccine research. Gamaleya is using adenoviruses in their Covid-19 vaccines; this is the same approach used in the vaccine developed by the University of Oxford and AstraZeneca. The adenovirus delivers genetic material for the spike protein that sits atop the virus that causes Covid-19, and that genetic material is designed to generate an immune response to the virus."
n = 3
n_sen = 10
n_gram_2(corpora, n, n_sen)

n = 2
n_sen = 15
n_gram_2(corpora, n, n_sen)

n = 4
n_sen = 10
n_gram_2(corpora, n, n_sen)

n = 3
n_sen = 20
n_gram_2(corpora, n, n_sen)
n = 3
n_sen = 20
n_gram_2(corpora, n, n_sen)
    
    
    
    
    
      