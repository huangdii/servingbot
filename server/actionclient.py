#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


def movebaseclient(x:int,y:int):
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x=x
    goal.target_pose.pose.position.y=y
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
        table1Arrival=False
        print("move base client init")
        while not rospy.is_shutdown():
            if table1Arrival:
                result = movebaseclient(-3,0.7)
                table1Arrival = False
            else:
                result = movebaseclient(1.3,0.7)
                table1Arrival = True

            if result:
                rospy.loginfo("goal execution OK")
            rospy.sleep(5)
    except rospy.ROSInterruptException:
        rospy.loginfo("test finished")