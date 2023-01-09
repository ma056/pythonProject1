# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : QT_Designer.py
@Author : wenjing
@Date : 2023/1/6 14:57
"""
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi('/test.ui')
    # 展示窗口
    ui.show()

    app.exec()


