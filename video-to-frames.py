import numpy as np
#import cv2
from subprocess import call
import numpy
import os
import sys

print(sys.version)


#NOTE: This was compiled with Python version 2.7.2
#This goes into the data folders and creates as as many photos as possible by using vlc media player plugin


#The base command is

path_to_vlc = "C:\\'Program Files (x86)'\\VideoLAN\\VLC"

path_to_data = "C:\\Users\\ppaudyal\\workspace\\video-asl\\DatabyClasses"

os.chdir(path_to_data)

prefix_counter = 0
for folder_path in os.listdir(path_to_data):
    this_path = path_to_data + "\\" + folder_path
    os.chdir(this_path)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    file_counter = 0
    for video_file in os.listdir(os.getcwd()):
        file_counter += 1
        prefix_counter += 1
        scene_path = this_path + "\\" + folder_path #+ str(file_counter)
        #os.mkdir(scene_path)
        this_vlc_command = "vlc " + this_path + "\\" + video_file + " --video-filter=croppadd --croppadd-cropbottom=70 --video-filter=scene --vout=dummy --scene-ratio=1 --scene-prefix=" \
                           + str(prefix_counter) + " --scene-path=" + scene_path + " vlc://quit"
        os.system(this_vlc_command)
        #run vlc_quit
        print(this_vlc_command)


#sanity check
#print(os.listdir(path_to_data))
#for dirs in path_to_data
#cd to directory
#create folder all_frames
#for file in current directory
#call vlc command to extract all frames to "all_frames"




# FFMPEG_BIN = "C:\\ffmpeg\\bin\\ffmpeg.exe"
#
#
# command = [ FFMPEG_BIN,
#             '-i', 'C:\\Users\\ppaudyal\\workspace\\video-asl\\test.mp4',
#             '-f', 'image2pipe',
#             '-pix_fmt', 'rgb24',
#             '-vcodec', 'rawvideo', '-']
#
# pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)
#
# raw_image = pipe.stdout.read(420*360*3)



# #vc = cv2.VideoCapture(0)
# vc = cv2.VideoCapture('C:\\Users\\ppaudyal\\workspace\\video-asl\\drop.avi')
# c=1
#
# print (cv2.__version__)
# if vc.isOpened():
#     rval , frame = vc.read()
# else:
#     rval = False
#
# while rval:
#     rval, frame = vc.read()
#     cv2.imwrite(str(c) + '.jpg',frame)
#     c = c + 1
#     cv2.waitKey(1)
# vc.release()