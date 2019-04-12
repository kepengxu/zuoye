import time
print(time.time())
print(time.mktime(time.localtime()))
s=time.strftime("%Y-%m-%d %X",time.localtime())
print(s)
# from keras.applications import NASNetLarge,InceptionResNetV2,DenseNet201,NASNetMobile
# model=NASNetLarge(include_top=False,pooling='avg')
# model=InceptionResNetV2(include_top=False,pooling='avg')
# model=DenseNet201(include_top=False,pooling='avg')
# model=NASNetMobile(include_top=False,pooling='avg')
# from keras.models import Model
# x=Model()
# model