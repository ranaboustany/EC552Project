#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ranaboustany
"""

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

def main():
    #Inport libraries
    import pandas as pd

    #set up database of bacteria sequences as db as pandas dataframe df
    db_df = pd.read_csv("bacteria_db_test.csv")

    # read the protein sequences file into pandas dataframe
    seq_df = pd.read_csv("protein_seq_test.csv")
    
    for i in seq_df.index: # i indexes possible protein sequences
        for j in db_df.index: # j indexes bacteria database 
            s1 = seq_df['sequence'][i]
            s1_ID = seq_df['ID'][i]
            s2 = db_df['sequence'][j]
            s2_ID = db_df['ID'][j]
            mm = compareSeqs(s1,s2)
            print("Protein", s1_ID, "sequence: ", s1, "and \nBacteria", s2_ID, "sequence:", s2, "\nhave", mm, "mismatches\n")
    
    
    
if __name__ == "__main__":
    main()
        
        
        
    