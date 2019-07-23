import httplib
from jinja2 import Template
from flask import Flask
from flask import request
# from flask import jsonify
app = Flask(__name__)

html = open('c.html').read()
template = Template(html)

# conn = httplib.HTTPConnection("google.com")
# res = conn.getresponse()
# res.getheaders()


# @app.route("/")
# def hello():
#     return "Hello World"
@app.route("/")
def ip():
    # return jsonify({'ip': request.remote_addr}), 200
    return (template.render(name=str(request.remote_addr)))


if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port=4567)