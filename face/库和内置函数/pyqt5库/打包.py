# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 打包.py
@Author : wenjing
@Date : 2023/1/11 10:31
"""
# windows系统打包只能打包成exe文件，mac可以打包成app
# 包含.ui文件的软件打包

# 1.首先使用QtDesigner设计一个界面，生成xxx.ui文件，
# 2.使用pyuic5命令生成对应的ui_xxx.py文件，
#       pyuic5 -o view_2.py view_2.ui
# 3.最后编写启动文件xxx.py
#       打开venv底下的Scripts文件夹,然后cmd,输出下列命令行
#       pyinstaller -F -w C:\Users\Mawenjing\PycharmProjects\PyQtDemo\wordcount_summary_view.py
