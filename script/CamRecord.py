#!/usr/bin/env python3

import os

#image_view = "rosrun image_view image_view image:=/camera/rgb/image_raw"
video_recorder = "rosrun image_view video_recorder image:=/camera/rgb/image_raw"

#os.system(image_view)
os.system(video_recorder)
