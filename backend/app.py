from flask import Flask
from flask import send_file
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient("localhost",27017)
db = client["mlcoin"]

@app.route("/get-datasets")
def datasets():
    dataset_collection = db["datasets"]
    return dataset_collection.find({})

@app.route("/download-datasets/<dataset>")
def download_datasets(dataset):
    return send_file("datasets/"+dataset+".zip",as_attachment=True,attachment_filename=dataset+".zip")

if __name__ == "__main__":
    app.run("localhost",8000,debug=True)
