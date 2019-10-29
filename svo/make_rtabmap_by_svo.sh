#!/bin/bash
SVO_FILE=$1
DATABASE_NAME=${SVO_FILE%.*}
DATABASE_FILE=$DATABASE_NAME.db
roslaunch servebot zed_rtabmap_svo.launch svo_file:=$(realpath $SVO_FILE) database_path:=$(rospack find servebot)/db/$DATABASE_FILE
