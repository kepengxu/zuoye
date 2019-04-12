#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from tfrbm import BBRBM
from tqdm import tqdm
from keras.utils import conv_utils
from keras.backend.common import normalize_data_format
from tensorflow.examples.tutorials.mnist import input_data
import cv2
from keras.layers import Conv2D,Input,UpSampling2D,pooling,MaxPooling2D,Dropout,concatenate
from keras.models import Model
from keras.engine import Layer,InputSpec
import os
import keras
import tensorflow as tf
from keras.callbacks import TensorBoard
from keras.losses import sparse_categorical_crossentropy
import keras.backend as K
h,w=914//8,990//8
def get_data(dir):
    Images=[]
    l=os.listdir(dir)
    for i in tqdm(l):
        imagepath=os.path.join(dir,i)
        image=cv2.imread(imagepath,cv2.IMREAD_GRAYSCALE)
        image=cv2.resize(image,(w,h))
        image=image>80
        image=np.array(image*1,np.uint8)
        Images = np.reshape(image, [-1])
        # cv2.imshow('image',image)
        # cv2.waitKey(0)
        Images.append(image)

    Images=np.array(Images,np.int64)

    print(Images.shape)
    print(Images.dtype)
    # Images=Images[:,:,:,np.newaxis]
    return Images


if __name__=='__main__':
    Images=get_data('/home/cooper/PycharmProjects/zuoye/math_theory_work/作业2/images')
    mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
    mnist_images = mnist.train.images

    bbrbm = BBRBM(n_visible=914*990/4, n_hidden=500, learning_rate=0.001, momentum=0.95, use_tqdm=True)
    errs = bbrbm.fit(Images, n_epoches=30, batch_size=10)
    plt.plot(errs)
    # plt.show()
    # model=Get_model()
    # model.compile(optimizer='sgd',loss=sparse_categorical_crossentropy,metrics=['accuracy'])
    # model.fit(Images,Images,batch_size=1,epochs=10,validation_split=0.2,callbacks=[TensorBoard('/home/cooper/PycharmProjects/zuoye/math_theory_work/logs')])
    #
