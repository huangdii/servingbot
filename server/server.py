#!/usr/bin/env python3
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from actionclient import movebaseclient
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
    {"x":"-3.0","y":"0.9"},
    {"x":"-1.0","y":"0.9"},
    {"x":"1.3","y":"0.9"}
]



@app.route("/api/order/food/<foodNum>", methods=["GET"])
def orderFood(foodNum):
  global ordered
  if not ordered:
    res = db[int(foodNum)-1]
    ordered = True
    startPoint = table_db[0]
    x = float(startPoint['x'])
    y = float(startPoint['y'])
    movebaseclient(x,y)

    rospy.loginfo("moving back to 식당 execution OK")

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

    res = table_db[int(tableNo)]
    
    x = float(res['x'])
    y = float(res['y'])
    print("서빙하러 가는 테이블의 좌표(x,y):",x ,y)
    movebaseclient(x,y)
    rospy.loginfo("goal execution OK")
    return tableNo + " 번 테이블로의 서빙이 시작되었습니다"
  elif serving:
    return "지금 로봇은 서빙중에 있습니다."

@app.route("/api/reset/serving/", methods=["GET"])
def resetServing():
  global serving
  serving = False
  return "reset 되었습니다"


if __name__ == '__main__':
  try:
    rospy.init_node('movebase_client_py')
    rospy.loginfo("move base init Successed")
    app.run(host='0.0.0.0',port=5000)
  except rospy.ROSInterruptException:
    rospy.loginfo("test finished")
