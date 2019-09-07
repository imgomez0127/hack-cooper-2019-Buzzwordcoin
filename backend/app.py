import sys
from flask import Flask
from flask import send_file,jsonify
import pymongo
from pymongo import MongoClient
from flask_cors import CORS
from datetime import datetime
app = Flask(__name__)
client = MongoClient("localhost",27017)
db = client["mlcoin"]
CORS(app)
def find_most_recent_block():
    block_collection = db["block"]
    block_sorted_by_date = list(db.find({}).sort("date",pymongo.DESCENDING))
    return block_sorted_by_date[0]

@app.route("/get-datasets")
def datasets():
    print("hello world",file=sys.stderr)
    dataset_collection = db["datasets"]
    datasets = list(dataset_collection.find())
    for dataset in datasets:
        del dataset["_id"] 
    return jsonify(datasets)

@app.route("/download-dataset/<dataset>")
def download_datasets(dataset):
    return send_file("datasets/"+dataset+".zip",as_attachment=True,attachment_filename=dataset+".zip")

@app.route("/get-most-recent-block")
def most_recent_block():
    return jsonify(find_most_recent_block())

@app.route("/check-if-more-accurate/<float:accuracy>")
def check_if_more_accurate(accuracy):
    accepted = find_most_recent_block()["accuracy"] < accuracy
    return jsonify({"accepted":accepted})

@app.route("/add-block/<float:accuracy>")
def add_block(accuracy):
    block_collection = db["block"]
    date = datetime.datetime().strftime("%Y-%m-%dT%H:%M:%S.000Z")
    previous_block = find_most_recent_block()
    block_hash = hash(previous_block["hash"]+str(accuracy))
    previous_block["next_hash"] = block_hash
    block_collection.update_one(previous_block)
    block_collection.insert_one({
        "hash":block_hash,
        "accuracy":accuracy,
        "next_hash":"",
        "date":date
    })
    return True
    
if __name__ == "__main__":
    app.run("localhost",8000,debug=True)
