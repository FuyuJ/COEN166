# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:16:33 2022

@author: fuyum
"""

import tensorflow as tf
from tensorflow import keras 
fashion_mnist = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

'''
1.a Select one image from each class of the dataset to display as a gray-scale image.
'''
import matplotlib.pyplot as plt
for i in range(10):
    plt.imshow(x_train[i,:,:], cmap='gray')
    plt.show()

# normalize the pixel values to be in [0, 1]
x_train, x_test = x_train / 255.0, x_test / 255.0 
# note: you need to flatten the image to a vector, to serve as the input layer of the network.

# code to be implemented …
"""
Build a two-layer neural network for image recognition with the fashion MNIST data set.
The network has one hidden layer, and an output layer. 
The hidden layer has 512 nodes, and adopts the ReLU activation function; 
the output layer has 10 nodes, and adopts the softmax activation function to output the class probabilities. 
Use the “sparse_categorical_crossentropy” loss function, use ‘adam’ as the optimizer, 
use a batch size of 32, and train your model for 5 epochs. 
"""
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from sklearn import metrics
import numpy as np

#create model
model = Sequential()
#1st layer, flatten input image (28x28 image) into a 1D vector (1x784)
model.add(Flatten(input_shape = (28, 28)))
#2nd layer, hidden layer with 512 nodes and ReLU activation function
model.add(Dense(512, activation = 'relu'))
#3rd layer, output layer with 10 nodes and softmax activation function to output the class probabilities
model.add(Dense(10, activation = 'softmax'))
model.summary()
#train/fit model
model.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam',  metrics = ['accuracy'])
model.fit(x_train, y_train, epochs = 5, batch_size = 32)
'''
1.b Give the recognition accuracy rate of the test set, and show the confusion matrix
'''
#Testing accuracy
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Accuracy Rate = ", test_acc)

predicted_probability = model.predict(x_test)
y_test_hat = np.argmax(predicted_probability, axis=1)

#generate confusion matrix 
#diagonal elements represent the number of elements that were predicted correctly
#vertical = ground truth labels
#horizontal = predicted categories
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test, y_test_hat, labels=range(10))
print("Confusion Matrix:")
print(cm)

