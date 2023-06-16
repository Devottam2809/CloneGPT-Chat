from flask import Flask,render_template,jsonify,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/api",methods=["GET","POST"])
def qa():
    if request.method=="POST":
        data={"result":"This is working"}
        return jsonify(data)
    data={"result":"This is working"}
    return jsonify(data)
    return render_template("index.html")
app.run(debug=True)