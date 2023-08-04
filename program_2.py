#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fn(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fn(n-1)+fn(n-2)
num=int(input("enter a number:"))
if num>0:
    print("fn(",num,")=",fn(num),sep="")
else:
    print("error in input")


# In[3]:


def bin2dec(val):
    rev=val[::-1]
    dec=0
    i=0
    for dig in rev:
        dec+=int(dig)*2**i
        i+=1
    return dec

def oct2hex(val):
    rev=val[::-1]
    dec=0
    i=0
    for dig in rev:
        dec+=int(dig)*8**i
        i+=1
    list=[]
    while dec!=0:
        list.append(dec%16)
        dec=dec//16
    n1=[]
    for ele in list[::-1]:
            if ele<=9:
                  n1.append(str(ele))
            else:
                n1.append(chr(ord('A')+(ele-10)))
                hex="".join(n1)
    return hex

num1=input("Enter a binary number:")
print(bin2dec(num1))
num2=input("Enter an octal number:")
print(oct2hex(num2))


# In[ ]:




