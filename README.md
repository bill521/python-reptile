# python_reptile

## 项目介绍

```
爬取抖音视频脚本
``` 

## 批量安装依赖包
```commandline
pip install -r requirements.txt
```

## 打包成exe执行文件 
```commandline
安装
pip install -i https://pypi.douban.com/simple/ pyinstaller #豆瓣源
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller #清华源
```

## 打包成exe
```commandline
安装
Pyinstaller -F -i logo.ico -n spider main.py
```

## 命令使用
```commandline

下载抖音单个分享视频：
dys 分享视频地址
下载个人主页所有视频
dyb 个人首页地址

```




## 依赖包写入 requirements.txt
```commandline
pip freeze > requirements.txt
```
