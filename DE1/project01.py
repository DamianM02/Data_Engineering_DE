#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd


# In[32]:


df=pd.read_csv("lab1_ex01.csv")


# In[33]:


import json


# In[34]:


list=[]

for col in df.columns:
    dictionary={
        "name": col,
        "missing": df[col].isna().sum() / len(df[col]),
        "type": "other"
    }

    if df[col].dtype=="int64":
        dictionary["type"]="int"

    elif df[col].dtype=="float64":
        dictionary["type"]="float"
    list.append(dictionary)


# In[35]:


with open("ex01_fields.json", "w") as f:
    json.dump(list, f)


# In[36]:


import numpy as np


# In[37]:


dictionary={}
for col in df.columns:
    if df[col].dtype != 'object':
        dictionary.update({col:df[col].describe().to_dict()})
    else:
        dict={
            'count': str(len(df[col])-df[col].isna().sum()),
            'unique':str(len(df[col].unique())),
            'top':str(df[col].value_counts().idxmax()),
            'freq':str(df[col].value_counts().max()),
        }
        dictionary.update({col:dict})


# In[38]:


with open('ex02_stats.json', 'w') as f:
    json.dump(dict, f)


# In[39]:


lista=[]
c="s"
for col in df.columns:
    col="".join(char for char in col if char.isalnum() or char in [' ', '_'])
    col=col.lower()
    col=col.replace(' ', '_')
    lista.append(col)



# In[40]:

df.columns=lista
df.to_csv('ex03_columns.csv', index=False)


# In[41]:


import pickle
#!pip install openpyxl
import openpyxl


# In[42]:


pd.DataFrame(df).to_excel('ex04_excel.xlsx', index=False)

with open('ex04_json.json', 'w') as f:
    json.dump(df.to_dict(orient='records'), f)

with open('ex04_pickle.pkl', 'wb') as f:
    pickle.dump(df, f)


# In[43]:


dff=pd.read_pickle('lab1_ex05.pkl')
dff = dff.fillna('')
(dff.iloc[dff.index.str.startswith('v'), 1:3]).to_markdown('ex05_table.md')


# In[44]:


with open("lab1_ex06.json", 'r') as p:
    data=json.load(p)

dff = pd.json_normalize(data, sep='.')

dff.to_pickle('ex06_pickle.pkl')


# In[44]:




