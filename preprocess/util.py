#-*- coding:utf-8 -*-
# AUTHOR:   fuzx
# FILE:     util.py
# ROLE:     TODO (some explanation)
# CREATED:  2017-09-23 17:02:34
# MODIFIED: 2017-09-23 17:02:38


import nltk
from nltk.tokenize import RegexpTokenizer
import random
    

def get_noun(sentence):
    if not sentence:
        raise ValueError, "Empty sentence for get_noun()"
    is_noun = lambda pos: pos[:2] == 'NN'
    # delete punctuation
    tokenizer = RegexpTokenizer(r'\w+')
    tokenized =  tokenizer.tokenize(sentence)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
    if len(nouns) > 0:
        return random.choice(nouns)
    return random.choice(tokenized)
    
if __name__ == "__main__":
    print(get_noun("I am a Chinses!"))