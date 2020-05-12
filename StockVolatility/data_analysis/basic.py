#@title ```basic.py```

#import numpy, pandas and matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


#Basic checks: find null values, set index, etc.

def basic_check(df, index_name="day"):
  """Find the null values and set index of a given DataFrame.
  :param: df, pd.DataFrame, the data, e.g. df = pd.read_csv("stockdata3.csv")
  :param: index_name, str, name of the index, must be one of the column names, e.g. index_name ="day"
  :rtype: pd.DataFrame
  """
  df.set_index(index_name, inplace=True)
  df.index = pd.to_datetime(df.index,unit='D')

  #check for null entries
  print("Null values summary:\n")
  print(df.isnull().sum())

  return df

def plot_column(df, feature):
    """Plot the resampled column of df, e.g. plot_column(df, "a") plots the "a" column
    
    :param: df, pandas.DataFrame, the data, e.g. df = pd.read_csv("stockdata3")
    :param: feature, str, name of column to be plotted. 
    """
    y = df[feature]
    y.plot(figsize=(28, 8))
    plt.xlabel('Minute number')
    plt.ylabel("Stock "+feature)
    plt.show()

def day_check(df, column_name = "day"):
  for ii in df['day'].unique():
    if(len(df[df['day']==ii])!=391):
      print("Day "+str(ii)+" has "+str(len(df[df['day']==ii]))+" minutes data!")
      print(df[df['day']==ii].tail())


def date_check(df):
  for date in df.index.unique():
    if(len(df[df.index==date])!=391):
      print("Day "+str(date)+" has "+str(len(df[df.index==date]))+" minutes data!")
      print(df[df.index==date].tail())
