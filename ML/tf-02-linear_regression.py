#linear_regression

#1. ready to X, Y data set
# X = [1, 2, 3, 4, 5]
# Y = [1, 2, 3, 4, 5]

# X, Y placeholder, placeholder는 train 시킬 때, feed_dict로 넘겨 줄 수 있다.
X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])

#2. W is Weight, b is bias, tf.Variable(값, 이름)
W = tf.Variable(tf.random_normal([1]), name ='weight')
b = tf.Variable(tf.random_normal([1]), name ='bias')
hypothesis = W * X + b

#3. Loss, It is cost fuction
cost = tf.reduce_mean(tf.square(hypothesis - Y))

#4. minimizing cost function
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

#5. Session 정의
sess = tf.Session()

#6. Session 초기화
sess.run(tf.global_variables_initializer())

#7. 학습
for step in range(2001):
    cost_var, W_var, b_var, _ = sess.run([cost, W, b, train], feed_dict = {X : [1, 2, 3, 4, 5], Y : [1, 2, 3, 4, 5]})
    if step % 20 == 0:
        print(step, cost_var, W_var, b_var)
#8. test
print(sess.run(hypothesis, feed_dict={X : [5]}))
print(sess.run(hypothesis, feed_dict={X : [8.5]}) )
print(sess.run(hypothesis, feed_dict={X : [7, 10]}))
