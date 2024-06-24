#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
path = '19.Income share held by lowest 20.csv.csv'
data = pd.read_csv(path)
data.replace('..', 0, inplace = True)
data.to_csv('19c.Income share held by lowest 20.csv', index= False)


# In[66]:


# Load the CSV file
df1 = pd.read_csv('Highmiddle_income.csv.csv') 


# Filter the DataFrame for middle-income and upper-middle-income countries
# Assuming the relevant income levels are labeled exactly as 'Middle income' and 'Upper middle income'
filtered_df1 = df1[df1['Income Group'].isin(['High income', 'Upper middle income'])]
country_codes1 = filtered_df1['Country Code'].tolist()

print(country_codes1)
print(len(country_codes1))


# In[ ]:





# In[ ]:





# In[ ]:




