#处理用户相关的
from app.controller import admin

@admin.route('/')
def index():
    return 'user-index'