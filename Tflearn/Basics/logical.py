from __future__ import absolute_import, division, print_function

import tensorflow as tf
import tflearn

X = [[0.], [1.]]
Y = [[1.], [0.]]

# with 블록은 파일을 열고 쓰고 닫을 때 굳이 close()를 하지 않더라도 자동으로 닫아줌
with tf.Graph().as_default():
    g = tflearn.input_data(shape=[None, 1])
    g = tflearn.fully_connected(g, 128, activation='linear')