import httplib
from jinja2 import Template
from flask import Flask
from flask import request
from pymongo import MongoClient
import appf

client = MongoClient()
db = client['info']
collection = db.users

app = Flask(__name__)


html = open('d.html').read()
# mongo1= open("Bd/users.js").read()

template = Template(html)
@app.route("/",methods=['post', 'get'])
def ip():


    colection_str = []
    mas_collection_names = db.collection_names()
    for i in range(len(mas_collection_names)):
        collection_names = request.form.get('collection_names')
        colection_str.append(str(mas_collection_names[i]))
    message=""
    if collection_names == 'users':
        message = collection_names
        appf.app1.run(host='0.0.0.0', port=1455)

    # return (template.render(name=colection_str))

    return (template.render(name=colection_str, name2=message))

if __name__ == "__main__":
# app.run()nn
    app.run(host='0.0.0.0', port=1497 ,debug=True)