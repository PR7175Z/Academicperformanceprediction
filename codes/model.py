import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# reading data file
data = pd.read_csv('../data/data.csv')
display(data.head())

length = len(data)
Parental_Support = np.array([
    0 if data['Parental Support'][i] == 'Low' 
    else 1 if data['Parental Support'][i] == 'Medium'
    else 2
    for i in range(length)
])

data['Parental Support Numeric'] = Parental_Support
print(data.head())


features = np.array(
    [
    'Parental Support Numeric',
    'Previous Grade',
    'Study Hours Per Week',
    'Extracurricular Activities',
    'Attendance Rate',
]
)
target = np.array(['Final Grade'])

x = data[features]
print(x.head())

y = data[target]
print(y.head())

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.2,random_state= None)
#random_state = None gives Random data split everytime executed

print(x_train.head())
print(y_train.head())

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

with open('../data/model45.pkl','wb') as f:
    pickle.dump(model,f)