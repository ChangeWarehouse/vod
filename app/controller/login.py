from app.controller import admin
from flask import render_template,request
from app.code.code import StatusCode
from app.helper.func import ajaxReturn
# 登陆
@admin.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip() if request.form.get('username') else ''
        username =""
        password = request.form.get('password').strip() if request.form.get('password') else ''
        if not username or not password:
            return ajaxReturn(StatusCode.A90000,data={"username":"fq"})
        # 查库  如果说用户名或者密码正确，我是可以重定向到系统内部，如果错误，我怎么办？failure+1 lock


    return render_template('login/login.html')