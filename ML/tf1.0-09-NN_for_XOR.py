import tensorflow as tf
import numpy as np
#tensorflow 2.0 사용불가, tensorflow 1.0 사용가능
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import matplotlib.pyplot as plt

#x_data = shape : (4, 2) 4 x 2 matrix, y_data = shape : (4, 1) 4 x 1 matrix 매트릭스로 생각하면 쉽다
x_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_data = np.array([[0], [1], [1], [0]], dtype=np.float32)
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

#NN을 사용하여 XOR 구현
W1 = tf.Variable(tf.random_normal([2, 2]))
b1 = tf.Variable(tf.random_normal([2]))

W2 = tf.Variable(tf.random_normal([2, 1]))
b2 = tf.Variable(tf.random_normal([1]))

f_x = tf.sigmoid(tf.matmul(X, W1) + b1)
hypothesis = tf.sigmoid(tf.matmul(f_x, W2) + b2)
cost = -tf.reduce_mean(Y * tf.log(hypothesis) +  (1 - Y) * tf.log(1 - hypothesis))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.15).minimize(cost)

prediction = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, Y), dtype=tf.float32))
#run
cost_arr = []
h_arr = []
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(10001):
        cost_val, h_val, _ = sess.run([cost, hypothesis, optimizer], feed_dict={X : x_data, Y : y_data})
        cost_arr.append(cost_val)
        h_arr.append(h_val)
        if step % 500 == 0 :
            print(cost_val, "hy", h_val)
# plt.plot(h_arr, cost_arr)
# plt.show()
    p, a = sess.run([prediction, accuracy], feed_dict={X :x_data, Y : y_data})
    print("\nprediction ", p, "\naccuracy ", a)
