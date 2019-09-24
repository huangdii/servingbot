#!/usr/bin/env python3
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from .goal_api import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import rospy
import actionlib

app = Flask(__name__)
cors = CORS(app, resources={
  r"/*": {"origin": "*"},
})

db = [{"content":"김치찌개주문되었습니다, 곧 로봇이 음식을 가져다 드리겠습니다"},{"content":"오무라이스주문되었습니다"}]


ordered = False
serving = False


table_db = [
    {"x":"-3.0","y":"0.7"},
    {"x":"-3.0","y":"2.0"},
    {"x":"-3.0","y":"4.0"}
]



@app.route("/api/order/food/<foodNum>", methods=["GET"])
def getSlideContent(foodNum):
  global ordered
  if not ordered:
    res = db[int(foodNum)-1]
    ordered = True
    return res['content']
  elif ordered:
    return "로봇이 바쁩니다"

@app.route("/api/reset/order/", methods=["GET"])
def resetOrder():
  global ordered
  ordered = False
  return "reset 되었습니다"

@app.route("/api/received/", methods=["GET"])
def orderReceived():
  return "음식 서빙이 끝났습니다 식당으로 돌아갑니다 "

@app.route("/api/serving/start/<tableNo>",methods=["GET"])
def servingStart(tableNo):
  global serving
  if not serving:
    serving = True
    return tableNo + " 번 테이블로의 서빙이 시작되었습니다"
  elif serving:
    return "지금 로봇은 서빙중에 있습니다."

@app.route("/api/reset/serving/", methods=["GET"])
def resetServing():
  global serving
  serving = False
  return "reset 되었습니다"

def movebase_client():

  client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
  client.wait_for_server()

  goal = MoveBaseGoal()
  goal.target_pose.header.frame_id = "map"
  goal.target_pose.header.stamp = rospy.Time.now()
  goal.target_pose.pose.position.x = -3.0
  goal.target_pose.pose.orientation.w = 0.7

  client.send_goal(goal)
  wait = client.wait_for_result()
  
  if not wait:
      rospy.logerr("Action server not available!")
      rospy.signal_shutdown("Action server not available!")
  else:
  # Result of executing the action
      return client.get_result()   

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)
  try:
    # Initializes a rospy node to let the SimpleActionClient publish and subscribe
    rospy.init_node('movebase_client_py')
    result = movebase_client()
    if result:
        rospy.loginfo("Goal execution done!")
  except rospy.ROSInterruptException:
      rospy.loginfo("Navigation test finished.")
  # app.run(host='localhost',port=5000)
