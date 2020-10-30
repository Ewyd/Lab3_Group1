#!/usr/bin/env python
# coding: utf-8
To execute the code, execute every cells in the order. To execute it, click on a cell then click on the button "Run" above. Follow the instructions! 
# In[1]:


pip install ipynb


# In[2]:


# The client function needs to be imported for you to be able to send messages.
from ipynb.fs.full.Fonction_Client import ChartSend


# In[8]:


# You can run this code as many times as you want to send messages.
ChartSend()


# In[9]:


# The serveur function needs to be imported for you to be able to treat messages.
from ipynb.fs.full.Fonction_Serveur import QueueTreatment
QueueTreatment()


# In[10]:


#and then 
from ipynb.fs.full.Fonction_Serveur import createlogFile
createlogFile()

we would also have decided to run serveur function every X second, but we consider it easier to understand
# In[6]:


#You can also download your file once treated with the ID 
from ipynb.fs.full.Fonction_Client import ChartSent


# In[11]:


ChartSent()


# In[ ]:




