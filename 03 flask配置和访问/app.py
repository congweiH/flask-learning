from flask import Flask
import config  # 导入配置文件

"""
1 __name__ 是 "__main__" ，模块名
2 这里的 Flask 是一个类，生成 app 对象
3 WSGI:web server gateway interface(web服务器网关接口)
    是为python语言定义的web服务器和框架(flask,django等)之间的一种简单而通用的接口
    连接 web服务器 和 框架, 一个规则，大家默认的协议
4 flask有内置的服务器，但是可以不用这个默认的服务器，可以换成别的服务器，比如nginx
"""
app = Flask(__name__)

"""
app.config 里面是一些配置，以键值对给出
ENV : 环境, 有production、development、testing
DEBUG : 调试模式，默认为 False
详细内容可以打印app.config查看
"""
# print(app.config)
# # 修改环境
# app.config["ENV"] = "development"
# # 修改为调试模式
# app.config["DEBUG"] = True

"""
也可以将配置信息放入到配置文件config.py中，然后加载配置文件
一般采用这种方式
"""
app.config.from_object(config)

"""
@:装饰器
route:路由
"""
@app.route('/')  # 路由  url  '/' 默认主页
def index():  # 视图函数 view
    return 'Hello World!'


"""
可以加载html标签
"""
@app.route('/test')
def test():
    return '<font color="red"> test </font>'


if __name__ == '__main__':
    """
        1 可以更换ip地址 或 端口号
            app.run(host="IP地址",port="端口号")
            如果需要外网访问，ip地址改为 0.0.0.0
            默认情况只能本机访问，即localhost
        2 debug 模式   常用于开发阶段
            app.run(debug=True)
            代码内容改变时，按保存（ctrl+s）服务器会自动重新启动，再刷新网页时，内容会更改（如果修改了网页的内容）
            问题：如果无法进入debug模式的话，参考 https://my.oschina.net/yimingkeji/blog/2875817
            也可以通过app.config["DEBUG"] = "True"配置
   """
    # app.run(debug=True)
    app.run()
