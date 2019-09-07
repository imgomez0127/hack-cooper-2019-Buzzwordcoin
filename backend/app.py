import sys
from flask import Flask
from flask import send_file,jsonify
from pymongo import MongoClient
from flask_cors import CORS
app = Flask(__name__)
client = MongoClient("localhost",27017)
db = client["mlcoin"]
CORS(app)

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

if __name__ == "__main__":
    app.run("localhost",8000,debug=True)
