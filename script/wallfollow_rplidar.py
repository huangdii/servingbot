#! /usr/bin/env python
 
# import ros stuff
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf import transformations
 
import math

pub_ = None
regions_ = {
    'right': 0,
    'fright': 0,
    'front': 0,
    'fleft': 0,
    'left': 0,
}
state_ = 0
state_dict_ = {
    0: 'find the wall',
    1: 'turn left',
    2: 'follow the wall',
}

pub_ = None
regions_ = {
    'right': 0,
    'fright': 0,
    'front': 0,
    'fleft': 0,
    'left': 0,
}
state_ = 0
state_dict_ = {
    0: 'find the wall',
    1: 'turn left',
    2: 'follow the wall',
}

def clbk_laser(msg):
    global regions_


    front = min(min(lidar[0:30]),10.0)
    front = min(min(lidar[330:359]),front)

    regions_ = {
        'right': min(min(lidar[31:75]),10),
        'front':  front,
        'left':   min(min(lidar[285:329]),10),
    }

    take_action()


def change_state(state):
    global state_, state_dict_
    if state is not state_:
        print 'Wall follower - [%s] - %s' % (state, state_dict_[state])
        state_ = state


def take_action():
    global regions_
    regions = regions_
    msg = Twist()
    linear_x = 0
    angular_z = 0
    
    state_description = ''
    
    d = 0.4
    if regions['front'] > d and regions['left'] > d and regions['right'] > d:
        print('case 1 - nothing')
        change_state(0)
    elif regions['front'] < d and regions['left'] > d and regions['right'] > d:
        print('case 2 - front')
        change_state(1)
    elif regions['front'] > d and regions['left'] > d and regions['right'] < d:
        print('case 3 - right')
        change_state(2)  # wall follow
    elif regions['front'] > d and regions['left'] < d and regions['right'] > d:
        print('case 4 - left')
        change_state(0)
    elif regions['front'] < d and regions['left'] > d and regions['right'] < d:
        print('case 5 - front and right')
        change_state(1)  # turn left
    elif regions['front'] < d and regions['left'] < d and regions['right'] > d:
        print('case 6 - front and left')
        change_state(1)
    elif regions['front'] < d and regions['left'] < d and regions['right'] < d:
        print('case 7 - front and left and right')
        change_state(1)
    elif regions['front'] > d and regions['left'] < d and regions['right'] < d:
        print('case 8 - left and right')
        change_state(0)
    else:
        state_description = 'unknown case'
        rospy.loginfo(regions)

def find_wall():
    msg = Twist()
    msg.linear.x = 0.15
    msg.angular.z = -0.3
    return msg

def turn_left():
    msg = Twist()
    msg.angular.z = 0.3
    return msg

def follow_the_wall():
    global regions_
    
    msg = Twist()
    msg.linear.x = 0.15
    return msg


def main():
    global pub_
    
    rospy.init_node('reading_laser')
    
    pub_ = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    
    sub = rospy.Subscriber('/scan', LaserScan, clbk_laser)
    
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        msg = Twist()
        if state_ == 0:
            msg = find_wall()
        elif state_ == 1:
            msg = turn_left()
        elif state_ == 2:
            msg = follow_the_wall()
            pass
        else:
            rospy.logerr('Unknown state!')
        
        pub_.publish(msg)
        
        rate.sleep()

if __name__ == '__main__':
    main()
