# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 12:12:53 2018

@author: logesh
"""
#import statements
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import unicodedata
from pattern.en import suggest
import contractions
pattern = re.compile(r"(.)\1{2,}")
tokenizer = nltk.TweetTokenizer(strip_handles=True)
stopword_list = nltk.corpus.stopwords.words('english')
#url and hyperlinks removal
def remove_url(doc):
    doc = re.sub(r'https?:\/\/.*[\r\n]*','',doc)
    doc = doc.lower()
    return doc
        
#remove special characters
def remove_special_characters(text):
    text = re.sub('[^a-zA-z\s]', '', text)
    return text

#tokenization
def tokenize_text(doc):
    tokens=tokenizer.tokenize(doc)
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    return(" ".join(filtered_tokens))   

#Remove additional characters    
def reduce_lengthening(text):
    return pattern.sub(r"\1\1", text)
        
#remove accented characters
def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text
  
#lemmentization
def lemmetize(text):
    lem = WordNetLemmatizer()
    tokens = text.split(" ")
    list1 = [lem.lemmatize(token,pos='v') for token in tokens]
    return(" ".join(list1))
   
#Replace contractions in string of text    
def replace_contractions(text):
    return(contractions.fix(text)) 

    


def normalize(sentences):
    count=0
    nor_sentences = []
    for doc in sentences:
        doc = remove_url(doc)
        doc = replace_contractions(doc)
        doc = tokenize_text(doc)
        doc = remove_special_characters(doc)
        doc = remove_accented_chars(doc)
        doc = reduce_lengthening(doc)
        doc = lemmetize(doc)
        doc = re.sub(' +', ' ', doc)
        nor_sentences.append(doc)
        count = count+1
        print(count) 
    return(nor_sentences)    
        
        