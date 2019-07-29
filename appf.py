import httplib
from jinja2 import Template
from flask import Flask
from flask import request
from pymongo import MongoClient

client = MongoClient()
db = client['info']
collection = db.users

app1= Flask(__name__)


html = open('c.html').read()
# mongo1= open("Bd/users.js").read()

template = Template(html)
prob="\n"
@app1.route("/")
def ip():

    post_str = []
    # for post in collection.find({"age": {"$lt": 30}}).sort("name"):
    for post in collection.find():
        post_str.append(str(post))

    # return (template.render(name=str(request.remote_addr),name1=mas))
    # return (template.render(name=str(request.remote_addr)))
    return (template.render(name=post_str))

if __name__ == "__main__":
# app.run()
    app1.run(host='0.0.0.0', port=1454)