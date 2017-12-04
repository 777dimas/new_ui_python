#!/usr/bin/python3
# -*- coding: utf-8 -*-
import configparser, subprocess
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QDesktopWidget

class AuthWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.login_field = QLineEdit(self)
        self.login_field.move(90, 20)
        self.login_field.resize(215, 30)
        login_field_name = QLabel(self)
        login_field_name.setText("Login:")
        login_field_name.move(48, 25)

        self.pass_field = QLineEdit(self)
        self.pass_field.move(90, 70)
        self.pass_field.resize(215, 30)
        pass_field_name = QLabel(self)
        pass_field_name.setText("Password:")
        pass_field_name.move(25, 75)

        self.serial_field = QLineEdit(self)
        self.serial_field.move(90, 120)
        self.serial_field.resize(215, 30)
        serial_field_name = QLabel(self)
        serial_field_name.setText("Serial:")
        serial_field_name.move(48, 125)

        button_set = QPushButton("Apply", self)
        button_set.setGeometry(380, 70, 90, 30)
        button_set.clicked.connect(self.writeLogins)
        button_set.clicked.connect(self.close)
        button_set.move(90, 180)

        closeButton = QPushButton("Close", self)
        closeButton.setGeometry(380, 70, 90, 30)
        closeButton.clicked.connect(self.close)
        closeButton.move(215, 180)

        self.setWindowTitle('- Autorization - ')
        self.setFixedHeight(250)
        self.setFixedWidth(400)
        self.center()
        self.show()

    def center(self):

        windowGeometry = self.frameGeometry()
        windowCenter = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(windowCenter)
        self.move(windowGeometry.topLeft())

    def writeLogins(self):

        login = self.login_field.text()
        password = self.pass_field.text()
        serial = self.serial_field.text()
        if not login or not password or not serial:
            subprocess.call("/home/dima/PycharmProjects/new_ui_python/error_ui.py", shell=True)
        else:
            login_value = (login+','+password)
            config = configparser.ConfigParser()
            config.read('launcher.ini', encoding='utf-8')
            config.set('Options', 'Autologin', login_value)
            config.set('Options', 'Serial', serial)
            with open('launcher.ini', 'w') as configfile:
                config.write(configfile)
       # subprocess.call("cd /home/flash/Progs/GlobalSlots/ && wine launcher.exe", shell=True)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = AuthWindow()
    sys.exit(app.exec_())
