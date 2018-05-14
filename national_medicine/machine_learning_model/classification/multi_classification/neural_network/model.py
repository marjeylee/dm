# -*- coding: utf-8 -*-
"""
构建模型
"""

import tensorflow as tf

from national_medicine.machine_learning_model.classification.multi_classification.neural_network.data_manager import \
    get_train_vector_batch
from national_medicine.machine_learning_model.classification.multi_classification.neural_network.model_shape import \
    model_shape

__author__ = 'l'
__date__ = '2018/5/11'


class MultiClassificationModel:
    """
    多分类模型
    """

    def create_full_connection_layer(self, bottom, name):
        """
        创建全连接层
        :param bottom: 上一层输出
        :param name:名称
        :return:
        """
        with tf.variable_scope(name):
            shape = bottom.get_shape().as_list()
            dim = 1
            for d in shape[1:]:
                dim *= d
            x = tf.reshape(bottom, [-1, dim])
            weights = self.get_wight(name)
            biases = self.get_bias(name)
            name = name + '_fc'
            fc = tf.nn.bias_add(tf.matmul(x, weights), biases, name=name)
            return fc

    @staticmethod
    def get_wight(name):
        """
        获取权重w
        :param name:卷积层名称
        :return:
        """
        shape = model_shape[name][0]
        initial_value = tf.truncated_normal(shape, stddev=0.1)
        name = name + '_w'
        return tf.Variable(initial_value, name=name)

    @staticmethod
    def get_bias(name):
        """
        获取偏移量
        :param name:
        :return:
        """
        shape = model_shape[name][1]
        initial_value = tf.truncated_normal(shape, stddev=0.1)
        name = name + '_b'
        return tf.Variable(initial_value, name=name)

    def __init__(self, batch_size):
        """
        模型构建
        :param batch_size:
        """
        self.input = tf.placeholder(dtype=tf.float32, shape=[batch_size, 1300], name='input')
        self.full_connection_layer1 = self.create_full_connection_layer(self.input, "full_connection_layer1")
        self.relu1 = tf.nn.relu(self.full_connection_layer1, name='relu1')
        self.full_connection_layer2 = self.create_full_connection_layer(self.relu1,
                                                                        "full_connection_layer2")
        self.relu2 = tf.nn.relu(self.full_connection_layer2, name='relu2')
        self.full_connection_layer3 = self.create_full_connection_layer(self.relu2,
                                                                        "full_connection_layer3")
        self.relu3 = tf.nn.relu(self.full_connection_layer3, name='relu3')





        self.probability = tf.nn.softmax(self.relu3, name="probability")
        print(self)

    def train(self):
        """
        模型训练
        :return:
        """
        y_ = tf.placeholder(tf.float32, shape=[None, 1300])
        cross_entropy = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(logits=self.relu3, labels=y_))
        train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
        correct_prediction = tf.equal(tf.argmax(y_, 1), tf.argmax(self.relu3, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        input_batch, output_batch = get_train_vector_batch()
        with tf.Session(
                config=tf.ConfigProto(gpu_options=(tf.GPUOptions(per_process_gpu_memory_fraction=0.7)))) as sess:
            sess.run(tf.global_variables_initializer())
            for i in range(500000):
                try:
                    if i % 20 == 0:
                        train_accuracy = accuracy.eval(feed_dict={
                            self.input: input_batch, y_: output_batch})
                        print("step %d, training accuracy %g" % (i, train_accuracy))
                    train_step.run(feed_dict={
                        self.input: input_batch, y_: output_batch})
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    model = MultiClassificationModel(5)
    model.train()
