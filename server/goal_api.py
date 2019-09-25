
import rospy
import rospkg
import json
from geometry_msgs.msg import PoseStamped
import os


def current_time_show():
    print(rospy.Time.now())


if __name__ == '__main__':
    rospy.init_node("goal_send_test_node")  

    tableno = 2

    rospack = rospkg.RosPack()
    json_path = rospack.get_path('servebot') + '/server/table_no.json'
    with open(str(json_path),'r') as f:
        table_poses = json.load(f)

    ps = PoseStamped()  
    ps.pose.position.x = float(table_poses[tableno]["x"])
    ps.pose.position.y = float(table_poses[tableno]["y"])
    pub = rospy.Publisher("/move_base_simple/goal",PoseStamped,queue_size=1)
    pub2 = rospy.Publisher("/move_base/goal",PoseStamped,queue_size=1)
    pub3 = rospy.Publisher("/move_base/current_goal",PoseStamped,queue_size=1)
    ps.header.frame_id = 'requested_pos'
    ps.header.stamp = rospy.Time.now()
    
    while not rospy.is_shutdown():
        pub.publish(ps)
        pub2.publish(ps)
        pub3.publish(ps)

