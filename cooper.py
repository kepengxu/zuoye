# coding:utf-8

import numpy as np


import keras
from keras.optimizers import sgd
sgd=sgd(0.01)
from keras.models import Sequential
from keras.layers import *
def get_model(l,inputshape=3):
    model = Sequential()

    model.add(Dense(5,input_dim=inputshape))
    for i in l:
        model.add(Dense(i,activation='relu'))
    model.add(Dense(2))
    model.compile(loss='mean_squared_error', optimizer=sgd)
    return model




def Get_Data(path):

    data=[]
    with open(path) as f:
        for line in f:
            line=line[:-1]
            words=line.split(',')
    #        print words
            tl=[float(n) for n in words]
            data.append(tl)
    Data=np.array(data,np.float)
    Data[:,0]=Data[:,0]/100.0
    Data[:,3]=Data[:,3]/10000.0
    Data[:,4]=Data[:,4]/10000.0
    x=Data[:,:3]
    y=Data[:,3:]
    return x,y


path= '/home/cooper/下载/biao.csv'
x,y=Get_Data(path)
ll=[4,8,16,32,64,32,16,8]
model=get_model(ll)
model.fit(x,y,batch_size=20,nb_epoch=10000)
da=[[0.7339,3.9635,0.9880],[0.7555,4.0975,1.0268]]
model.save('model.hdf5')
da=np.array(da,np.float)
pre=model.predict(da,2,1)
for p in pre:
    print p*10000.0

