#!/usr/bin/env python
# coding: utf-8

# In[162]:


import pandas as pd

sep=[ '|',',', ';']
for i in sep:
    dec=','
    if i==',':
        dec='.'
    df=pd.read_csv("proj2_data.csv", sep=i, decimal=dec)
    if len(list(df.columns))>1:
        break


# # Exercise 1

# In[163]:


df


# In[164]:


import pickle as pkl
with open ("proj2_ex01.pkl", "wb") as f:
    pkl.dump(df, f)


# 
# # Exercise 2

# In[165]:


dict={}
f=open("proj2_scale.txt", 'r')
t=1
for i in f:
    dict.update({i.replace('\n', ''):t})
    t+=1
f.close()


# In[166]:


df2=df.copy()
df2[["task_grade", "final_grade"]]=df2[["task_grade", "final_grade"]].replace(dict)


# In[167]:


#df2


# In[168]:


with open("proj2_ex02.pkl", "wb") as f:
    pkl.dump(df2, f)


# # Exercise 3

# In[169]:


##################################################################################

f=open("proj2_scale.txt", 'r')

category=pd.CategoricalDtype([i.replace("\n", '') for i in f])
df3=df.copy()
df3[["task_grade", "final_grade"]]=df3[["task_grade", "final_grade"]].astype(category)

f.close()
df3.dtypes


# In[170]:


with open("proj2_ex03.pkl", "wb") as f:
    pkl.dump(df3,f)


# # Exercise 4

# In[182]:


################################################################################

import numpy as np
import math
df4=pd.DataFrame()
for i in df.keys():
    if df[i].dtype==object:
        d=df[i].str.extract("([-+]?\d*[\.\,]?\d+)")
        if not d.isna().values.all():
            df4[i]=d


# In[183]:


df4=df4["jury_score"].str.replace(',', '.')
pd.to_numeric(df4)
df4=df4.sort_values(ignore_index=True)


# In[184]:


df4


# In[173]:


with open("proj2_ex04.pkl", "wb") as f:
    pkl.dump(df4, f)


# 
# # Exercise 5
# 

# In[174]:


text=df.columns[df.dtypes==object]

uniquecols=df.columns[df.nunique()<=10]

atoz=df.columns[df.columns.str.fullmatch("[a-z]+")]

notin2=[]



# In[174]:





# In[174]:




