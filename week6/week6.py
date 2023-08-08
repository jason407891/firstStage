from flask import request
from flask import redirect
from flask import Flask, render_template, jsonify
from flask import session
import mysql.connector
import datetime

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/static")

app.secret_key="jasonkey"

conn = mysql.connector.connect(
    host="NO-20230525204903",
    user="jason",
    password="12tina28",
    database="website"
)

cursor=conn.cursor()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member_page():
    if session["login"]=="true":
        name=session['name']
        select_query = """
            SELECT message.content, member.name 
            FROM message 
            JOIN member ON message.member_id = member.id
            ORDER BY message.time DESC
        """
        cursor.execute(select_query)
        contents = cursor.fetchall()

        return render_template("member.html",result=name,contents=contents)
    else:
        return redirect("/")

@app.route("/error")
def handle_error():
    errormsg=request.args.get("message")
    return render_template("error.html",result=errormsg)

@app.route("/signup",methods=["POST"])
def handle_signup():
    username=request.form.get("username","")
    account=request.form.get("account","")
    password=request.form.get("password","")
    sql= "SELECT COUNT(*) FROM member WHERE username = %s"
    cursor.execute(sql, (account,))
    count = cursor.fetchone()[0]
    if count>0:
        errormsg="帳號已經被註冊"
        return redirect("/error?message="+errormsg)
    else:
        sql="INSERT INTO member (name, username, password, follower_count, time) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql,(username, account, password, 0, datetime.datetime.now()))
        conn.commit()
        return redirect("/")


@app.route("/login",methods=["POST"])
def handle_signin():
    acc=request.form.get("account","")
    pas=request.form.get("password","")
    cursor=conn.cursor()
    sql = "SELECT * FROM member WHERE username = %s AND password = %s"
    cursor.execute(sql, (acc, pas))
    result = cursor.fetchone()
    # 若查詢結果不為 None，表示帳號和密碼驗證成功
    if result:
        # 將會員的 ID、帳號和姓名等資訊加入 Session 中紀錄，表示登入成功
        session['login']= "true"
        session['user_id'] = result[0]  # 假設 ID 欄位在第一個位置
        session['name'] = result[1]  # 假設 name 欄位在第三個位置
        session['username'] = result[2]  # 假設 username 欄位在第二個位置
        return redirect("/member")  # 導向到會員頁面
    else:
        errormsg="帳號或密碼輸入錯誤"
        return redirect("/error?message="+errormsg)  # 導向到登入失敗頁面



@app.route("/sendmsg",methods=['POST'])
def handle_sendmsg():
    msg=request.form.get("msg","")
    insert_query = "INSERT INTO message (member_id, content, like_count, time) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (session['user_id'], msg, 0, datetime.datetime.now()))
    conn.commit()
    return redirect("/member")
    

@app.route("/logout")
def handle_logout():
    session.pop('login',None)
    session.pop('user_id',None)
    session.pop('username',None)
    session.pop('name',None)
    return redirect("/")



app.run(port=3000)