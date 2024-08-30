# This file is to be used to train the model 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import pickle

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

# reading data file
try:
    data = pd.read_csv('../data/data.csv')
except Exception as e:
    print(e)

display(data.head())

length = len(data)

# convert string data to numeric values
Parental_Support = np.array([
    0 if data['Parental Support'][i] == 'Low' 
    else 1 if data['Parental Support'][i] == 'Medium'
    else 2
    for i in range(length)
])
# add the converted data with other array
data['Parental Support Numeric'] = Parental_Support
print(f'Data Head: \n{data.head()}')


# classifying features 
features = np.array(
    [
    'Parental Support Numeric',
    'Previous Grade',
    'Study Hours Per Week',
    'Extracurricular Activities',
    'Attendance Rate',
]
)
# classifying target
target = np.array(['Final Grade'])


# assigning x and y terms
x = data[features]
print(f'X Head:\n{x.head()}')
y = data[target]
print(f'Y Head:\n{y.head()}')


# spliting the data into train and test category
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.2,random_state= None)#random_state = None gives Random data split everytime executed
print(f'X Train Head:\n{x_train.head()}\nY Train Head:\n{y_train.head()}')


# creating model
model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)


# orignal values
o_mse = mean_squared_error(y_test,y_pred)
o_r2 = r2_score(y_test,y_pred)
o_score = model.score(x_test,y_test)


# saving the created model
try: # if model.pkl file already exists
    with open('../models/model.pkl','rb') as f:
        loaded_data = pickle.load(f)

        # loaded values
        y_load = loaded_data.predict(x_test)
        l_mse = mean_squared_error(y_test,y_load)
        l_r2 = r2_score(y_test,y_load)
        l_score = loaded_data.score(x_test,y_test)

        print(f'Mean Square Error:\n(Original):{o_mse}, (Loaded){l_mse}')
        print(f'R2 Score:\n(Original):{o_r2}, (Loaded){l_r2}')
        print(f'Score:\n(Original):{o_score}, (Loaded){l_score}')

        if(l_r2 > o_r2):# replaces file only if better score is achieved
            with open('../models/model.pkl','wb') as f:
                pickle.dump(model,f)
except Exception as e: # if model.pkl file doesnot exists exists
    print(e)
    with open('../models/model.pkl','wb') as f:
        pickle.dump(model,f)
    
    print(f'Mean Square Error:{o_mse}')
    print(f'R2 Score:{o_r2}')
    print(f'Score:{o_score}')