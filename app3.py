import httplib
from jinja2 import Template
from flask import Flask
from flask import request
from pymongo import MongoClient

client = MongoClient()
db = client['info']
collection = db.users

app = Flask(__name__)


html = open('b.html').read()
# mongo1= open("Bd/users.js").read()

template = Template(html)
prob="\n"
@app.route("/")
def ip():

    head=str(request.headers)
    mas=head.split(' ')

    # return (template.render(name=str(request.remote_addr),name1=mas))
    # return (template.render(name=str(request.remote_addr)))
    return (template.render(name=str(collection.find_one())))



if __name__ == "__main__":
# app.run()
    app.run(host='0.0.0.0', port=1456)