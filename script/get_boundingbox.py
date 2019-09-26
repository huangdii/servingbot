#!/usr/bin/env python3

import rospy

from darknet_ros_msgs.msg import BoundingBox
from darknet_ros_msgs.msg import BoundingBoxes

def callback(msg:BoundingBoxes):
    for Bounding_box in msg.bounding_boxes:
        print("Class : {}, Probability : {}, xmin : {}, ymin : {}, xmax : {}, ymax : {}".format(
            Bounding_box.Class, Bounding_box.probability, Bounding_box.xmin, Bounding_box.ymin, Bounding_box.xmax, Bounding_box.ymax)
        )

# def callback(data):
#     rospy.loginfo(data.data)

rospy.init_node("get_boundingbox")
sub = rospy.Subscriber('/darknet_ros/bounding_boxes', BoundingBoxes, callback)

rospy.spin()
