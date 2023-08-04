#!/usr/bin/env python
# coding: utf-8

# In[3]:


sen=input("Enter a sentence:")
wordlist=sen.split(" ")
print("This sentences has",len(wordlist),"words")
digcnt=upcnt=locnt=0
for ch in sen:
    if '0'<=ch<='9':
        digcnt+=1
    elif 'A'<=ch<='Z':
        upcnt+=1
    elif 'a'<=ch<='z':
        locnt+=1
print("The sentence has",digcnt,"digits",upcnt,"upper case letters",locnt,"lower case letters")


# In[4]:


str1=input("Enter string 1\n")
str2=input("Enter string 2\n")
if len(str2)<len(str1):
    short=len(str2)
    long=len(str1)
else:
    short=len(str1)
    long=len(str2)
matchcnt=0
for i in range(short):
    if str1[i]==str2[i]:
        matchcnt+=1
print("Similarity between two said strings:")
print(matchcnt/long)


# In[ ]:




