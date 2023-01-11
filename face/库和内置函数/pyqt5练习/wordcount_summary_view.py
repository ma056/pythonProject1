# -- coding: utf-8 --
import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5 import uic

import pymysql


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        # self.setupUi(self)
        # 【读取】功能
        self.init_ui()
        # self.button_read.clicked.connect(self.read)

    def init_ui(self):
        self.ui = uic.loadUi('./view_1.ui')
        # print(self.ui.__dict__) #输出所有控件的信息
        self.ho_name = self.ui.lineEdit  # ho_name输入框
        self.check_btn = self.ui.pushButton  # 查询按钮
        self.tableWidget = self.ui.tableWidget
        self.exit_btn = self.ui.pushButton_2  # 退出按钮
        self.clear_btn = self.ui.pushButton_3  # 清空数据按钮

        self.check_btn.clicked.connect(self.read)
        self.clear_btn.clicked.connect(self.buttonClear)
        self.exit_btn.clicked.connect(self.buttonExit)

    def buttonClear(self):
        self.tableWidget.setRowCount(0) # 连线一起清除
        # self.ho_name.clearContents()

    def buttonExit(self):
        sender = self.sender()
        print(sender.text() + ' 按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()

    # 【读取】按钮功能
    def read(self):
        # 数据库连接对象
        conn = pymysql.connect(
            # host="localhost",
            # port=3306,
            # user="root",
            # passwd="123123",
            # database="homework",
            # charset='utf8'
            host="engserver.westus.cloudapp.azure.com",
            port=3306,
            user="bi_report",
            password="pass@123",
            database="helios",
            charset='utf8',
        )
        # 游标对象
        cur = conn.cursor()
        # # 查询的sql语句
        # sql = "SELECT * FROM admin11 where "
        # where_ho_name = self.ho_name.text()
        # sql += "username = '" + where_ho_name + "'"
        # print(sql)
        # cur.execute(sql)
        sql = "SELECT * FROM wordcount_summary where "
        where_ho_name = self.ho_name.text()
        sql += "ho_name = '" + where_ho_name + "'"
        # print(sql)
        cur.execute(sql)
        # 获取查询到的数据, 是以二维元组的形式存储的, 所以读取需要使用 data[i][j] 下标定位
        data = cur.fetchall()
        # 打印测试
        # print(data)
        # print(data[0][1]) # 打印第1行第2个数据,

        # 遍历二维元组, 将 id 和 name 显示到界面表格上
        # x = 0
        # for i in data:
        #     y = 0
        #     for j in i:
        #         self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(data[x][y])))
        #         y = y + 1
        #     x = x + 1

        x = 0
        for i in data:
            y = 0
            row_count = self.tableWidget.rowCount()  # 返回当前行数(尾部)
            self.tableWidget.insertRow(row_count)  # 尾部插入一行
            for j in i:
                self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(data[x][y])))
                print(x,y)
                y = y + 1
            x = x + 1
        cur.close()
        conn.close()


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.ui.show()
    sys.exit(app.exec())
