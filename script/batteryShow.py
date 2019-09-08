#!/usr/bin/env python3

import rospy
import sys
import numpy as np 
from sensor_msgs.msg import LaserScan,BatteryState


def clbkReadBattery(data : BatteryState):
    print(data.percentage, data.power_supply_health, data.power_supply_status, data.power_supply_technology)
    sys.stdout.flush()

rospy.init_node("read_battery")
rospy.Subscriber("/battery_state",BatteryState,clbkReadBattery)
rospy.spin()