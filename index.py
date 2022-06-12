# REST API return jsonify o client
from ctypes import util
from flask import Flask, jsonify, request
import utils

app = Flask(__name__)

# defien endpoint
@app.route("/categories", methods = ["GET"])
def getCategories():
    rows = utils.getALL("SELECT * FROM category")
    data = []
    # paste du lieu json va tra ve cho client
    for r in rows:
        data.append({
            "id": r[0],
            "name": r[1],
            "url": r[2],
        })
    # hung toan bo du lieu trong news
    return jsonify({"categories": data})


@app.route("/news", methods = ["GET"])
def getNews():
    rows = utils.getALL("SELECT * FROM news")
    data = []
    # parse du lieu json va tra ve cho client
    for r in rows:
        data.append({
            "id": r[0],
            "subject": r[1],
            "description": r[2],
            "image": r[3],
            "original_url": r[4]
        })

    # hung toan bo du lieu trong news
    return jsonify({"news": data})



@app.route("/news/<int:newsID>", methods = ["GET"])
def getNewsByID(newsID):
    r = utils.getNewsByID(newsID)
    d = {
        "subject": r[0],
        "description": r[1],
        "image": r[2],
        "original_url": r[3],
        "category_name": r[4],
        "category_url": r[5]
    }

    return jsonify({"product": d})

@app.route("/news/<int:newsID>", methods = ["POST"])
def insertComment(newsID):
    # import pdb
    # pdb.set_trace()
    # kiem tra co content hay khong
    # neu khong kiem tra thi dung request se bao loi
    if request.form.get("content"):
        utils.addComment(newsID, request.form["content"])
        
        return jsonify({"status": 1, "message": "Successful"})
    
    return jsonify({"status": -1, "message": "Need News ID"})

@app.route("/news/add", methods = ["POST"])
def insertNews():
    pass


if __name__ == "__main__":
    app.run() 