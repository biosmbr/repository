'''
Created on Aug 7, 2017

@author: centos7
'''

import tensorflow as tf
hello=tf.constant('hello,Tensorflow')
sess=tf.Session()
print sess.run(hello)