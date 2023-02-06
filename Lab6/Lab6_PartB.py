# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:27:00 2022

@author: fuyum
"""

import tensorflow as tf
from tensorflow import keras
fashion_mnist = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0 # normalize the pixel values to be in [0, 1]

from tensorflow.keras import datasets, layers, models
from keras.models import Sequential
import numpy as np
from keras.layers import Dropout, Flatten, Dense, Reshape
import math
"""
(1) The input layer is the flattened image, that is, a 1-dimensional vector with 𝑚 × 𝑛 elements
(2) A (Dense)compressed layer (hidden layer) with 𝑃 nodes, 𝑃 < 𝑚 × 𝑛, followed by ReLU activation
(3) An (Dense)expansion layer (hidden layer) with 𝑚 × 𝑛 × 𝑇 nodes, 𝑇 = 2 is the expansion factor, followed by
ReLU activation
(4) An output layer with 𝑚 × 𝑛 nodes, followed by Sigmoid activation
(5) A reshape layer that convert the 1-dimensional vector output to the 𝑚 × 𝑛 2-dimensional image
"""
#3 values of P: 10, 50, 200

#display the first 10 test original images
import matplotlib.pyplot as plt
for i in range(10):
    plt.imshow(x_test[i,:,:], cmap='gray')
    plt.show()
    
def psnr(P):
    model = models.Sequential()
    #1st layer, which will flatten the input image (dimension = 28 x 28 pixels) into a 1D vector (1 x 784)
    model.add(Flatten(input_shape = (28, 28)))
    #2nd layer, Compression layer, which has P number of nodes (P < 28x28), and it uses the ReLU activation function
    model.add(Dense(P, activation='relu'))
    #3rd layer, expansion layer with 28 x 28 x 2 nodes and uses ReLU activation function
    model.add(Dense(28*28*2, activation = 'relu'))
    #4th layer, output layer with 28x28 nodes, using a sigmoid activation
    model.add(Dense(28*28, activation = 'sigmoid'))
    #5th layer, reshape to convert the 1d vector back to a 28x28 2d image. 
    model.add(Reshape((28, 28)))
    
    model.summary()
    
    #training/fitting the model with our fashion_mnist data that we imported
    model.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['accuracy'] )
    #dont need the labels because not classification task
    
    model.fit(x_train, x_train, epochs = 10, batch_size = 64)

    #𝑀𝐴𝑋𝐼 = 1
    #compare the original picture with the decompressed image
    #original image= test image
    #decompressed image = what we get from model
    #use direct subtraction to get difference between original picture and decompressed image
    predicted_images = model.predict(x_test)
    #calculate mse
    
    #display the first 10 images decompressed
    for i in range(10):
        plt.imshow(predicted_images[i,:,:], cmap='gray')
        plt.show()

    PSNR_values = 0
    for x in range(len(x_test)):
        difference = x_test[x] - predicted_images[x]
        dif = difference**2
        new_sum = sum(sum(dif))
        mse = new_sum/784
        #10log10 (𝑀𝐴𝑋𝐼^2/𝑚𝑠𝑒 ),
        #peak signal to noise ratio
        PSNR = 10*math.log(1/mse, 10)
        PSNR_values += PSNR

    #average of PSNR list
    PSNR_avg = PSNR_values/len(x_test)
    return PSNR_avg

    
print(psnr(10), "\n")
print(psnr(50), "\n")
print(psnr(200), "\n")