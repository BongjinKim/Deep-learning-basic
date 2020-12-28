#tensorflow 1.0
import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

x_data = [[1], [2], [3], [4], [5], [20]]
y_data = [[0], [0], [0], [1], [1], [1]]
X = tf.placeholder(tf.float32, shape=[None, 1])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([1, 1], mean=0.001, stddev=0.001), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) *
                       tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.00015).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(100010):
        cost_val, hypothesis_val, _ = sess.run([cost, hypothesis, train], feed_dict = {X : x_data, Y : y_data})
        if step % 20000 == 0:
            print(step, hypothesis_val)
    h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X: x_data, Y:y_data})
    print('\nhypothesis : ',h,"\ncorrect : ", c, '\naccuracy : ', a)
