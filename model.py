# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 21:22:44 2019

@author: Supriya
"""
#I'm still getting few errors so only couldn't give the accuracy.I have tried my level best to do it.
import pandas as pd

features = pd.read_csv('/Users/Supriya/Desktop/Adelaide.csv')
features.head(10)

print('The shape of our features is:', features.shape)
features.describe()
features = pd.get_dummies(features)
features.iloc[:,5:].head(5)

import numpy as np
labels = np.array(features['RainTomorrow_Yes'])
features= features.drop('RainTomorrow_Yes', axis = 1)
feature_list = list(features.columns)
features = np.array(features)

from sklearn.model_selection import train_test_split

train_features , test_features = train_test_split(features, test_size = 0.2)
train_labels , test_labels = train_test_split(labels, test_size = 0.2)
print(test_features)

import numpy as np

features = np.array(features)

from sklearn.model_selection import train_test_split

train_features, test_features = train_test_split(features, test_size = 0.2)

print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)

mean=[12.628368,22.945402,1.572185,5.824924,7.752002,36.530812,9.954295,15.470665,59.618476,44.820097,1018.727579,
      1016.772202,0,0,16.973193,21.603953,1.565243]
baseline_preds = test_features[:, feature_list.index('RainToday_Yes')
baseline_errors = abs(baseline_preds - test_labels)
print('Average baseline error: ', round(np.mean(baseline_errors), 2))

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)

rf.fit(train_features, train_labels);

predictions = rf.predict(test_features)

errors = abs(predictions - test_labels)

print('Mean Absolute Error:', round(np.mean(errors), 2))

mape = 100 * (errors / test_labels)

accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')
