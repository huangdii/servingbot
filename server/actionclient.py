#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


def movebaseclient():
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x=2.0
    goal.target_pose.pose.position.y=0.7
    goal.target_pose.pose.orientation.w=1

    client.send_goal(goal)
    result = client.wait_for_result()
    if not result:
        rospy.logerr("no result, no action server available")
        rospy.signal_shutdown("action server not available")
    else:
        return client.get_result()

if __name__ =='__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebaseclient()
        if result:
            rospy.loginfo("goal execution OK")
    except rospy.ROSInterruptException:
        rospy.loginfo("test finished")