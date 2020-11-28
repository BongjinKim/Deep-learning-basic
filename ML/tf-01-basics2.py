import tensorflow as tf

#1. Build graph
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)

#2. run graph
@tf.function
def forward():
	#3. update variables
    return node1 + node2

out_a = forward()
print(out_a)
