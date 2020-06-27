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

Return value: classes 
"""

import numpy as np
import csv
import os
import base64
#import re

class Element:
  pass


#create list 
def Create_List(total_entries, row_number, temp_table):
    lst = []
    for x in range(1,total_entries):

        # see if it is a word (valid)
        if(any(map(str.isdigit, temp_table[row_number][x])) == False):

            lst.append(temp_table[row_number][x])
        else:
            lst.append('NA')
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
            obj.ID = base64.b64encode(os.urandom(ID_length)).decode('ascii')
            key.append(obj) 
        else:
            obj = Element()
            obj.element = tmp[i]
            obj.ID = "NA"
          
    return key;

def New_Array(key, lst):
    for i in range(len(lst)):
        for j in range(len(key)):
            if(lst[i]==key[j].element):
                lst[i]=key[j]
    return lst  

def ID_Assignment(total_entries, col_num, temp_table, ID_len):
    lst = Create_List(total_entries, col_num, temp_table)
    key = Uniqueness_Key(ID_len, lst)
    lst = New_Array(key, lst)
    return lst

def main(filename1):
    
    temp_table=[]
    with open(filename1, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for column in csvreader:
            if column != 0:
                temp_table.append(column)
    temp_table=np.transpose(temp_table)
    
    #total element number
    total_entries = len(temp_table[0])
    
    #create lists for each ID category
    subjects = ID_Assignment(total_entries, 0, temp_table, 3)
    countries = ID_Assignment(total_entries, 1, temp_table, 9)
    languages = ID_Assignment(total_entries, 2, temp_table, 7)
    people = ID_Assignment(total_entries, 3, temp_table, 10)
    research_area = ID_Assignment(total_entries, 4, temp_table, 8)
    #tags = ID_Assignment(total_entries, 5, temp_table, 11)
    
    for i in range(len(subjects)):
        print(research_area[i].ID)
    
    return subjects, countries, languages, people, research_area #, tags
    


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("2 arguments needed")
        sys.exit(os.EX_OK)
    file1Path = sys.argv[1]
    main(file1Path)
