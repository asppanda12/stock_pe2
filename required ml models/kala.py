
import pandas as pdr
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
df=pdr.read_csv("BPCL.csv")
import tensorflow as tf
df2=df.reset_index()['Close']

scaler=MinMaxScaler(feature_range=(0,1))
df2=scaler.fit_transform(np.array(df2).reshape(-1,1))


training_size=int(len(df2)*0.65)
test_size=len(df2)-training_size
train_data,test_data=df2[0:training_size],df2[training_size:len(df2),:1]

import numpy
def create_dataSet(dataset,time_stramp=1):
    data_x,data_y=[],[]
    for i in range(len(dataset)-time_stramp-1):
        a=dataset[i:(i+time_stramp),0]
        data_x.append(a)
        data_y.append(dataset[i+time_stramp,0])
    return numpy.array(data_x),numpy.array(data_y)


time_stramp=100
x_train,y_train=create_dataSet(train_data,time_stramp)
x_test,y_test=create_dataSet(test_data,time_stramp)



x_train=x_train.reshape(x_train.shape[0],x_train.shape[1],1)
x_test=x_test.reshape(x_test.shape[0],x_test.shape[1],1)

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

from keras.models import load_model
model=load_model('BPCL.h5')

import tensorflow as tf
train_predict=model.predict(x_train)
test_predict=model.predict(x_test)

train_predict=scaler.inverse_transform(train_predict)
test_predict=scaler.inverse_transform(test_predict)
import math
from sklearn.metrics import mean_squared_error
skt=math.sqrt(mean_squared_error(y_train,train_predict))
print(skt)
print(math.sqrt(mean_squared_error(y_test,test_predict)))


x_input=test_data[1758:].reshape(1,-1)

temp_input=list(x_input)
temp_input=temp_input[0].tolist()
from numpy import array

lst_output=[]
n_steps=100
i=0

while(True):
    
    if(len(temp_input)>100):
        #print(temp_input)
        x_input=np.array(temp_input[1:])
        # print("{} day input {}".format(i,x_input))
        x_input=x_input.reshape(1,-1)
        x_input = x_input.reshape((1, n_steps, 1))
        #print(x_input)
        yhat = model.predict(x_input, verbose=0)
        # print("{} day output {}".format(i,yhat))
        temp_input.extend(yhat[0].tolist())
        temp_input=temp_input[1:]
        #print(temp_input)
        lst_output.extend(yhat.tolist())
        i=i+1
    else:
        x_input = x_input.reshape((1, n_steps,1))
        yhat = model.predict(x_input, verbose=0)
        # print(yhat[0])
        temp_input.extend(yhat[0].tolist())
        # print(len(temp_input))
        lst_output.extend(yhat.tolist())
        i=i+1