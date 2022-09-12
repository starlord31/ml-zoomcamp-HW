#!/usr/bin/env python
# coding: utf-8

# In[174]:


import numpy as np
np.__version__


# In[175]:


import pandas as pd
df = pd.read_csv('E:\Downloads\data.csv')
df


# In[176]:


cm_grouped = df.groupby(['Make'])['Make'].count().sort_values(ascending=False)
cm_grouped


# In[177]:


df[df['Make'] == 'Audi'].nunique()


# In[178]:


df.isnull().sum()


# In[179]:


df['Engine Cylinders'].median()


# In[180]:


ec = df.groupby(['Engine Cylinders'])['Engine Cylinders'].count().sort_values(ascending=False)
ec


# In[181]:


s = df
s['Engine Cylinders'].fillna(value = 4.0, inplace = True)
s['Engine Cylinders'].median()


# In[182]:


new = df[['Make', 'Engine HP', 'Engine Cylinders']]
new[df['Make']=='Audi'].drop_duplicates()


# In[ ]:





# In[ ]:





# In[ ]:




