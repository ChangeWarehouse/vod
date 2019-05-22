# 引入flask
from flask import Flask

# 定义函数

def create_app():
    app = Flask(__name__,template_folder='views')
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    register_blueprint(app) # 注册蓝图
    return app

# 注册蓝图
def register_blueprint(app):
    from app.controller import admin
    app.register_blueprint(admin)



