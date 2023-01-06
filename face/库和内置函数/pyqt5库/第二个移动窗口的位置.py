# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 第二个移动窗口的位置.py
@Author : wenjing
@Date : 2023/1/4 13:37
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QDesktopWidget

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

    # 将窗口设置再屏幕的左上角
    # w.move(0,0)
    # 调整窗口在屏幕中央显示
    center_pointer = QDesktopWidget().availableGeometry().center()
    x = center_pointer.x()
    y = center_pointer.y()
    # w.move(x, y)
    # w.move(x-150, y-150)
    print(w.frameGeometry())
    print(w.frameGeometry().getRect())
    print(type(w.frameGeometry().getRect()))
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(x - width / 2, y - height / 2)
    # 展示窗口
    w.show()
    ## 5.程序开始运行程序，直到关闭了窗口
    # 程序进行循环等待状态
    app.exec()
