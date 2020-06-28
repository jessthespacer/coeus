#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup, Comment

import pandas as pd

uni_names = pd.read_csv("./universities.txt", header=None)

uni_names.columns = ['name']

# initialize a pandas dataframe that will contain all the scraped data
# add more columns name as needed
data = pd.DataFrame(columns=['name', "locality", "state", "country", 'url'])


# In[133]:


for uni in uni_names.name:
    # make url -> fetch page -> parse html -> select the table on the sidebar
    uni_wiki_url = "https://en.wikipedia.org/wiki/" + "_".join(uni.split(" "))
    page = requests.get(uni_wiki_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    sidebar_table = soup.find_all('table', {"class": "infobox vcard"})[0]
    
    # key-value variable to store everything for one particular uni
    juice = {"name" : uni}

    # find url
    url = sidebar_table.find("span", class_="url")
    url = url.find("a", href=True)
    juice['url'] = url['href']
    
    try:
        queries = ['locality', 'country-name', 'state']
        columns = ['locality', 'country', 'state']
        for query, column in zip(queries, columns):
            location = sidebar_table.find("th", string="Location").parent
            loc = location.find("div", class_=query)
            juice[column] = loc.text
    except:
        # probably, state was missing
        pass
    # Add the new Uni entry to the grand table aka. `data`
    data = data.append(juice, ignore_index=True)

print(data)

