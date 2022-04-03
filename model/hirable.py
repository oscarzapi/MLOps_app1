# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# importing libraries

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report
import pickle


#importing Dataset

dataset = pd.read_csv('hirable.csv')

# Cleaning up Dataset

dataset = dataset.drop([
"sl_no",
"ssc_p",
"ssc_b",
"hsc_p",
"hsc_b",
"hsc_s",
"specialisation",
"salary",
"degree_t"
], axis=1)


# Featurization

dataset = dataset.rename(columns = {'degree_p': 'bsc', 'mba_p': 'msc'})

dataset['gender'] = dataset.gender.replace(['M', 'F'], [1, 2])

dataset['workex'] = dataset.workex.replace(['Yes', 'No'], [1, 0])

dataset['status'] = dataset.status.replace(['Placed', 'Not Placed'], [1, 0])

# Downscalling Method For BSc & MSc grades

def downscale(score):
    return score/10/2

degrees = ['bsc', 'msc']

for col in degrees:
    dataset[col] = downscale(dataset[col])

# Separating into dependent and independent variables
X = dataset.drop(['status'], axis=1)
y = dataset.status

# Splitting dataset into trainig and testing

X_train, X_test, y_train, y_test = train_test_split(X, y,train_size=0.8,random_state=1)

# Fitting with random forest model

model=RandomForestClassifier(n_estimators=100)
model.fit(X_train,y_train)

# Prediction and testing
y_pred=model.predict(X_test)


# Report and Accuracy Score

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Classification Report RF:\n",classification_report(y_test,y_pred))

# Model testing on new data
# [[gender, bsc, workex, etest_p, msc]]

######### WRITE THE FOLLOWING CODE IN THE CONSOLE TO TEST THE MODEL ########

# Sample 1
#sample1 = np.array([[0, 2.9, 1, 78.50, 3.7]])
#model.predict(sample1)

# Sample 2
#sample = np.array([[1, 3.9, 0, 78.5, 3.7]])
#model.predict(sample)

######### ################################################### ########

# Saving model
pickle.dump(model, open('hireable.pkl', 'wb'))

