import pickle
import cv2
from sklearn import neighbors
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
from tensorflow.keras.layers import GlobalMaxPooling2D
from numpy.linalg import norm
from sklearn.neighbors import NearestNeighbors

feature_list=pickle.load(open('embeddings.pkl','rb'))

#print(np.array(feature_list).shape)
#print(np.array(feature_list))


filenames=pickle.load(open('filenames.pkl','rb'))


model=ResNet50(weights='imagenet',include_top=False,input_shape=(224,224,3))
model.trainable=False
model=tf.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])


img=image.load_img('1164.jpg',target_size=(224,224))
img_array=image.img_to_array(img)
img_array=img_array.reshape(1,224,224,3)
preprocessed_img=preprocess_input(img_array)
result=model.predict(preprocessed_img).flatten()
normalized_result=result/norm(result)


neighbors=NearestNeighbors(n_neighbors=5,algorithm='brute',metric='euclidean')
neighbors.fit(feature_list)
distances,indices=neighbors.kneighbors([normalized_result])
print(indices)
print(distances)

for i in indices[0]:
    print(filenames[i])
    temp_img=cv2.imread(filenames[i])
    cv2.imshow('output',cv2.resize(temp_img,(240,240)))
    cv2.waitKey(0)