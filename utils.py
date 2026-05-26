#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 19:01:38 2022

@author: pmat
"""

from functools import reduce
import random

# samples the indices of w using the weights of w
# if x=1 the probability is linearly proportional 
# if x=-1 it is inversely proportional
# if x=0 it becomes uniform
# One might use other values of x to stress de differences
# for x>1 it will give more probability than the linear proportion
def sample(w,x):
    nw=list(map((lambda y:y**x),w))
    sum=reduce((lambda x,y:x+y),nw,0)
    nw=list(map((lambda y:y/sum),nw))
    for i in range(1,len(nw)):
        nw[i]=nw[i-1]+nw[i]
    r=random.random()
    #print(nw)
    #print(r)
    i=0
    b=True
    while(i<len(nw) and b):
        if(r<nw[i]):
            s=i
            b=False
        i+=1
    return s



# generates a random DNA string of size n and at least c fragments
# with random size [dmin,dmax] until covering all original DNA string
# it prints the DNA string
# to simplify the code, it does not abstract from the implementation
def generate(n,c,dmin,dmax):
    r=[]
    for i in range(n):
        r+=[random.randint(0,3)]
    w=[]
    print(r) # original DNA string
    cov=[]
    for i in range(n):
        cov+=[False]
    for i in range(c):
        pos=random.randint(0,n-dmin-1)
        dim=random.randint(dmin,dmax)
        w+=[r[pos:min(pos+dim,n)]]
        for j in range(pos,min(pos+dim,n)):
            cov[j]=True
    while not all(cov):
        pos=random.randint(0,n-dmin-1)
        dim=random.randint(dmin,dmax)
        w+=[r[pos:min(pos+dim,n)]]
        for j in range(pos,min(pos+dim,n)):
            cov[j]=True
    return w