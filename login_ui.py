#!/usr/bin/python3
# -*- coding: utf-8 -*-
import configparser
import sys

import PyQt5.QtWidgets


class Example(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
     #   config = configparser.ConfigParser()
     #   config.read('launcher.ini')
     #   login = config.get('Options', 'Logins')

        name_set = PyQt5.QtWidgets.QLineEdit(self)
        name_set.move(90, 20)
        name_set.resize(215, 30)

        pass_set = PyQt5.QtWidgets.QLineEdit(self)
        pass_set.move(90, 70)
        pass_set.resize(215, 30)

        button_set = PyQt5.QtWidgets.QPushButton("Set", self)
        button_set.setGeometry(380, 70, 90, 30)
       # button_set.clicked.connect(self.buttonSet)
        button_set.move(90, 130)

        button_close = PyQt5.QtWidgets.QPushButton("Close", self)
        button_close.setGeometry(380, 70, 90, 30)
        #button_close.clicked.connect(self.closeEvent)
        button_close.move(215, 130)

        self.setWindowTitle('Login')
        self.setFixedHeight(200)
        self.setFixedWidth(400)
        self.show()
        rectangle = self.frameGeometry()
        centerPoint = PyQt5.QtWidgets.QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(centerPoint)
        self.move(rectangle.topLeft())

   # def buttonSet(self):
   #     config = configparser.ConfigParser()
   #     config.read('launcher.ini')
   #     config.set('Options', 'Logins', self.())
   #     with open('launcher.ini', 'w') as configfile:
   #         config.write(configfile)

   # def buttonClose(self):



if __name__ == '__main__':

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())