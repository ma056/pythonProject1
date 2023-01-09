# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : qt_designer_1.py
@Author : wenjing
@Date : 2023/1/9 15:47
"""
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi('./login-1.ui')
        # print(self.ui.__dict__) #输出所有控件的信息
        self.user_name_qwidget = self.ui.lineEdit  # 用户名输入框
        self.password_qwidget = self.ui.lineEdit_2  # 密码输入框
        self.login_btn = self.ui.pushButton  # 登录按钮
        self.forget_password_btn = self.ui.pushButton_2  # 忘记密码按钮
        self.textBrower = self.ui.textBrowser  # 文本显示区域

        self.login_btn.clicked.connect(self.login)

    def login(self):
        '''登录按钮的槽函数'''
        user_name = self.user_name_qwidget.text()
        password = self.password_qwidget.text()
        for i in range(10):
            print('正在登陆服务器。。%s'%(i+1))
            time.sleep(1)

        if user_name == 'admin' and password == '123456':
            self.textBrower.setText('欢迎%s' % user_name)
            self.textBrower.repaint()
        else:
            self.textBrower.setText('用户名或密码错误')
            self.textBrower.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    app.exec()