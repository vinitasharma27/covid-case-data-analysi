#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[2]:


covid_df = pd.read_csv("C:/Users/hp/Downloads/covid_19_india.csv")


# In[3]:


covid_df.head(10)


# In[4]:


covid_df.info()


# In[5]:


covid_df.describe()


# In[6]:


vaccine_df = pd.read_csv("C:/Users/hp/Downloads/covid_vaccine_statewise.csv")


# In[7]:


vaccine_df.head(7)


# In[8]:


covid_df.drop(["Sno","Time","ConfirmedIndianNational","ConfirmedForeignNational"] ,inplace = True,axis = 1)


# In[9]:


covid_df.head()


# In[10]:


covid_df['Date'] = pd.to_datetime(covid_df['Date'],format = '%Y-%m-%d')


# In[11]:


covid_df['Active_Cases'] = covid_df['Confirmed'] - (covid_df['Cured'] + covid_df['Deaths'])
covid_df.tail()


# In[12]:


statewise = pd.pivot_table(covid_df,values = ["Confirmed","Deaths","Cured"],index = "State/UnionTerritory",aggfunc = max)


# In[13]:


statewise["Recovery Rate"] = statewise["Cured"]*100/statewise["Confirmed"]


# In[14]:


statewise["Morality Rate"] = statewise["Deaths"]*100/statewise["Confirmed"]


# In[15]:


statewise = statewise.sort_values(by = "Confirmed",ascending = False)


# In[16]:


statewise.style.background_gradient(cmap = "cubehelix")


# In[17]:


# top ten active cases
top_10_active_cases = covid_df.groupby(by = 'State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by = ['Active_Cases'],ascending = False).reset_index()


# In[18]:


fig = plt.figure(figsize = (16,9))


# In[19]:


plt.title("Top 10 states with most cases in India",size = 25)


# In[20]:


ax = sns.barplot(data =  top_10_active_cases.iloc[:10],y = 'Active_Cases',x = 'State/UnionTerritory',linewidth = 2,edgecolor = 'red')


# In[21]:


# top ten active cases
top_10_active_cases = covid_df.groupby(by = 'State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by = ['Active_Cases'],ascending = False).reset_index()

fig = plt.figure(figsize = (16,9))
plt.title("Top 10 states with most cases in India",size = 25)


ax = sns.barplot(data =  top_10_active_cases.iloc[:10],y = 'Active_Cases',x = 'State/UnionTerritory',linewidth = 2,edgecolor = 'red')


plt.xlabel('States')
plt.ylabel('Total Active Cases')
plt.show()


# In[22]:


# Top states with highest deaths
top_10_deaths = covid_df.groupby(by = 'State/UnionTerritory').max()[['Deaths','Date']].sort_values(by = ['Deaths'],ascending = False).reset_index()


# In[23]:


top_10_deaths = covid_df.groupby(by = 'State/UnionTerritory').max()[['Deaths','Date']].sort_values(by = ['Deaths'],ascending = False).reset_index()
fig = plt.figure(figsize=(18,5))
plt.title("top 10 states with most Deaths",size =25 )
ax = sns.barplot(data = top_10_deaths.iloc[:12],y = "Deaths",x = "State/UnionTerritory",linewidth = 2 , edgecolor = 'black')
plt.xlabel("States")
plt.ylabel("Total Death Cases")
plt.show()


# In[24]:


# Growth trend
fig = plt.figure(figsize=(12,6))
ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Maharastra','Kernataka','Kerala','Tamil Nadu','Uttar Pradesh']),
                                  x = 'Date' , y = 'Active_Cases', hue = 'State/UnionTerritory'])
ax.set_title("top 5 affected states in India",size = 16 )


# In[ ]:


vaccine_df.head()


# In[ ]:


vaccine_df.rename(columns = {'Updated On' : 'Vaccine_Date'},inplace = True)


# In[ ]:


vaccine_df.head(10)


# In[ ]:


vaccine_df.info()


# In[ ]:


vaccine_df.isnull().sum()


# In[ ]:


vaccination = vaccine_df.drop(columns = ['Sputnik V (Doses Administered)','AEFI','18-44 Years (Doses Administered)','45-60 Years (Doses Administered)','60+ Years (Doses Administered)'], axis = 1)


# In[ ]:


vaccination.head()


# In[ ]:


# MALE VS FEMALE VACINATION
male = vaccination["Male(Individuals Vaccinated)"].sum()
female = vaccination["Female(Individuals Vaccinated)"].sum()
px.pie(names =["Male","Female"],values = [male, female] , title = "Male and Female Vaccination")


# In[ ]:


# remove rows where state is India
vaccine = vaccine_df[vaccine_df.State!='India']
vaccine


# In[ ]:


vaccine.rename(columns = {"Total Individuals Vaccinated": "Total"},inplace = True)
vaccine


# In[ ]:


# most vaccinated  state
max_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac = max_vac.sort_values('Total',ascending = False)[:5]
max_vac


# In[ ]:


fig = plt.figure(figsize = (10,5))
plt.title("TOP 5 VACINATED STATES IN INDIA",size = 20)
x = sns.barplot(data = max_vac.iloc[:10], y = max_vac.Total,x = max_vac.index,linewidth = 2,edgecolor = 'black')
plt.xlabel("states")
plt.ylabel("vaccination")
plt.show()


# In[ ]:


# least vaccinated  state
min_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
min_vac = min_vac.sort_values('Total',ascending = True)[:5]
min_vac


# In[ ]:


fig = plt.figure(figsize = (10,5))
plt.title("TOP 5 LEAST VACINATED STATES IN INDIA",size = 20)
x = sns.barplot(data = min_vac.iloc[:10], y = max_vac.Total,x = max_vac.index,linewidth = 3,edgecolor = 'red')
plt.xlabel("states")
plt.ylabel("vaccination")
plt.show()


# In[ ]:




