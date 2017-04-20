import sys, os
from label_image import predict_video

is_test_video = True

image_folder = "C:\\Users\\ppaudyal\\workspace\\video-asl\\tf_files\\flower_photos\\finish"


#take a video


#parse vide

if(is_test_video):
    prediction_matrix = predict_video(image_folder)