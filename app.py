from flask import Flask, url_for, request, render_template
from wsgiref.simple_server import make_server
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route("/<int:name>")
def hello1(name):
    return f"<a>Hello, {escape(name)} int</a>"

@app.route("/<string:name>")
def hello2(name):
    return f"<a>Hello, {escape(name)} string</a>"

@app.route("/rest", methods=["GET", "POST"])
def rest():
    if request.method == "GET":
        return "GET"
    else:
        return "POST"
    
@app.route("/hello/")
@app.route("/hello/<name>")
def hello3(name=None):
    return render_template("hello.html", name=name)

if __name__ == "__main__":
    with app.test_request_context():
        print(url_for("hello2", name="strabc", next='strababc'))

    if 1:
        app.async_to_sync
        app.debug = True
        app.run()
    else:
        server = make_server("127.0.0.1", 5000, app)
        print("Running on http://127.0.0.1:5000")
        server.serve_forever()