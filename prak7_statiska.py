#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
#memanggil dan menampilkan dataset
data_tommy = pd.read_csv('C:/kuliah/Semester 2/titanic - titanic.csv')
print(data_tommy)


# In[6]:


#mengambil data pada kolom tertentu
data1 = data_tommy.loc[:,['Age','Pclass','Survived']]
print(data1)


# In[7]:


#memvisualisasikan data titanic
data2 = data_tommy[['Age', 'Pclass', 'Survived']]
data2.plot(title='Persebaran Data', x='Age', y='Pclass', kind='scatter', c='Survived', colormap='Paired')


# In[8]:


#memanipulasi data jumlah penumpang berdasarkan group Pclass
data3 = data_tommy[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
penumpang=data3.groupby('Pclass')['Name'].nunique()
print('Jumlah Penumpang:\n', penumpang)


# In[9]:


#memfilter data penumpang yang selamat berdasarkan pclass
data4 = data_tommy[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
notsurvivedpassanger=data4['Pclass'].loc[data_tommy['Survived']==0]
print('Penumpang yang tidak survived:\n', notsurvivedpassanger.value_counts())
survivedpassanger=data4['Pclass'].loc[data_tommy['Survived']==1]
print('\nPenumpang yang survived:\n', survivedpassanger.value_counts())


# In[11]:


#memanipulasi data jumlah penumpang berdasarkan group Sex
data3 = data_tommy[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
penumpang=data3.groupby('Sex')['Name'].nunique()
print('Jumlah Penumpang:\n', penumpang)


# In[12]:


#memfilter data penumpang yang selamat berdasarkan pclass
data4 = data_tommy[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
notsurvivedpassanger=data4['Pclass'].loc[data_tommy['Survived']==0]
print('Penumpang yang tidak survived:\n', notsurvivedpassanger.value_counts())
survivedpassanger=data4['Pclass'].loc[data_tommy['Survived']==1]
print('\nPenumpang yang survived:\n', survivedpassanger.value_counts())


# In[15]:


#memfilter data penumpang yang selamat berdasarkan sex
data4 = data_tommy[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
notsurvivedpassanger=data4['Sex'].loc[data_tommy['Survived']==0]
print('Penumpang yang tidak survived:\n', notsurvivedpassanger.value_counts())
survivedpassanger=data4['Sex'].loc[data_tommy['Survived']==1]
print('\nPenumpang yang survived:\n', survivedpassanger.value_counts())


# In[ ]:




