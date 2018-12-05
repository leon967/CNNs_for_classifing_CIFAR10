import tensorflow as tf 

def weight_variable(shape):
	initial = tf.truncated_normal(shape, stddev=0.1)
	return tf.Variable(initial)

def bias_variable(shape):
	initial = tf.constant(0.1, shape=shape)
	return tf.Variable(initial)

def conv2d(x, W):
	return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
	return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

class LeNet(object):
	def __init__(self, x, keep_prob, num_classes):
		self.x = x
		self.keep_prob = keep_prob
		self.num_classes = num_classes
		self._build_model()

	def _build_model(self):

		# Conv1 layer
		W_conv1 = weight_variable([5, 5, 3, 6])
		b_conv1 = bias_variable([6])
		h_conv1 = tf.nn.relu(conv2d(self.x, W_conv1) + b_conv1)
		h_pool1 = max_pool_2x2(h_conv1)

		# Conv2 layer
		W_conv2 = weight_variable([14, 14, 6, 16])
		b_conv2 = bias_variable([16])
		h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
		h_pool2 = max_pool_2x2(h_conv2)

		# FC layer
		W_fc1 = weight_variable([1024, 120])
		b_fc1 = bias_variable([120])
		h_pool2_flat = tf.reshape(h_pool2, [-1, 1024])
		h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

		# Drop layer
		keep_prob = tf.placeholder(tf.float32)
		h_fc1_drop = tf.nn.dropout(h_fc1, self.keep_prob)

		# Output layer
		W_fc2 = weight_variable([120, self.num_classes])
		b_fc2 = bias_variable([self.num_classes])
		self.y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
