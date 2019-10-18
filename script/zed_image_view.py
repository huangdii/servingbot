#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2, cv_bridge



class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()        
        self.image_sub = rospy.Subscriber("/zed/zed_node/right_raw/image_raw_color", 
                                         Image, self.image_callback)
    
    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg,'bgr8')
        # cv2.namedWindow("followBotImage",cv2.WINDOW_GUI_EXPANDED)
        cv2.namedWindow("zed_image",cv2.WINDOW_GUI_NORMAL)
        cv2.imshow("zed_image", image)
        cv2.waitKey(3)
        
rospy.init_node('zed_image_viewer')
follower = Follower()
rospy.spin()

