#tensorflow 1.0
# hypothesis using matrix
import tensorflow as tf
import numpy as np
#tensorflow 2.0 사용불가, tensorflow 1.0 사용가능
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#1 dataset
xy = np.loadtxt('dataset.csv', delimiter=',', dtype=np.float32)
#numpy에서는 ,를 사용하여 2차원 배열의 slice가 가능함
x_data = xy[:, 0:-1]
y_data = xy[:,[-1]]
X = tf.placeholder(tf.float32, shape = [None, 3])
Y = tf.placeholder(tf.float32, shape = [None, 1])

#2 Variables, 3 x 1 matrix
W = tf.Variable(tf.random_normal([3, 1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')
hypothesis = tf.matmul(X, W) + b

#3 cost
cost = tf.reduce_mean(tf.square(hypothesis - Y))

#4 minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 1e-5)
train = optimizer.minimize(cost)

#5, 6 session, init
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#7 학습
for step in range(2001):
    cost_var, h_var, _ = sess.run([cost, hypothesis, train], feed_dict = {X : x_data, Y : y_data})
    if step % 20 == 0:
        print(cost_var, h_var)

#8 test 총점이 같은 세 사람의 비교
print("A : ", sess.run(hypothesis, feed_dict = {X : [[100, 90, 110]]}))
print("B : ", sess.run(hypothesis, feed_dict = {X : [[110, 100, 90]]}))
print("C : ", sess.run(hypothesis, feed_dict = {X : [[90, 110, 100]]}))
