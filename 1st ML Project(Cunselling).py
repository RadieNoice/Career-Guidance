# -*- coding: utf-8 -*-
"""Copy of Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IsiJSHyoDUOn61Bo3KnD0to7nEO4FHpp
"""

#Importing Library
import pandas as pd #For data interpretation
import sklearn #for machine learning
from sklearn.model_selection import train_test_split #To segregate the given data to train and test data where the
                                                     #train data is use to feed the model so that it could learn
                                                      #and it could implement it on the test data
from sklearn.tree import DecisionTreeClassifier#ai algorithm
from sklearn.metrics import accuracy_score#to check the accuracy of the predciton with train data on test data
from sklearn.preprocessing import LabelEncoder#to encode the letters(data) to numbers so that it would
                                               #be feasible for the algorithm to process

data=('/content/lwriuhguie.csv')
p_data=pd.read_csv(data)#to convert the csv file into data structure
columns=p_data.columns#to get the columns present in the data which is in array
columns=columns.tolist()#to convert the array to list data type
target=columns[-1]#to get the target column
columns.pop()#to remove the target column so that it would be convinient to fro the algorithm to feed i the data
print(p_data.head())#example
print(columns)#to show the columns excluded of the target column

z=p_data[target].unique()#to get the unique values present in the data
z=z.tolist()#similar to previous one
z.sort()#sorting the unique system in order
l=[]
for i in columns:
  l.append((p_data[i].unique()).tolist()) # to sort the unique values of each column for eazy mapping of the predicted targeted value
print(l)
for i in l:
  i.sort()
print(l)
print(z)
columns

e=LabelEncoder()#to encode the data based on alphabetical order
for i in columns:
  p_data[i]=e.fit_transform(p_data[i])#to encode each and every column using for loop and feeding it to the algorithm
p_data[target]=e.fit_transform(p_data[target])#to feed or fit the targeted value
p_data.head()

x=p_data.drop(target,axis=1)#the x data which is the data from which the machine learns
y=p_data[target]#to get the y column which is targeted data

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=56)#splitting 90% for training and 10% for testing to predicts its accuracy
c=DecisionTreeClassifier(criterion='entropy',max_depth=20)#now feeding thos datas and applying the parameters for proper classification of data
c.fit(x_train,y_train)#fitting or feeding the data to the algoeithm
y_pred=c.predict(x_test)#now predicting the targeted value from the learned data
accuracy=accuracy_score(y_test,y_pred)#testing its accuracy with with the real data and the predicted one
print(f'Accuracy:{accuracy*100:.2f}')

num_rows=int(input('Enter The Number of Rows ')) #to create a quiz like question patterns to analize the users intrest and predicing its career
d=[]
for i in range(num_rows):
  rd=[]
  a=0
  while a<=len(columns)-1:
    if a==0:
      m=eval(input(f'{columns[a]}: '))
      l[a].append(m)
      l[a].sort()
      rd.append(l[a].index(m))
      a+=1

    elif a<=len(columns)-1:
      def fn (b):
        global a
        n=input(f'{columns[a]}: ')
        if n in l[a]:
          rd.append(l[a].index(n))
          a+=1
        else:
          j='pls use these only: '
          for i in l[a]:
            j=j+' '+i
          print(j)
      fn(a)
    d.append(rd)
t=pd.DataFrame(d,columns=columns)#converting the obtained data which is the test data like the previous one and convering it to a dataframe predicting

t_label=p_data[target]#to label the values in the targeted column
c=DecisionTreeClassifier(criterion='entropy',max_depth=20)#similar to the privious ons instead of verifing we are actually predicting now
c.fit(x_train,y_train)#fitting and feeding the data
y_pred=c.predict(t)#to predict the targeted value with the learned data
y_pred=y_pred.tolist()#to convert it from array to list data type
y=0
for i in y_pred:#getting the enoded index for the targeted value
  y=i
print(y)

print(z[y])#predicting the targeted value