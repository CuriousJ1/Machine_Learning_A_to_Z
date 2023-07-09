# Data Preprocessing Tools

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose

# Importing the dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# print(dataset)
# print()
# print(x)
# print()
# print(y)

# Taking care of missing data
# simple imputer class needs parameters
# imputer fit parameters is the dataset values
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(x[:, 1:3])

# overrides data in x with mean values
x[:, 1:3] = imputer.transform(x[:, 1:3])

# print(x)

# Encoding Categorical data
