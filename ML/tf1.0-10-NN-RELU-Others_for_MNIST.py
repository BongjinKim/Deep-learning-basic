import tensorflow as tf
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
#print(x_train.shape, y_train.shape)
#imshow(img, cmap=color(gray_r : 회색 reverse))
plt.imshow(x_train[0], cmap=plt.cm.gray_r)
'''
reshape으로 (28,28) to 784 바꿈
normalization 데이터 전처리 위해 0~1사이의 값으로 바꿈
데이터의 값은 0~255 값 이기 때문에, 255를 나누어줌
'''
x_train = x_train.reshape(60000, 784).astype("float32") / 255
x_test = x_test.reshape(10000, 784).astype("float32") / 255

#one_hot_encoding
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

'''
모델 생성 및 학습
1. softmax classifier 단일모델 학습

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=10, input_dim=784,  activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer=tf.optimizers.Adam(lr=0.01), metrics=['accuracy'])
model.summary()
val_loss: 0.3147 - val_accuracy: 0.9174

2. NN for MNIST
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=256, input_dim=784,  activation='relu'))
model.add(tf.keras.layers.Dense(units=256, input_dim=256,  activation='relu'))
model.add(tf.keras.layers.Dense(units=10, input_dim=256,  activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer=tf.optimizers.Adam(lr=0.01), metrics=['accuracy'])
model.summary()

val_loss: 0.1503 - val_accuracy: 0.9682

3. Xavier for MNIST
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=256, input_dim=784, activation='relu', kernel_initializer ='glorot_normal'))
model.add(tf.keras.layers.Dense(units=256, input_dim=256, activation='relu', kernel_initializer ='glorot_normal'))
model.add(tf.keras.layers.Dense(units=10, input_dim=256, activation='softmax', kernel_initializer ='glorot_normal'))
model.compile(loss='categorical_crossentropy', optimizer=tf.optimizers.Adam(lr=0.01), metrics=['accuracy'])
model.summary()

val_loss: 0.1507 - val_accuracy: 0.9717

4. Dropout
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=256, input_dim=784, activation='relu', kernel_initializer ='glorot_normal'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(units=256, input_dim=256, activation='relu', kernel_initializer ='glorot_normal'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(units=10, input_dim=256, activation='softmax', kernel_initializer ='glorot_normal'))
model.compile(loss='categorical_crossentropy', optimizer=tf.optimizers.Adam(lr=0.001), metrics=['accuracy'])
model.summary()

val_loss: 0.0666 - val_accuracy: 0.9798
'''
#model test
model.fit(x_train, y_train, batch_size=100, epochs=10, validation_data=(x_test, y_test))
