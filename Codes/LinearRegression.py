#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:41:11 2023

@author: eduardolopez

This code fits a linear regression model to predict GSTOTCST (annual gas cost)
"""



import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LogisticRegression

# here we load the data
file_path = Path("/Users/eduardolopez/downloads/csv/vehpub.csv")
wwc = pd.read_csv(file_path)


# Select relevant features, we want to pick top 10 features logically, there are robust methods too, you select logically. 
labels_names = ['GSYRGAL', 'FEGEMPG', 'ANNMILES', 'OD_READ', 'VEHAGE', 'HHVEHCNT', 'HHSIZE', 'GSTOTCST']
wwc = wwc[labels_names]

# Make all values greater than 0, now we make all values in the selected >0
wwc = wwc.clip(lower=0)


# Split data into training and testing sets
X = wwc.drop('GSTOTCST', axis=1) 
y = wwc['GSTOTCST'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#  linear regression 
regr = linear_model.LinearRegression()

# logistic regression
logreg = LogisticRegression()

# Train using training sets
regr.fit(X_train, y_train)
logreg.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(X_test)
y2_pred = logreg.predict(X_test)
# The coefficients
print("Coefficients: \n", regr.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

# Plot actual vs predicted values
plt.scatter(y_test, y_pred)


plt.xlabel("Actual values")
plt.ylabel("Predicted values")
plt.xlim(0,15000)
plt.ylim(0,15000)
plt.plot([0, y_test.max()], [0, y_test.max()], '--', color='blue')
plt.show()

