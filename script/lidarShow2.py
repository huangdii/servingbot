#!/usr/bin/env python3

import rospy
import sys
import numpy as np 
from sensor_msgs.msg import LaserScan


min,max = sys.argv[1:3]
float_formatter = lambda x: "%.2f" % x
np.set_printoptions(formatter= {'float_kind':float_formatter})

def clbkReadLaser(data : LaserScan):
    ranges = np.array(data.ranges[int(min):int(max)])
    print('from min : {0} to max : {1} --> {2} total scan size : {3}'.format(min,max,ranges[:],len(data.ranges)),end='\r' )
    sys.stdout.flush()

rospy.init_node("ScanReadNode")
rospy.Subscriber("/scan",LaserScan,clbkReadLaser)
rospy.spin()
