from sklearn import svm
import pandas as pd

model=svm.SVC()

dataset=pd.read_csv('titanic.csv', index_col='PassengerID')

dataset_no_NA = dataset[['Survived', 'PClass', 'Age', 'SexCode']].dropna()
dataset_no_NA['PClass'] = dataset_no_NA['PClass'].str.slice(0,1)

X_train = dataset_no_NA[['PClass', 'SexCode', 'Age']]
y_train = dataset_no_NA['Survived']

model.fit(X_train,y_train)
predicted=model.predict(X_train[:10])

y_test=y_train[:10]
print('predskazanya seti')
print(predicted)
print('\ncorrect answers')
print(y_test)