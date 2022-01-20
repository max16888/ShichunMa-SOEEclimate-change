#!/usr/bin/env python
# coding: utf-8

# # Experiments with change the emission

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import fair
from fair.forward import fair_scm
from fair.SSPs import ssp126, ssp245, ssp370, ssp585


# In[2]:


ssp245.Emissions.emissions


# In[3]:


ssp245.Emissions.emissions.shape


# In[4]:


C45,F45,T45 = fair_scm(emissions = ssp245.Emissions.emissions)


# In[5]:


stop_emitting = ssp245.Emissions.emissions.copy()


# In[6]:


stop_emitting[265:, 1:] = 0


# In[7]:


Cstop, Fstop, Tstop = fair_scm(emissions = stop_emitting)


# In[23]:


plt.plot(np.arange(1765,2501), T45, label='SSP245')
plt.plot(np.arange(1765,2501), Tstop, label='Zero emissions 2030')
plt.xlabel('year')
plt.ylabel('Temperature relative to 1765, K')
plt.title('SSP245 and zero emissions from 2030')
plt.legend()
plt.savefig('002_plot.png') # save figure


# In[9]:


plt.plot(np.arange(2030, 2501), Tstop[265:]-Tstop[265])
plt.title('Committed warming')
plt.ylabel('Temperature relative to 2030, K')
plt.xlabel('year')


# In[19]:


T = {}
species = {
    1 : 'CO2 fossil',
    2 : 'CO2 land use',
    3 : 'Methane',
    4 : 'Nitrous oxide',
    5 : 'Sulphate',
    9 : 'Black carbon',
}
for stop in [1,2,3,4,5,9]:
    stop_emitting = ssp245.Emissions.emissions.copy()
    stop_emitting[265:, stop] = 0
    C, F, T[species[stop]] = fair_scm(emissions = stop_emitting)
    plt.plot(np.arange(1765,2501), T[species[stop]], label='Zero %s' % species[stop])
plt.plot(np.arange(1765,2501), T45, label='SSP245')
plt.legend()


# In[11]:


label='Zero %s' % species[stop]


# In[22]:


for stop in [1,2,3,4,5,9]:
    plt.plot(np.arange(1765,2501), T[species[stop]] - T45,
label='Zero %s' % species[stop])
plt.legend()
plt.xlim(2020, 2100)
plt.ylim(-1.25,0.25)
plt.ylabel('Temperature compared to SSP245, K')
plt.title('Zero emissions commitments')
plt.savefig('001_plot.png') # save figure


# In[13]:


df = pd.DataFrame(data=ssp245.Emissions.emissions)
df.set_index(0, inplace=True)
df.index.name = 'year'
# these are not required - it just might help
df.columns = ['FossilCO2', 'OtherCO2', 'CH4', 'N2O', 'SOx',
'CO', 'NMVOC', 'NOx', 'BC', 'OC', 'NH3', 'CF4', 'C2F6',
'C6F14', 'HFC23', 'HFC32', 'HFC43_10', 'HFC125', 'HFC134a',
'HFC143a', 'HFC227ea', 'HFC245fa', 'SF6', 'CFC_11', 'CFC_12',
'CFC_113', 'CFC_114', 'CFC_115', 'CARB_TET', 'MCF', 'HCFC_22',
'HCFC_141B', 'HCFC_142B', 'HALON1211', 'HALON1202',
'HALON1301', 'HALON2402', 'CH3BR', 'CH3CL']
df


# In[14]:


df.to_csv('emissions_file.csv')


# In[15]:


df = pd.read_csv('emissions_file_modified.csv')
df


# In[16]:


# extract data
emissions = df.values
emissions


# In[17]:


Cnew, Fnew, Tnew = fair_scm(emissions = emissions)
plt.plot(np.arange(1765, 2501), T45, label='SSP245')
plt.plot(np.arange(1765, 2501), Tnew, label='CO2 ramp down and no CFCs')
plt.legend()


# In[ ]:




