#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:45:34 2020

@author: kaitlyn
"""

'''
Tags

Create tag IDs for the persontag category
1. Create class w person, tag, and person-tag ID
2. Create table w just the tags and people
3. Separate out the tags, and fill in a table just w classes
4. Create Excel spreadsheet w that
'''
import string
import numpy as np
import random
import pandas as pd

class PT:
    pass

class Element:
    pass

from ID_Generation import Create_List
from ID_Generation import Uniqueness_Key
from ID_Generation import New_Array

def New_Array_Tag(tag_key, RA_T):
    RA_array=[]
    Tag_array =[]
    TagID_array =[]
    for i in range(len(tag_key)):
        for j in range(len(RA_T)):
            if(tag_key[i].element==RA_T[j].T):
                TagID_array.append(tag_key[i].ID)
                Tag_array.append(tag_key[i].element)
                RA_array.append(RA_T[j].R)
    return RA_array, Tag_array, TagID_array
    

#create table that will take out tags and people
def ppl_tag(total_entries, col_p, col_t, ra_ID, temp_table, ppl, ppl_ID):
    people = Create_List(total_entries, col_p, temp_table)
    tags = Create_List(total_entries, col_t, temp_table)
    
    #separate all tags
    for i in range(len(tags)):
        a = tags[i]
        tags[i] = a.split(",")
        
    #create one list w no distinction
    T = []
    P=[]
    RA_T = []
    for i in range(len(tags)):
        for j in range(len(tags[i])):
            T.append(tags[i][j])  
            P.append(people[i])
            
            obj = PT()
            obj.T = tags[i][j]
            obj.R = ra_ID[i]
            RA_T.append(obj)
            
    #make unique tag key
    tag_key = Uniqueness_Key(8, T)
    
    #array of tag IDs we want
    T_ID = New_Array(tag_key, T)
    print(T_ID)
    
    #get the people column sorted
    P_ID = []
    
    for i in range(len(P)):
        for j in range(len(ppl)):
            if(ppl[j] == P[i]):
                P_ID.append(ppl_ID[j])           
    print(P_ID) 
    
    PT_ID=[]
    for i in range(len(T_ID)):
          PT_ID.append(random.randint(10**(7), 10**(8)))  
    
    
    pt_tbl = {'ID': PT_ID,
              'Tag ID': T_ID,
              'Person ID': P_ID
            }
    df4 = pd.DataFrame(pt_tbl, columns= ['ID','Tag ID', 'Person ID'])
    df4.to_csv (r'/home/kaitlyn/Documents/hackathon/pt_tbl.csv', index = False, header=True)
    
    RA_array, Tag_array, TagID_array = New_Array_Tag(tag_key, RA_T)
    
    pt_tag = {'Tag': Tag_array,
              'Tag ID': TagID_array,
              'Research Area ID': RA_array
            }
    df4 = pd.DataFrame(pt_tag, columns= ['Tag','Tag ID', 'Research Area ID'])
    df4.to_csv (r'/home/kaitlyn/Documents/hackathon/tag_tbl.csv', index = False, header=True)
    
    return tag_key


    
                
    
    
      
    
    
    
