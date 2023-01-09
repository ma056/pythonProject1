# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : qt-designer_2.py
@Author : wenjing
@Date : 2023/1/9 16:18
多进程
"""
import sys
import time
from PyQt5 import uic
from PyQt5.Qt import QApplication, QWidget, QThread


class MyThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(10):
            print('是线程中执行....%d' % (i + 1))
            time.sleep(1)


class MyWin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi('./thread.ui')
        # 从ui文件中加载控件
        lineedit = self.ui.lineEdit
        btn1 = self.ui.pushButton
        btn2 = self.ui.pushButton_2

        # 给2个按钮绑定槽函数
        btn1.clicked.connect(self.click_1)
        btn2.clicked.connect(self.click_2)

    def click_1(self):
        for i in range(10):
            print('是UI线程中执行....%d' % (i + 1))
            time.sleep(1)

    def click_2(self):
        self.my_thread = MyThread()  # 创建线程
        self.my_thread.start()  # 开始线程


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWin()
    w.ui.show()
    app.exec()