#tensorflow 1.0
import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

xy = np.loadtxt('zoo.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]
X = tf.placeholder(tf.float32, [None, 16])
Y = tf.placeholder(tf.int32, [None, 1])

#동물의 종류
animal_classes = 7

#y_one_hot api 사용 후 reshape
y_one_hot = tf.one_hot(Y, animal_classes)
y_one_hot = tf.reshape(y_one_hot, [-1, animal_classes])

W = tf.Variable(tf.random_normal([16, animal_classes]), name = 'weight')
b = tf.Variable(tf.random_normal([animal_classes]), name = 'bias')

#logits, hypothesis
logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)

#cost
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits = logits, labels = y_one_hot)
cost = tf.reduce_mean(cost_i)

#minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

#predict
prediction = tf.argmax(hypothesis, 1)
is_correct = tf.equal(prediction, tf.argmax(y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(10000):
        sess.run(optimizer, feed_dict = {X : x_data, Y : y_data})
        if step % 200 == 0:
            loss, acc = sess.run([cost, accuracy], feed_dict = {X : x_data, Y : y_data})
            print(step, loss, acc)

    pre = sess.run(prediction, feed_dict = {X : x_data})
    for (p, y) in zip(pre, y_data.flatten()):
        print(p, int(y))
