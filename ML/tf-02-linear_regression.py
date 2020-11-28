#numpy는 array연산의 표준으로 for 없이 연산 가능
import numpy as np
import tensorflow as tf

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

tf.model = tf.keras.Sequential()
# units = output shape, input_dim = input shape
tf.model.add(tf.keras.layers.Dense(units=1, input_dim=1))

#tf 2.0 version gradientDescent
#tf 2.0에서는 함수형 api 사용을 권장함
sgd = tf.keras.optimizers.SGD(lr=0.1)  # SGD = standard gradient descendent, lr = learning rate
tf.model.compile(loss='mse', optimizer=sgd)  # mse = mean_squared_error, After computing the squared distance between the inputs, the mean value over the last dimension is returned.
loss = mean(square(y_true - y_pred), axis=-1)

# prints summary of the model to the terminal
tf.model.summary()

# fit() = tf 1.0 train + for
tf.model.fit(x, y, epochs=200)

# predict() returns predicted value
y_predict = tf.model.predict(np.array([5, 6, 7, 8, 9]))
print(y_predict)
