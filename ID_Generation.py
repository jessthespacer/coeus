#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 23:03:47 2020

@author: kaitlyn
"""

"""
Goal: Create a random number generator that will allow countries, languages,
people, research area, tag, and subject

Subject: > (3 digits)

Countries: >> (5 digits)

Languages: >> (4 digits)

People: >>> (10 digits)

Research Area: >> (8 digits)

Tags: >>> (9 digits)

1. Import csv file
2. Create struct (element, element ID)
3. 
2. Check if it is valid (must be a word) and it is filled
        --- if blank, next blank
3. Go through rows for the 6 areas
4. Use unique function to create values in new array
5. Go through each element and randomize an ID number
6. Create new list that has class
7. Insert lists back into csv file.

Return value: file called "sample1.csv" that will have new ID columns 
"""

import random
#import re

class Element:
    pass

#create list 
def Create_List(total_entries, col_num, temp_table):
    lst = []
    for x in range(1,total_entries):
        lst.append(temp_table[col_num][x])
    return lst

def Uniqueness_Key(ID_length, array):
    
    key = []
    
    for i in range(len(array)):
        array[i] = array[i].lower()
    
    #unique values algorithm
    tmp = list(set(array))
    
    #create Element class list
    for i in range(len(tmp)):
        if tmp[i] != 'NA':
            obj = Element()
            obj.element = tmp[i]
            obj.ID = random.randint(10**(ID_length-1), 10**(ID_length))
            key.append(obj) 
        else:
            obj = Element()
            obj.element = tmp[i]
            obj.ID = "NA"
          
    return key;

def New_Array(key, lst):
    array=[]
    for i in range(len(lst)):
        for j in range(len(key)):
            if(lst[i]==key[j].element):
                array.append(key[j].ID)
    return array

def ID_Assignment(total_entries, col_num, temp_table, ID_len):
    lst = Create_List(total_entries, col_num, temp_table)
    key = Uniqueness_Key(ID_len, lst)
    ids = New_Array(key, lst)
    return lst, ids

def People_ID(total_entries, ID_length, col_num, temp_table):
    lst=[]
    ids = []
    for i in range(1, total_entries):
        ids.append(random.randint(10**(ID_length-1), 10**(ID_length)))
        lst.append(temp_table[col_num][i])
    return lst, ids
    
