参考教程视频  https://www.bilibili.com/video/BV17z4y1X7UZ



# 虚拟环境

1 下载virtualenv包

```text
pip install virtualenv
```

2 下载virtualenvwrapper包

```text
pip install virtualenvwrapper-win
```

3 配置环境存放的目录

创建环境变量

```text
WORKON_HOME = "D:\env\pythonenv"
```

完成后记得重新打开cmd！！！

4 创建虚拟环境

```text
1. 默认基于系统的python环境创建
mkvirtualenv temp	 
2. 如果电脑上有多个python版本,可以指定基于哪个python版本创建
mkvirtualenv temp --python=C:\Python\Python366\python.exe  
```

5 退出虚拟环境

```text
deactivate
```

6 列出所有虚拟环境

```text
lsvirtualenv
```

7 进入或者切换环境

```text
workon temp
```

8 删除虚拟环境

```text
rmvirtualenv test10
```

9 列出环境内安装包的情况

```text
pip list
```



# 项目结构

```text
--项目名
   |---static  	(静态,存放css,js)
   |---template (模板,存放html)
   |---app.py 	(运行|启动)
```



# web模式

传统web模式

```text
mvc:
m  	(model 模型, 和数据库相关)
v	(view 视图, 展示给用户看的部分)
c	(controler, 控制器, 处理请求)
```

python-web模式

```text
mtv:
m	(model 模型,和数据库相关)
t	(template 模板, 展示给用户看的部分, html)
v	(view 其控制作用, python代码)
```



mvc 和 mtv 类似，只是换了个名字。


