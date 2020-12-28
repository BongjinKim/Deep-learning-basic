# # cost minimize 구현하기위해 cost function 그래프 그리기
# import tensorflow as tf
# import matplotlib.pyplot as plt
# #tensorflow 2.0 사용불가, tensorflow 1.0 사용가능
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()
#
# #1 data set, placeholder
# X = tf.placeholder(tf.float32)
# Y = tf.placeholder(tf.float32)
#
# #2 optimizer를 구현하기 위해서 W를 placeholder로 선언, b is not
# W = tf.placeholder(tf.float32)
#
# hypothesis = W * X
# #3 cost, Loss function
# cost = tf.reduce_mean(tf.square(hypothesis - Y))
#
# #4 cost minimize 생략
#
# #5 #6 session 선언, 초기화
# sess = tf.Session()
# sess.run(tf.global_variables_initializer())
#
# #7 run and draw
# cost_arr, W_arr = [[], []]
# for i in range(-20, 40):
#     cost_var, W_var = sess.run([cost, W], feed_dict = {W : [i * 0.1], X : [1,2,3,4,5], Y : [1,2,3,4,5]})
#     cost_arr.append(cost_var)
#     W_arr.append(W_var)
# plt.plot(W_arr, cost_arr)
# plt.title('cost(W) = reduce_mean(tf.square(hypothesis - Y))')

import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

#1 data set, placeholder
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

#2 optimizer를 구현했으므로 random 값 삽입
W = tf.Variable(tf.random_normal([1]), name = 'weight')

hypothesis = W * X
#3 cost, Loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

#4 cost minimize 구현, cost'(W) = tf.reduce_mean(W * X**2 - X * Y)
gradient = tf.reduce_mean(W * X**2 - X * Y) * 2
learning_rate = 0.01
descent = W - gradient * learning_rate
update = W.assign(descent)


#5 #6 session 선언, 초기화
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#7 학습
for step in range(41):
    cost_var, W_var, _ = sess.run([cost, W, update], feed_dict = {X : [1,2,3,4,5], Y : [1,2,3,4,5]})
    print(step ,cost_var, W_var)
