#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Import data, Diagonose, Clean Data, Visualize Data
Data: Correlation between fertility and female education

"""

import pandas as pd
import numpy as np
'''
It gives the percent of females aged 15 or over who can read and write , 
the averge number of children that a woman will give birth to, and population
for a given country in a continent.
'''
# The first 7 rows are description, we need to skil these 7 rows

#------ Step1: Import data set
fertility = pd.read_excel('TREND01-5G-educ-fertility-bubbles.xls',skiprows=7)


#------ Step2: Diagnose data set
fertility.head()
fertility.tail()
fertility.info()
fertility.columns2
fertility.dtypes

'''
 Problems
     1: Country and Continent is capitalized, female literacy has a space
     2: Missing values: NaN 
     3. Country names are french
     4. The column name 'Country ' has a space
     There are 196 countries in the world, not every country in this world 
     is listed in this dataset
     5. fertility column should contain float value, but contain object instead
'''

fertility.describe() #can only be used on numeric columns
#For categorical data diagnose, we can use .value_counts() method

#----- Step3: Clean data set

fertility['Continent'].value_counts(dropna=False)

fertility = fertility[~fertility['Continent'].isnull()] #remove all nan rows

fertility = fertility.iloc[:-2] # remove the last two rows

#change the column name 
fertility = fertility.rename(columns = {'Country ':'Country'
                                        ,'female literacy':'Female_Literacy'})

#Check each country only appear once
(fertility['Country'].value_counts(dropna=False) == 1).all()

#make sure there is no missing value at all for the whole data set
fertility.isnull().all()

#convert string type to float type 
fertility['Female_Literacy'] = fertility['Female_Literacy'].astype(float)
fertility['fertility'] = fertility['fertility'].astype(float)

#---- Step4: Visualization 

import matplotlib.pyplot as plt

#Histogram
fertility['population'].plot('hist')
plt.show()

fertility[fertility['population'] > 1000000000]

#Boxplot can find outlier
fertility.boxplot(column='population',by='Continent')
plt.show()

#Scatter plots
#Relationship between 2 numric variables

colors = list(fertility['Continent'])

for i in range(len(colors)):
    if(colors[i] == 'AF'):
        colors[i] = 'Blue'
    elif(colors[i] == 'LAT'):
        colors[i] = 'Brown'
    elif(colors[i] == 'EUR'):
        colors[i] = 'Yellow'
    elif(colors[i] == 'OCE'):
        colors[i] = 'Pink'
    elif(colors[i] == 'ASI'):
        colors[i] = 'Red'
    elif(colors[i] == 'NAM'):
        colors[i] = 'Green'
        
        
#dictionary for continent colors        
mycolor = {'AF':'Blue',
           'LAT':'Brown',
           'EUR':'Yellow',
           'OCE':'Pink',
           'ASI':'Red',
           'NAM':'Green'}

#total population of 'AF'
af = fertility[fertility['Continent']=='AF']
pop_af =  af['population'].sum()

#total population of 'LAT'
lat = fertility[fertility['Continent']=='LAT']
pop_lat =  lat['population'].sum()

#total population of 'EUR'
eur = fertility[fertility['Continent']=='EUR']
pop_eur =  eur['population'].sum()

#total population of 'OCE'
oce = fertility[fertility['Continent']=='OCE']
pop_oce =  oce['population'].sum()

#total population of 'ASI'
asi = fertility[fertility['Continent']=='ASI']
pop_asi =  asi['population'].sum()

#total population of 'NAM'
nam = fertility[fertility['Continent']=='NAM']
pop_nam =  nam['population'].sum()

#dictionary for continent population
mypop = {'AF':pop_af,
           'LAT':pop_lat,
           'EUR':pop_eur,
           'OCE':pop_oce,
           'ASI':pop_asi,
           'NAM':pop_nam}
        

#scatter plots relationship between female literacy and fertiliy
plt.scatter(fertility['Female_Literacy'],fertility['fertility'],
            s = fertility['population']/1000000, c = colors,label=None)

#s: size: population in millions
plt.xlabel('Adult female literacy(%)',fontsize=15)
plt.ylabel('Number of children per woman',fontsize=15)
plt.grid(True)
plt.title('Correlation between fertility and female education',fontsize=15)

plt.text(90.5,1.769,'China')
plt.text(50.8,2.682,'India')
plt.text(99.0,2.077,'USA')

plt.yticks([0,2,4,6,8,10])


continents = ['AF','LAT','EUR','OCE','ASI','NAM']
# Here we create a legend:
# we'll plot empty lists with the desired size and label
for area in continents:
    plt.scatter([], [], c = mycolor[area], alpha = 0.5, s = mypop[area]/10000000,
                label= area)
    plt.legend(loc='lower left',scatterpoints=1, frameon=False, labelspacing=1, title='Continets')
plt.show()


'''
Principles of tidy data
    1. Columns represent separate variables
    2. Rows represent individual observations
    3. Observational units form tables
    
For data to be tidy, it must have:    
    .Each variable as a separate column
    .Each row as a separate observation
'''


'''
    Melting data is the process of turning columns of your data into rows of data.
    Pivoting: turn each unique value of a variable, and turn them into separate columns.
'''

#Practice

europe = fertility[fertility['Continent'] == 'EUR']

plt.scatter(europe['Female_Literacy'],europe['fertility'],s = europe['population']/1000000
            ,c = 'yellow')

for item in europe['Country']:
    country = europe[europe['Country'] == item]
    x = country.Female_Literacy 
    y = country.fertility
    plt.text(x,y,item)


asi = fertility[fertility['Continent'] == 'ASI']

plt.scatter(asi['Female_Literacy'],asi['fertility'],s = asi['population']/1000000
            ,c = 'red')

oce = fertility[fertility['Continent'] == 'OCE']

plt.scatter(oce['Female_Literacy'],oce['fertility'],s = oce['population']/10000
            ,c = 'pink')

for item in oce['Country']:
    country = oce[oce['Country'] == item]
    x = country.Female_Literacy 
    y = country.fertility
    plt.text(x,y,item)