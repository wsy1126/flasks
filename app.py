from flask import Flask, url_for, request, session, flash, render_template, make_response, abort, redirect
from wsgiref.simple_server import make_server
from markupsafe import escape
import time
app = Flask(__name__)

# 普通的
@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"

# 带格式验证的变量
@app.route("/var/<int:name>")
def hello1(name):
    return f"<a>Hello, {escape(name)} int</a>"

# 带格式验证的变量
@app.route("/var/<string:name>")
def hello2(name):
    return f"<a>Hello, {escape(name)} string</a>"

# restful接口
@app.route("/rest", methods=["GET", "POST"])
def rest():
    if request.method == "GET":
        return "GET"
    else:
        return "POST"

# 多路由+渲染模板
@app.route("/hello/")
@app.route("/hello/<name>")
def hello3(name=None):
    return render_template("hello.html", name=name)

# 测试POST
@app.route("/post", methods=["POST"])
def hello4():
    return "success POSTed"

# 上传
@app.route("/upload", methods=["POST"])
def upload_file():
    f = request.files['the_file']
    f.save(F"./uploads/{time.time()}.png")
    return "successful"

# cookie
@app.route("/cookes/")
def coo():
    username = request.cookies.get("username")
    print(F"{username} is visiting")
    password = request.cookies.get("password")
    resp = make_response(render_template("hello.html"))
    resp.set_cookie("username", username)
    resp.set_cookie("password", password)
    return resp

# 错误处理
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>page not found</h1>", 401

# 引发错误
@app.route("/401")
def raise_error():
    abort(401)

# 重定向
@app.route("/402")
def jumper():
    return redirect(url_for("raise_error"))

# session
def get_secret_key():
    import secrets
    return secrets.token_hex()

## app.secret_key = br'_5#y2L"F4Q8z\n\xec]/'
app.secret_key = get_secret_key()
{"username": "jjooee", "password": "abc123"}
@app.route("/login", methods=["POST"])
def login():
    if request.form["username"] == "jjooee":
        session["username"] = request.form["username"]
        return "login successed"
    else:
        return "login failed"

@app.route("/secret")
def secret():
    if request.form["username"] in session.values():
        return "visiting secret thing"
    else:
        return "visiting failed"

@app.route("/logout")
def logout():
    session.pop("username", None)
    return "logout successed"

# 消息闪现
# flash.py

# 日志
# 标准的日志类
from logging import basicConfig, DEBUG
basicConfig(filename='app.log', level=DEBUG, format='%(levelname)s %(asctime)s %(message)s')
@app.route("/log")
def logg():
    app.logger.debug("A value for debuging")
    return "logging"



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