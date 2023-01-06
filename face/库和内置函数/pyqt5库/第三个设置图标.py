# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 第三个设置图标.py
@Author : wenjing
@Date : 2023/1/4 13:56
"""
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建一个QWidget
    w = QWidget()
    w.setWindowTitle('看图标')
    w.setWindowIcon(QIcon('座位图.png'))
    w.show()

    app.exec()