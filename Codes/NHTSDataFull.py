#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 06:42:42 2023

@author: eduardolopez
"""

import pandas as pd
import numpy as np
from pathlib import Path
file_path = Path("/Users/eduardolopez/downloads/csv/vehpub.csv")
wwc = pd.read_csv(file_path)

import matplotlib.pyplot as plt
import seaborn as sns

columns= ['HOUSEID', 'VEHID', 'VEHYEAR', 'VEHAGE', 'MAKE', 'MODEL', 'FUELTYPE',
       'VEHTYPE', 'WHOMAIN', 'OD_READ', 'HFUEL', 'VEHOWNED', 'VEHOWNMO',
       'ANNMILES', 'HYBRID', 'PERSONID', 'TRAVDAY', 'HOMEOWN', 'HHSIZE',
       'HHVEHCNT', 'HHFAMINC', 'DRVRCNT', 'HHSTATE', 'HHSTFIPS', 'NUMADLT',
       'WRKCOUNT', 'TDAYDATE', 'LIF_CYC', 'MSACAT', 'MSASIZE', 'RAIL', 'URBAN',
       'URBANSIZE', 'URBRUR', 'CENSUS_D', 'CENSUS_R', 'CDIVMSAR', 'HH_RACE',
       'HH_HISP', 'HH_CBSA', 'SMPLSRCE', 'WTHHFIN', 'BESTMILE', 'BEST_FLG',
       'BEST_EDT', 'BEST_OUT', 'HBHUR', 'HTHTNRNT', 'HTPPOPDN', 'HTRESDN',
       'HTEEMPDN', 'HBHTNRNT', 'HBPPOPDN', 'HBRESDN', 'GSYRGAL', 'GSTOTCST',
       'FEGEMPG', 'FEGEMPGA', 'GSCOST', 'FEGEMPGF']

    
wwc = wwc[(wwc['VEHAGE'] >= 0) & (wwc['OD_READ'] >= 0) & (wwc['GSTOTCST'] >= 0) & (wwc['FEGEMPG'] >= 0)]

for col in ['VEHAGE','OD_READ','GSTOTCST','FEGEMPG']:
    sns.histplot(data=wwc, x=col)
    plt.show()
    
mean_age = wwc['VEHAGE'].mean()
median_age = wwc['VEHAGE'].median()
std_dev_age = wwc['VEHAGE'].std()
mean_abs_dev_age = np.abs(wwc['VEHAGE'] - wwc['VEHAGE'].mean()).mean()

print("Mean age:", mean_age)
print("Median age:", median_age)
print("Standard deviation of age:", std_dev_age)
print("Mean absolute deviation of age:", mean_abs_dev_age)

mean_age = wwc['OD_READ'].mean()
median_age = wwc['OD_READ'].median()
std_dev_age = wwc['OD_READ'].std()
mean_abs_dev_age = np.abs(wwc['OD_READ'] - wwc['OD_READ'].mean()).mean()

print("Mean read:", mean_age)
print("Median read:", median_age)
print("Standard deviation of read:", std_dev_age)
print("Mean absolute deviation of read:", mean_abs_dev_age)

mean_age = wwc['GSTOTCST'].mean()
median_age = wwc['GSTOTCST'].median()
std_dev_age = wwc['GSTOTCST'].std()
mean_abs_dev_age = np.abs(wwc['GSTOTCST'] - wwc['GSTOTCST'].mean()).mean()

print("Mean cost:", mean_age)
print("Median cost:", median_age)
print("Standard deviation of cost:", std_dev_age)
print("Mean absolute deviation of cost:", mean_abs_dev_age)

mean_age = wwc['FEGEMPG'].mean()
median_age = wwc['FEGEMPG'].median()
std_dev_age = wwc['FEGEMPG'].std()
mean_abs_dev_age = np.abs(wwc['FEGEMPG'] - wwc['FEGEMPG'].mean()).mean()

print("Mean economy:", mean_age)
print("Median economy:", median_age)
print("Standard deviation of economy:", std_dev_age)
print("Mean absolute deviation of economy:", mean_abs_dev_age)
    
pd.plotting.scatter_matrix(wwc.iloc[:,[3, 9, 55, 56]],figsize=(15,15))

perc = np.linspace(0,100,len(wwc))

#EcovsFossilHistogram
data = wwc[(wwc['VEHAGE'] >= 0) & (wwc['OD_READ'] >= 0) & (wwc['GSTOTCST'] >= 0) & (wwc['FEGEMPG'] >= 0)]
fossil_data = wwc[(wwc['FUELTYPE'] == 1) | (wwc['FUELTYPE'] == 2)]
eco_data = wwc[wwc['FUELTYPE']== 3]
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20,10))
ax1.hist(fossil_data['GSTOTCST'], bins=100)
ax1.set_title('Fossil Fuel Dataset')
ax1.set_xlabel('GSTOTCST')
ax1.set_ylabel('Frequency')
ax2.hist(eco_data['GSTOTCST'], bins=100)
ax2.set_title('Ecological Dataset')
ax2.set_xlabel('GSTOTCST')
ax2.set_ylabel('Frequency')
plt.xlim(0,80000)
plt.show()

#UrbanvsRuralHistogram
urban_data = wwc[wwc['URBRUR'] == 1]
rural_data = wwc[wwc['URBRUR'] == 2]
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20, 10))
perc = np.linspace(0,100,len(data))
ax1.hist(urban_data['GSTOTCST'], bins=100)
ax1.set_title('Urban Dataset')
ax1.set_xlabel('GSTOTCST')
ax1.set_ylabel('Frequency')
ax2.hist(rural_data['GSTOTCST'], bins=100)
ax2.set_title('Rural Dataset')
ax2.set_xlabel('GSTOTCST')
ax2.set_ylabel('Frequency')
plt.xlim(0,60000)
plt.show()

#USvsPAHistogram
us_data = wwc
pa_data = wwc[wwc['HHSTATE'] == 'PA']
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20, 10))
perc = np.linspace(0,100,len(data))
ax1.hist(us_data['GSTOTCST'], bins=100)
ax1.set_title('US Dataset')
ax1.set_xlabel('GSTOTCST')
ax1.set_ylabel('Frequency')
ax2.hist(pa_data['GSTOTCST'], bins=100)
ax2.set_title('PA Dataset')
ax2.set_xlabel('GSTOTCST')
ax2.set_ylabel('Frequency')
plt.xlim(0,80000)
plt.show()

#Correlations
vehage = wwc['VEHAGE']
odread = wwc['OD_READ']
gstotcst = wwc['GSTOTCST']
fegempg = wwc['FEGEMPG']

print("Correlations:")
print(vehage.corr(odread))
print(vehage.corr(gstotcst))
print(vehage.corr(fegempg))
print(odread.corr(gstotcst))
print(odread.corr(fegempg))
print(gstotcst.corr(fegempg))

#EcovsFossilHistogram
data = wwc[(wwc['VEHAGE'] >= 0) & (wwc['OD_READ'] >= 0) & (wwc['GSTOTCST'] >= 0) & (wwc['FEGEMPG'] >= 0)]
fossil_data = wwc[(wwc['FUELTYPE'] == 1) | (wwc['FUELTYPE'] == 2)]
eco_data = wwc[wwc['FUELTYPE'] == 3]

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20, 10))

# calculate the percentage and plot the fossil fuel dataset
n, bins, patches = ax1.hist(fossil_data['GSTOTCST'], bins=100, density=False)
ax1.set_title('Fossil Fuel Dataset')
ax1.set_xlabel('GSTOTCST')
ax1.set_ylabel('Relative Frequency (%)')
ax1.set_ylim(0, 100)
for i in range(len(patches)):
    patches[i].set_height(patches[i].get_height() / sum(n) * 100)

# calculate the percentage and plot the ecological dataset
n, bins, patches = ax2.hist(eco_data['GSTOTCST'], bins=100, density=False)
ax2.set_title('Ecological Dataset')
ax2.set_xlabel('GSTOTCST')
ax2.set_ylabel('Relative Frequency (%)')
ax2.set_ylim(0, 100)
for i in range(len(patches)):
    patches[i].set_height(patches[i].get_height() / sum(n) * 100)

plt.xlim(0, 80000)
plt.show()

data = wwc[(wwc['VEHAGE'] >= 0) & (wwc['OD_READ'] >= 0) & (wwc['GSTOTCST'] >= 0) & (wwc['FEGEMPG'] >= 0)]
urban_data = data[data['URBRUR'] == 1]
rural_data = data[data['URBRUR'] == 2]

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20, 10))


# plot the urban dataset
n, bins, patches = ax1.hist(urban_data['GSTOTCST'], bins=100, density=False)
ax1.set_title('Urban Dataset')
ax1.set_xlabel('GSTOTCST')
ax1.set_ylabel('Relative Frequency (%)')
ax1.set_ylim(0, 100)
plt.xlim(0, 10000)
for i in range(len(patches)):
    patches[i].set_height(patches[i].get_height() / len(urban_data) * 100)


# plot the rural dataset
n, bins, patches = ax2.hist(rural_data['GSTOTCST'], bins=100, density=False)
ax2.set_title('Rural Dataset')
ax2.set_xlabel('GSTOTCST')
ax2.set_ylabel('Relative Frequency (%)')
ax2.set_ylim(0, 100)
for i in range(len(patches)):
    patches[i].set_height(patches[i].get_height() / len(rural_data) * 100)

plt.xlim(0, 60000)
plt.show()

data = wwc[(wwc['VEHAGE'] >= 0) & (wwc['OD_READ'] >= 0) & (wwc['GSTOTCST'] >= 0) & (wwc['FEGEMPG'] >= 0)]
us_data = wwc
pa_data = data[data['HHSTATE'] == 'PA']
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20, 10))


# plot the US dataset
n, bins, patches = ax1.hist(us_data['GSTOTCST'], bins=100, density=False)
ax1.set_title('US Dataset')
ax1.set_xlabel('GSTOTCST')
ax1.set_ylabel('Relative Frequency (%)')
ax1.set_ylim(0, 100)
plt.xlim(0, 10000)
for i in range(len(patches)):
    patches[i].set_height(patches[i].get_height() / len(us_data) * 100)


# plot the PA dataset
n, bins, patches = ax2.hist(pa_data['GSTOTCST'], bins=100, density=False)
ax2.set_title('PA Dataset')
ax2.set_xlabel('GSTOTCST')
ax2.set_ylabel('Relative Frequency (%)')
ax2.set_ylim(0, 100)
for i in range(len(patches)):
    patches[i].set_height(patches[i].get_height() / len(pa_data) * 100)

plt.xlim(0, 80000)
plt.show()

