# 辅助函数
import json
# 定义返回结构
def ajaxReturn(info,data=[]):
    info['data'] = data
    return json.dumps(info)