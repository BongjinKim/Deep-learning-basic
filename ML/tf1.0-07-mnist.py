#tensorflow 1.0
#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
tf.set_random_seed(777)  # for reproducibility

import numpy as np

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/MNIST_data/", one_hot=True)

nb_classes = 10
#MNIST 28 * 28 pixel
X = tf.placeholder(tf.float32, [None, 784])
#0-9 digits, 10 classes
Y = tf.placeholder(tf.float32, [None, nb_classes])

W = tf.Variable(tf.random_normal([784, nb_classes]))
b = tf.Variable(tf.random_normal([nb_classes]))

#hypothesis
hypothesis = tf.nn.softmax(tf.matnul(X, W) + b)
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits = logits, labels = y_one_hot)
cost = tf.reduce_mean(cost_i)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

is_correct = tf.equal(tf.argmax(Y, 1), tf.argmax(hypothesis, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
