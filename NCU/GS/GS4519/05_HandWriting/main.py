from tensorflow.keras.datasets import mnist
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image as imageUtilities
import PIL.ImageOps

(x_train, y_train), (x_valid,y_valid) = mnist.load_data()

plt.imshow(x_train[0], cmap='gray')
y_train[0]

# we made the data from 2-D to 1-D even to 0~1.
x_train_1D = x_train.reshape(60000,784)
x_valid_1D = x_valid.reshape(10000,784)

x_train_1D.min()

x_train_1D_normal = x_train_1D/255
x_train_1D_normal.min()
x_valid_1D_normal = x_valid_1D/255

num_categories = 10
y_train.min()

y_train_category = keras.utils.to_categorical(y_train, num_categories)
y_valid_category = keras.utils.to_categorical(y_valid, num_categories)
y_train_category[0] # 測試看看

# Building model
model = Sequential()
model.add(Dense(units=512, activation='relu', input_shape=(784, )))
model.add(Dense(units=512, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', metrics=['accuracy'])
# throw to verify data, verify pre-result data to fix the model
model.fit(x_train_1D_normal, y_train_category, epochs=10, verbose=1, validation_data=(x_valid_1D_normal, y_valid_category)) 

# epochs : we normally set 10~20

model.predict(x_valid_1D_normal[0])
model.predict([x_valid_1D_normal[0]])
model.predict(np.array(x_valid_1D_normal[0]))
# Data type is wrong.
model.predict(np.array([x_valid_1D_normal[0]])) #we final have the result
np.argmax(model.predict(np.array([x_valid_1D_normal[0]])))
plt.imshow(x_valid[0], cmap='gray')


# This function can test our own image.
def predict_number(image_path):
    if "http" in image_path:
        image_path = keras.utils.get_file(origin=image_path)
    test_image = imageUtilities.load_img(image_path, color_mode='grayscale', target_size=(28,28))
    test_image_inverted  = PIL.ImageOps.invert(test_image)
    f, axarr = plt.subplots(1,2)
    axarr[0].imshow(test_image, cmap='gray')
    axarr[1].imshow(test_image_inverted, cmap='gray')

    test_image_array = imageUtilities.img_to_array(test_image_inverted)
    test_image_array_1D = test_image_array.reshape(1,784)
    test_image_array_1D_normal = test_image_array_1D/255
    return  np.argmax(model.predict(test_image_array_1D_normal))


# Model import and export
model.save("basic-nn-model")
model_from_cloud = keras.models.load_model("nmist-nn-model-20220512")

# 後續可以食做成網頁，也可以有個繪圖板供使用者測試