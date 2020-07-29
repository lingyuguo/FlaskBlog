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


@app.route("/index")
def index():
    return  render_template("index.html")
@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/index1", methods=["GET"])
def index1():
    username = request.args.get('username')
    password = request.args.get('password')
    dict={}
    dict[username]=password
    return dict

@app.route("/index2", methods=["GET", "POST"])
def index2():
    username = request.form.get('username')
    password = request.form.get('password')
    dict={}
    dict[username]=password
    return dict

if __name__ == '__main__':
    app.run()