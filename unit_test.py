import sys, os
from label_image import predict_video

is_test_video = True

video_folder = "C:\\Users\\ppaudyal\\workspace\\video-asl\\tf_files\\flower_photos"
path = "mixture"

#take a video


#parse vide

if(is_test_video):
    for path in os.listdir(video_folder):
        predict_video(video_folder+ "\\" + path)