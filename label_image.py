#This file loads a graph file and predicts with it.
#the graph file and the labels file are assumed to be in tf_files\\retrained_graph.pb.

import tensorflow as tf, sys
import os
import numpy as np

#change these if they lie somewhere else
retrained_labels = "tf_files\\retrained_labels.txt"
retrained_graph = "tf_files\\retrained_graph.pb"
#TODO get this dynamically from file
number_of_classes = 6

#predict Video takes a video sample of image files and puts a graph out with labels corresponding to y axis
def predict_video(path):

    #create an empty numpy array with zeroes
    predicted_values = np.zeros((os.listdir(path).__len__(), number_of_classes ))
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile(retrained_labels)]
    predictions_matrix = np.zeros((os.listdir(path).__len__(), 6))
    # unpersists graph from file
    with tf.gfile.FastGFile(retrained_graph, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        file_counter = 0
        for file in os.listdir(path):
            image_path = path + "\\" + file
            image_data = tf.gfile.FastGFile(image_path, 'rb').read()
            predictions = sess.run(softmax_tensor, \
                                   {'DecodeJpeg/contents:0': image_data})
            # sort to show labels of first prediction in order of confidence
            predictions_matrix[file_counter] = predictions
            file_counter = file_counter + 1
    return predictions_matrix

def sample_predict(image_path):
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()
    #loads label file, strips off the carriage return
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile(retrained_labels)]
    #unpersists graph from file
    with tf.gfile.FastGFile(retrained_graph, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, \
                               {'DecodeJpeg/contents:0': image_data})
        #sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            print('%s (score = %0.5f)' %(human_string, score))


#sample_predict("C:\\Users\\ppaudyal\\workspace\\video-asl\\tf_files\\flower_photos\\finish\\100001.jpg")


prediction_matrix = predict_video("C:\\Users\\ppaudyal\\workspace\\video-asl\\tf_files\\flower_photos\\finish")
np.savetxt("name", prediction_matrix, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')