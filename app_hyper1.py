import httplib
from jinja2 import Template
from flask import Flask
from flask import request
from pymongo import MongoClient

client = MongoClient()
db = client['info']
collection = db.users

app = Flask(__name__)


html = open('hyper1.html').read()
# mongo1= open("Bd/users.js").read()

template = Template(html)

@app.route("/")
def ip():


    colection_str = []
    mas_collection_names = db.collection_names()
    for i in range(len(mas_collection_names)):

        colection_str.append(str(mas_collection_names[i]))

    return (template.render(name=colection_str))

if __name__ == "__main__":
# app.run()nn
    app.run(host='0.0.0.0', port=1574 ,debug=True)