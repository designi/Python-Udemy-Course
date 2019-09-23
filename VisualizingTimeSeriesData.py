# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:35:52 2019

@author: ngarcia

https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.plot.html
"""
import numpy as np
import pandas as pd
import matplotlib
import logging
from matplotlib import dates
from datetime import datetime
from numpy.random import randn

np.random.seed(101)
rand_mat = randn(5,4)
print(rand_mat)

df = pd.DataFrame(data=rand_mat,index='A B C D E'.split())
df = pd.DataFrame(data=rand_mat,index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)
print(' ')
print(df['Y'])

mylist = ['W','Y']
print(df[mylist])


df['NEW'] = df['W']+df['Y']

print(df)


df.drop('NEW',axis=1,inplace=True) #inplace drops the column once called


print(df.loc['A'])


df = pd.DataFrame({'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]})

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})



df1 = pd.read_csv('C:\\Users\\ngarcia\\Desktop\\UDEMY-TSA-FINAL\\UDEMY_TSA_FINAL\\Data\\df1.csv',index_col=0)
df2 = pd.read_csv('C:\\Users\\ngarcia\\Desktop\\UDEMY-TSA-FINAL\\UDEMY_TSA_FINAL\\Data\\df2.csv')
#df3 = pd.read_csv('C:\\Users\\ngarcia\\Desktop\\df1.csv',index_col=0)

#df1['A'].plot.hist(edgecolor='k')
df1['A'].plot.hist(bins=20,grid=True)

df2.plot.bar()

#Formatting plots
title = 'MY PLOT TITLE'
xlabel = 'MY X DATA'
ylabel = 'MY Y LABEL'
ax = df2['c'].plot.line(figsize=(10,3),ls=':',c='red',lw=5,title=title)
ax.set(xlabel=xlabel,ylabel=ylabel)
ax = df2.plot()
#ax.legend(loc=0,bbox_to_anchor(2.0,1.0))


#Vizualization practice -> Create custom plots
try:
    df3 = pd.read_csv('C:\\Users\\ngarcia\\Desktop\\UDEMY-TSA-FINAL\\UDEMY_TSA_FINAL\\Data\\df3.csv')
    xlib = 'Produced'
    ylib = 'Defective'
    df3.plot(x='produced',y='defective',kind='scatter', title = 'produced vs defective',
             color='red',figsize=(15, 4))
except FileNotFoundError:
    logging.critical('The file does not exist \n Double check your file path')


#Create hitogram of produced
df3 = pd.read_csv('C:\\Users\\ngarcia\\Desktop\\UDEMY-TSA-FINAL\\UDEMY_TSA_FINAL\\Data\\df3.csv')
df3['produced'].plot(kind='hist',x='produced',figsize =(5,5),color='blue',edgecolor='white',bins=20,legend=(1)).autoscale(tight=True)


df3.groupby('weekday').mean().transpose().plot(kind='box',yticks=list(range(0,100,20)),title='produced for each weekday')
df3[['produced','weekday']].boxplot(by='weekday',grid=False)

df = pd.read_csv('C:\\Users\\ngarcia\\Desktop\\UDEMY-TSA-FINAL\\UDEMY_TSA_FINAL\\Data\\starbucks.csv',index_col='Date',parse_dates=True)
df.index
#daily --> yearly
df.resample(rule='A').mean()

df['Rolling_Mean'] = df['Close'].rolling(window=50).mean()
df[['Close','Rolling_Mean']].plot(kind='line',title='moving average plot of starbucks stock price')

#various ways to plot subsets of data
df['Close']['2017-01-01':'2017-12-31'].plot(figsize=(12,4))
df['Close'].plot(figsize=(12,4),xlim=['2017-01-01','2017-12-31'])
ax = df['Close']['2017-01-01':'2017-12-31'].plot(figsize=(12,4),ylim=(40,70),ls='--',c='red')
ax.set(xlabel='')
#specific to matplotlib --> Various ways to customize graphical output
#ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=0))
#ax.xaxis.set_major_formatter(dates.DateFormatter('%a-%B-%d'))
#ax.xaxis.set_minor_locator(dates.MonthLocator())
#ax.xaxis.set_minor_formatter(dates.DateFormatter('\n\n%b'))
#ax.yaxis.grid(True)
#ax.xaxis.grid(True)

try:
    df4 = pd.read_csv('C:\\Users\\ngarcia\\Desktop\\UDEMY-TSA-FINAL\\UDEMY_TSA_FINAL\\Data\\monthly_milk_production.csv', encoding='utf8')
    df4title = "Monthly milk production: pounds per cow. Jan '62 - Dec '75"
except FileNotFoundError:
    logging.critical('The file does not exist \n Double check your file path')

print(df4['Date'].head()) #get date data header
print(df4['Date'].dtype) #get date datatype
df4['Date'] = pd.to_datetime(df4['Date']) #set the date column to a datetime datatype
df4.set_index('Date',drop=True,inplace=True) #set the index to be the date column

df4plot = df4.plot(title=df4title)
df4['Month'] = df4.index.month #get month number
df4['Month'] = df4.index.strftime("%B") #get month name
df4['Month_Number'] = df4.index.month
df4_boxplot = df4.boxplot(by='Month_Number',figsize=(8,8),grid=False)
df4_boxplot.set_xlabel('Month')
df4_boxplot.set_ylabel('Production')
df4_boxplot.axes.set_title('Boxplot Production grouped by Month')



