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

def bacteriaRecommendation(report):
    """Takes in report as pandas dataframe and prints out recommendation = bacteria/bacterium with minimal mutations needed"""
    # # find index of minimum mutation
    # i_min = report[['mutations']].idxmin()
    # bac = report['bacteria'][i_min]
    # bac_seq = report['bacteriaSequence'][i_min]
    # pro_seq = report['proteinSequence'][i_min]
    # print("Recommended bacteria:")
    
    # find smallest number of mutation
    min_mutation = report['mutations'].min()
    i_list = [] # keep track on indices of min mutations just in case
    for i in report.index:
        if report['mutations'][i] == min_mutation:
            i_list += [i]

    print("Recommendation:")
    for j in i_list:
        print(report['bacteriaID'][j])
        
def detailedReport(bac, report):
    """Takes in report as pandas dataframe and bacteria name and creates a new "detailed" report for that bacteria: describing changes that should be made to bacterial sequence"""
    report_df = report.set_index('bacteriaID')
    bac_seq = report_df['bacteriaSequence'][bac]
    pro_seq = report_df['proteinSequence'][bac]
    l_b = len(bac_seq)
    l_p = len(pro_seq)
    if l_b != l_p: 
    # call helper function that adds to end of short sequence
        if l_b > l_p:
            shortSeq = pro_seq
            gapL = l_b - l_p
            shortSeq = makeLonger(pro_seq,gapL)
            pro_seq = shortSeq
        else:
            shortSeq = bac_seq
            gapL = l_p - l_b
            shortSeq = makeLonger(bac_seq,gapL)
            bac_seq = shortSeq
    print(bac_seq)
    print(pro_seq)
    if len(bac_seq) != len(pro_seq):
        print("something is wrong")
    
    lines = ["protein:  "+ pro_seq, "bacteria: " + bac_seq, "\nMutations:"] #store data in lest to then use in text file
    for i in range(len(bac_seq)): # lengths are now equal so pick one
        if bac_seq[i] != pro_seq[i]:
            if bac_seq[i] == '-':
                mut = ["Add " + pro_seq[i] + " at position "+ str(i)]
            elif pro_seq[i] == '-':
                mut = ["Remove " + bac_seq[i] + " at position "+ str(i)]
            else:
                mut = ["Change " + bac_seq[i] + " to "+ pro_seq[i] + " at position "+ str(i)]
            lines += mut
    print(lines)
    
    with open('detailed_report.txt', 'w') as f:
        f.write('\n'.join(lines))
    
    

def main():
    #Inport libraries
    import pandas as pd

    #set up database of bacteria sequences as db as pandas dataframe df
    db_df = pd.read_csv("bacteria_db_test.csv")

    # read the protein sequences file into pandas dataframe
    seq_df = pd.read_csv("protein_seq_test.csv")
    
    
    #Create empty dataframe to save data and later create report
    report_df = pd.DataFrame(columns=['bacteriaID', 'bacteriaSequence', 'proteinSequence', 'mutations'], index=range(len(db_df)))
    # initialize protein sequence with minimal mismatches to first one 
    chosen_pro = seq_df['sequence'][0]
    mm_min = 1000000000000000000000 # place holder for now, really big number, change to 1st comparison later!
    for i in db_df.index: # i indexes bacteria database 
        for j in seq_df.index: # j indexes possible protein sequences
            bac_seq = db_df['sequence'][i]
            bac_ID = db_df['ID'][i]
            pro_seq = seq_df['sequence'][j]
            mm = compareSeqs(bac_seq, pro_seq)
            if mm < mm_min:
                mm_min = mm # samallest number of mismatches 
                chosen_pro = pro_seq # saves protein sequence that would require minimal number of mutations
        # add data to report
        report_df.loc[i] = [bac_ID, bac_seq, chosen_pro, mm_min]
        
    print(report_df)
    # save report dataframe to csv file in working directory
    report_df.to_csv('report.csv', index=False)
    
    bacteriaRecommendation(report_df)
    
    bacA = input("Please enter bacteria ID: ")
    
    detailedReport(bacA, report_df)
        
            
    
if __name__ == "__main__":
    main()
        
        
        
    