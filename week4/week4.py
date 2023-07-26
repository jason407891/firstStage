from flask import request
from flask import redirect
from flask import Flask, render_template, jsonify
from flask import session



app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/static")

app.secret_key="jasonkey"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member_page():
    if session["loginstatus"]=="true":
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def handle_error():
    errormsg=request.args.get("message")
    return render_template("error.html",result=errormsg)

@app.route("/signin",methods=["POST","GET"])
def handle_signin():
    errormsg=""
    acc=request.form.get("account","")
    pas=request.form.get("password","")
    if acc=="" or pas=="":
        errormsg="Please enter username and password"
        return redirect("/error?message="+errormsg)
    elif acc=="test" and pas=="test":
        session["loginstatus"]="true"
        return redirect("/member")
    else:
        errormsg="Username or password is not correct"
        return redirect("/error?message="+errormsg)

@app.route("/logout")
def handle_logout():
    session["loginstatus"]="false"
    return redirect("/")



app.run(port=3000)