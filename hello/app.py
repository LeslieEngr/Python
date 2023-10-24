from flask import Flask, render_template, request  
#Import module va class can thiet. Flask: class chinh cua framework, request: module cho phep truy cap
#thong tin ve cac yeu cau HTTP gui den may chu, render: module tao va render cac trang Http or mau.
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name","world"))