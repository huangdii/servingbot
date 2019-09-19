from flask import Flask, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={
  r"/*": {"origin": "*"},
})

db = [{"content":"asdf"},{"content":"asdf2"},{"content":"asdf3"}]


@app.route("/api/slideContent/<slideNo>", methods=["GET"])
def getSlideContent(slideNo):
    res = db[int(slideNo)-1]
    return res['content']


if __name__ == '__main__':
    app.run(host='namlonx',port=5000)
    # app.run(host='localhost',port=5000)
