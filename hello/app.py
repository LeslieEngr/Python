from flask import Flask, render_template, request  
#Import module va class can thiet. Flask: class chinh cua framework, request: module cho phep truy cap
#thong tin ve cac yeu cau HTTP gui den may chu, render: module tao va render cac trang Http or mau.
app = Flask(__name__)

registrants = {}

@app.route("/", methods=["GET","POST"])
def index():

    return render_template("index.html")  

@app.route("/registrants", methods=["POST"])
def registrants():
    name = request.form.get("name")
    sport = request.form.get("sport")
    registrants[name] = sport
    return render_template("success.html")