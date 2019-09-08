#!/usr/bin/env python3

import rospy
import sys
import numpy as np 
from sensor_msgs.msg import LaserScan


min,max = sys.argv[1:3]
float_formatter = lambda x: "%.2f" % x
np.set_printoptions(formatter= {'float_kind':float_formatter})

def clbkReadLaser(data : LaserScan):
    ranges = np.concatenate((data.ranges[int(min):-1],data.ranges[:int(max)]),axis=0)
    print('from min : {0} to max : {1} --> {2}'.format(min,max,ranges[:]),end='\r' )
    sys.stdout.flush()

rospy.init_node("ScanReadNode")
rospy.Subscriber("/scan",LaserScan,clbkReadLaser)
rospy.spin()