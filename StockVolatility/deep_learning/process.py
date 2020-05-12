# imports
import numpy
import matplotlib.pyplot as plt
import pandas
import math



#@title Data preparation

def transform_data(df, features, targets, look_back = 0, look_forward = 1, split_ratio = 0.7):
  """transform the data in a custom form.

  :param: df, pd.DataFram, the data, 
    e.g. df = pd.read_excel("USMacroData.xls", "All")
  :param: features, list of strs, the features to be uses as the source features,
     e.g. ["Wage", "Consumption"]
  :param: look_back, int, number of days to look back in historic data,
     e.g. look_back = 11 means we use the last (11+1)=12 months' data to predict the future
  :param:look_forward, int, num of days to look forward
    e.g. look_forward = 3 means we want to predict next 3 months' data
  :param: split_ratio, float, split the data into training dataset and testing dataset by this ratio
    e.g. split_ratio=0.7 means we use the first 70% of the data as training data, the last 30% as the testing dataset
  :rtype: np.arrays, x_train, y_train, x_test, y_test
  """
  x, y = [], []
  for i in range(look_back, len(df) - look_forward):
      assert look_back < len(df)-look_forward, "Invalid look_back, look_forward values"
      
      x.append(np.array(df[i-look_back : i+1][features]))
      y.append(np.array(df[i+1: i+look_forward+1][targets]).transpose())

  # List to np.arrary
  x_arr = np.array(x)
  y_arr = np.array(y)

  split_point = int(len(x)*split_ratio)

  return x_arr[0:split_point], y_arr[0:split_point], x_arr[split_point:], y_arr[split_point:]

features = ["a","b", "c", "e", "f"]
targets = ["a"]
x_train, y_train, x_test, y_test = transform_data(new_sigma, features=features, targets = targets, look_back = 0, look_forward=1, split_ratio=0.7)

#Note that all returned np.arrays are three dimensional.
#Need to reshape y_train and y_test to fit the LSTM

# For the basic model only
y_train = np.reshape(y_train, (y_train.shape[0], -1))
y_test = np.reshape(y_test, (y_test.shape[0], -1))









