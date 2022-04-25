#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 19:58:28 2022

@author: ranaboustany
"""

#Inport libraries
import pandas as pd

#set up database of bacteria sequences as db
db = pd.DataFrame()

def makeLonger(s,l):
    """makes a sequence s longer by adding dashes to trailing space"""
    for gap in range(l):
        s = s + '-'
    return s


def compareSeqs(s1,s2):
    """Takes in 2 nucleotide sequences (strings) and returns number of differences (base pairs that  don't match)"""
    # check if sequences have the same length. If not, make shorter sequence longer by filling trailing gap
    l1 = len(s1)
    l2 = len(s2)
    
    if l1 != l2: 
    # call helper function that adds to end of short sequence
        if l1 > l2:
            shortSeq = s2
            gapL = l1 - l2
            shortSeq = makeLonger(s2,gapL)
            s2 = shortSeq
        else:
            shortSeq = s1
            gapL = l2 - l1
            shortSeq = makeLonger(s1,gapL)
            s1 = shortSeq
        print("sequences have different lengths")
    
    #convert both string sequences to uppercase letters
    s1 = s1.upper()
    s2 = s2.upper()
    
    mismatch = 0 # counts mismatches of base pairs
    for i in range(l1): #assuming l1 = l2
        if s1[i] != s2[i]:
            mismatch += 1
    
    return mismatch
        
        
        
    