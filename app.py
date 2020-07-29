#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: lingyuguo
 @contact: lingyuguo6240@163.com
 @Time : 2020/7/25 12:52
 
 """
from flask import Flask, request, render_template
from static import settings

app = Flask(__name__)
app.config.from_object(settings)
users = []      #存储用户数据
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/user", methods=["GET", "POST"])
def user():
    if request.method == "POST":
        username = request.form.get('username')      #获取form data
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        if repassword == password:       #密码一致性
            user = {"username": username,"password" : password}
            users.append(user)            #保存数据
            return "注册成功"
        else:
            return "两次密码不一致"
    return render_template("user.html")
@app.route("/show")
def show():
    return users

if __name__ == '__main__':
    app.run()