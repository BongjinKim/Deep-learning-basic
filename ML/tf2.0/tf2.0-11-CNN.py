#tensorfolw 2.0
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

#dataset load
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

#dataset reshape를 통해 input 사이즈 조절 (60000, 28, 28) => (60000, 28, 28, 1), (개수, Width, Height, Color)
train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))

#픽셀값 Normalization
train_images, test_images = train_images / 255.0, test_images / 255.0

#Model 생성, 3 convolutional layer and 2 maxpooling
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

#여러갈래의 input을 하나로 flatten 후 fully connected nn
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

#model 현황 요약, 간단한 모델은 굳이 tensorboard보단 summary만으로도 괜찮은듯
model.summary()

#adam optimizer, sparse_categorical_crossentropy : integer type으로 onehot 불필요, metrics 지표는 확률로
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#epoch : 5번 전체 이미지 학습
model.fit(train_images, train_labels, epochs=5)

#fit된 model을 가지고 test
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print(test_acc)

'''
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
conv2d_21 (Conv2D)           (None, 26, 26, 32)        320
_________________________________________________________________
max_pooling2d_15 (MaxPooling (None, 13, 13, 32)        0
_________________________________________________________________
conv2d_22 (Conv2D)           (None, 11, 11, 64)        18496
_________________________________________________________________
max_pooling2d_16 (MaxPooling (None, 5, 5, 64)          0
_________________________________________________________________
conv2d_23 (Conv2D)           (None, 3, 3, 64)          36928
_________________________________________________________________
flatten_7 (Flatten)          (None, 576)               0
_________________________________________________________________
dense_14 (Dense)             (None, 64)                36928
_________________________________________________________________
dense_15 (Dense)             (None, 10)                650
=================================================================
Total params: 93,322
Trainable params: 93,322
Non-trainable params: 0
_________________________________________________________________
Epoch 1/5
1875/1875 [==============================] - 20s 10ms/step - loss: 0.1467 - accuracy: 0.9549
Epoch 2/5
1875/1875 [==============================] - 19s 10ms/step - loss: 0.0460 - accuracy: 0.9857
Epoch 3/5
1875/1875 [==============================] - 19s 10ms/step - loss: 0.0331 - accuracy: 0.9895
Epoch 4/5
1875/1875 [==============================] - 19s 10ms/step - loss: 0.0258 - accuracy: 0.9923
Epoch 5/5
1875/1875 [==============================] - 19s 10ms/step - loss: 0.0208 - accuracy: 0.9933
313/313 - 1s - loss: 0.0282 - accuracy: 0.9917
0.9916999936103821
'''
