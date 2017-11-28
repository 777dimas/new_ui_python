#!/usr/bin/python3
# -*- coding: utf-8 -*-
import configparser
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton

class AuthWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.loginField = QLineEdit(self)
        self.loginField.move(90, 20)
        self.loginField.resize(215, 30)
        loginFieldName = QLabel(self)
        loginFieldName.setText("Login:")
        loginFieldName.move(48, 25)

        self.passField = QLineEdit(self)
        self.passField.move(90, 70)
        self.passField.resize(215, 30)
        passFieldName = QLabel(self)
        passFieldName.setText("Password:")
        passFieldName.move(25, 75)

        self.serialField = QLineEdit(self)
        self.serialField.move(90, 120)
        self.serialField.resize(215, 30)
        serialFieldName = QLabel(self)
        serialFieldName.setText("Serial:")
        serialFieldName.move(48, 125)

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
        self.show()

    def writeLogins(self):
        login = self.loginField.text()
        password = self.passField.text()
        serial = self.serialField.text()
        loginValue = (login+','+password)
        config = configparser.ConfigParser()
        config.read('launcher.ini')
        config.set('Options', 'Logins', loginValue)
        config.set('Options', 'serial', serial)
        with open('launcher.ini', 'w') as configfile:
            config.write(configfile)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = AuthWindow()
    sys.exit(app.exec_())
