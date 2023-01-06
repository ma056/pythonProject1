# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 窗口_QMainWindow.py
@Author : wenjing
@Date : 2023/1/4 15:45
"""
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel('这是文字')
        label.setStyleSheet('font-size:30px;color:red')

        # 调用父类中的menuBar,从而对菜单栏进行操作
        menu = self.menuBar()
        # 如果是Mac的话，菜单栏不会在Window中显示而是屏幕顶部系统菜单栏位置
        # 下面这一行代码使得Mac也按照Windows的那种方式在Window中显示Menu
        menu.setNativeMenuBar(False)
        file_menu = menu.addMenu('文件')
        file_menu.addAction('新建')
        file_menu.addAction('打开')
        file_menu.addAction('保存')

        edit_menu = menu.addMenu('编辑')
        edit_menu.addAction('复制')
        edit_menu.addAction('粘贴')
        edit_menu.addAction('剪切')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle('我是窗口标题')
    w.show()
    app.exec()

