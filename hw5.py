
# coding: utf-8

# In[1]:


import csv    
import json
import pickle

from collections import Counter 


def main(filename):
    file=open(filename)
    lines = file.readlines()
    
    all_words = []
    for line in lines:
        words=line.split()
        for word in words:
            import string 
            new_word=word.strip(string.punctuation)
            if new_word:
                all_words.append(new_word)
    
    counter = Counter(all_words)
   
    with open("wordcount.csv","w",newline='') as csvfile:          
        writer = csv.writer(csvfile)
        writer.writerow(['word', 'count'])
        for i in set(all_words):
            writer.writerow([i,all_words.count(i)])
            
    with open("wordcount.json","w")as jsonfile:
        json.dump(counter,jsonfile)
        
    with open ("wordcount.pkl","wb") as pklfile:
        pickle.dump(counter,pklfile)
    
if __name__ == '__main__': 
    main("i_have_a_dream.txt")

