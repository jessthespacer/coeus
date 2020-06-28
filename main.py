#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:38:57 2020

@author: kaitlyn
"""
import numpy as np
import csv
import pandas as pd

#from ID_Generation import Create_List(total_entries, col_num, temp_table)
from ID_Generation import ID_Assignment
from ID_Generation import People_ID
from ID_Generation import Create_List


col_s = 2
col_c = 3
col_l = 4
col_p = 0
col_r = 5
col_u = 1
col_t = 6
col_ur = 7
col_pr = 8
col_fr = 9
col_pn = 10

class Element:
    pass



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
    sbjs, sbjs_ID = ID_Assignment(total_entries, col_s, temp_table, 3)
    #print(sbjs_ID)
    cntrs, cntrs_ID = ID_Assignment(total_entries, col_c, temp_table, 4)
    lang, lang_ID = ID_Assignment(total_entries, col_l, temp_table, 5)
    ppl, ppl_ID = People_ID(total_entries, 6, col_p, temp_table)
    ra, ra_ID = ID_Assignment(total_entries, col_r, temp_table, 7)
    uni, uni_ID = ID_Assignment(total_entries, col_u, temp_table, 8)
    tags, tags_ID = ID_Assignment(total_entries, col_t, temp_table, 9)
    
    tag = Create_List(total_entries, col_t, temp_table)
    print(tag)

    
    #lists that dont need IDs
    uni_rnk = Create_List(total_entries, col_ur, temp_table)
    url_prs = Create_List(total_entries, col_pr, temp_table)
    url_fty = Create_List(total_entries, col_fr, temp_table)
    pubnum = Create_List(total_entries, col_pn, temp_table)
    
    #subject table
    sbjs_tbl = { 'Subject': sbjs,
                 'Subject ID': sbjs_ID
            }
    df = pd.DataFrame(sbjs_tbl, columns= ['Subject', 'Subject ID'])
    df.to_csv (r'/home/kaitlyn/Documents/hackathon/sbjs_tbl.csv', index = False, header=True)
    
    #language table
    lng_tbl = { 'Language': lang,
                'Language ID': lang_ID
            }
    df = pd.DataFrame(lng_tbl, columns= ['Language', 'Language ID'])
    df.to_csv (r'/home/kaitlyn/Documents/hackathon/sbjs_tbl.csv', index = False, header=True)
    

    #country table
    cntr_tbl = { 'Country': cntrs,
                 'Country ID': cntrs_ID
            }
    df1 = pd.DataFrame(cntr_tbl, columns= ['Country', 'Country ID'])
    df1.to_csv (r'/home/kaitlyn/Documents/hackathon/cntrs_tbl.csv', index = False, header=True)
    
    #uni table
    uni_tbl = { 'University': uni,
                 'University ID': uni_ID,
                 'Country ID': cntrs_ID,
                 'University Ranking': uni_rnk
            }
    df2 = pd.DataFrame(uni_tbl, columns= ['University', 'University ID', 'Country ID', 'University Ranking'])
    df2.to_csv (r'/home/kaitlyn/Documents/hackathon/uni_tbl.csv', index = False, header=True)
    
    #Research Area Table
    ra_tbl = { 'Research Area': ra,
               'Research Area ID': ra_ID,
               'Subject ID': sbjs_ID
            }
    df3 = pd.DataFrame(ra_tbl, columns= ['Research Area','Research Area ID', 'Subject ID'])
    df3.to_csv (r'/home/kaitlyn/Documents/hackathon/ra_tbl.csv', index = False, header=True)

    #Tags Table
    tag_tbl = { 'Tag': tags,
               'Tag ID': tags_ID,
               'RA ID': ra_ID
            }
    df4 = pd.DataFrame(tag_tbl, columns= ['Tag','Tag ID', 'RA ID'])
    df4.to_csv (r'/home/kaitlyn/Documents/hackathon/tag_tbl.csv', index = False, header=True)

    #People Table
    ppl_tbl = { 'Name': ppl,
               'Person ID': ppl_ID,
               'RA ID': ra_ID,
               'University ID': uni_ID,
               'Personal URL': url_prs,
               'Faculty URL': url_fty,
               'NumPubs': pubnum
            }
    df5 = pd.DataFrame(ppl_tbl, columns= ['Name','Person ID', 'RA ID', 'University ID', 'Personal URL', 'Faculty URL', 'NumPubs'])
    df5.to_csv (r'/home/kaitlyn/Documents/hackathon/ppl_tbl.csv', index = False, header=True)
    

    
    #for i in range(len(sbjs_ID)):
    #    print(lang_ID[i])
    


if __name__ == "__main__":
    """
    import sys
    if len(sys.argv) != 2:
        print("2 arguments needed")
        sys.exit(os.EX_OK)
    file1Path = sys.argv[1]
    """
    file1Path = '/home/kaitlyn/Documents/hackathon/sample.csv'
    
    file = main(file1Path)