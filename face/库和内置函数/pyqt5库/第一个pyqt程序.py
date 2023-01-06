# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 第一个pyqt程序.py
@Author : wenjing
@Date : 2023/1/4 11:14
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

if __name__ == '__main__':
    ## 1.只要是QT制作的app,必须有且只有1个QApplication对象
    ## 2.sys.argv当作参数的目的是将运行时的命令参数传递给QApplication对象
    app = QApplication(sys.argv)
    ## 3.创建了一个QWidget对象，将它的标题设置为：’第一个PyQt‘
    ## 4.然后调用show方法显示出来
    w = QWidget()
    # 设置窗口标题
    w.setWindowTitle('第一个pyqt程序')
    # 设置窗口的大小
    w.resize(300, 300)
    # 下面创建一个Label（纯文本），在创建的时候指定了父对象
    label = QLabel("账号: ", w)
    label.setGeometry(20, 20, 30, 20)

    # 文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText('请输入账号')
    edit.setGeometry(55, 20, 200, 20)

    # 再窗口里面添加控件
    btn = QPushButton("按钮", w)
    # 设置按钮的父亲时当前窗口，等于是添加到窗口种显示
    # btn.setParent(w)
    btn.setGeometry(50, 80, 70, 30)

    # 展示窗口
    w.show()
    ## 5.程序开始运行程序，直到关闭了窗口
    # 程序进行循环等待状态
    app.exec()
