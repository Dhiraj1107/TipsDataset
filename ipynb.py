#!/usr/bin/env python
# coding: utf-8

# In[3]:


import seaborn as sns
import pandas as pd


# In[4]:


tips=sns.load_dataset('tips')


# In[5]:


tips.head()


# In[6]:


tips.day.unique()


# In[7]:


tips.day.value_counts()


# In[8]:


tips.day.value_counts().plot(kind='bar')


# In[9]:


tips.time.value_counts(normalize=True)


# In[10]:


tips.groupby(['time'])['tip'].mean().plot.bar()


# In[11]:


tips.groupby(['sex'])['tip'].mean().plot.bar()


# In[12]:


tips.groupby(['smoker'])['tip'].mean().plot.bar()


# In[13]:


tips.groupby(['size'])['tip'].mean().plot.bar()


# In[14]:


tips.groupby(['smoker','sex'])['tip'].mean().unstack()


# In[15]:


tips.groupby(['smoker','sex'])['tip'].mean()


# In[16]:


tips.groupby(['smoker','day'])['tip'].mean().unstack()


# In[17]:


tips['tips_per']=(tips.tip/tips.total_bill)*100
tips_per.head()


# In[18]:


tips['tips_per']=(tips.tip/tips.total_bill)*100


# In[19]:


tips.head()


# In[20]:


tips.plot.scatter(x='total_bill',y='tip')


# In[21]:


sns.scatterplot(x='total_bill',y='tip',data=tips)


# In[22]:


sns.scatterplot(x='total_bill',y='tip',data=tips,hue='sex')


# In[23]:


sns.scatterplot(x='total_bill',y='tip',data=tips,hue='day')


# In[24]:


sns.scatterplot(x='total_bill',y='tip',data=tips,hue='time')


# In[25]:


sns.relplot(x='total_bill',y='tip',data=tips,col='sex',hue='time')


# In[26]:


sns.__version__


# In[27]:


sns.pairplot(data=tips, hue="sex")


# In[31]:


sns.displot (data=tips,x="total_bill",col="time",kde=True)


# In[ ]:




