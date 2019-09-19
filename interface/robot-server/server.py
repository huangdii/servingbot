from flask import Flask, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={
  r"/*": {"origin": "*"},
})

db = [{"content":"김치찌개주문되었습니다, 곧 로봇이 음식을 가져다 드리겠습니다"},{"content":"오무라이스주문되었습니다"}]

ordered = False
serving = False

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



if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)
  # app.run(host='localhost',port=5000)
