# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 窗口_QWidget.py
@Author : wenjing
@Date : 2023/1/4 15:38
"""
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class mywnd(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel('这是文字~')
        label.setStyleSheet('font-size:30px;color:red')
        label.setParent(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mywnd()
    # 设置窗口标题
    w.setWindowTitle('qwidget')
    w.show()
    app.exec()
