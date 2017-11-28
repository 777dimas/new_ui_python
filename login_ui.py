#!/usr/bin/python3
# -*- coding: utf-8 -*-
import configparser
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.loginField = QLineEdit(self)
        self.loginField.move(90, 20)
        self.loginField.resize(215, 30)
        loginFieldName = QLabel(self)
        loginFieldName.setText("Логин:")
        loginFieldName.move(40, 25)

        self.passField = QLineEdit(self)
        self.passField.move(90, 70)
        self.passField.resize(215, 30)
        passFieldName = QLabel(self)
        passFieldName.setText("Пароль:")
        passFieldName.move(32, 75)

        button_set = QPushButton("Применить", self)
        button_set.setGeometry(380, 70, 90, 30)
        button_set.clicked.connect(self.writeLogins)
        button_set.clicked.connect(self.close)
        button_set.move(90, 130)

        closeButton = QPushButton("Закрыть", self)
        closeButton.setGeometry(380, 70, 90, 30)
        closeButton.clicked.connect(self.close)
        closeButton.move(215, 130)

        self.setWindowTitle('- Авторизация - ')
        self.setFixedHeight(200)
        self.setFixedWidth(400)
        self.show()

    def writeLogins(self):
        login = self.loginField.text()
        password = self.passField.text()
        loginValue = (login+','+password)
        config = configparser.ConfigParser()
        config.read('launcher.ini')
        config.set('Options', 'Logins', loginValue)
        with open('launcher.ini', 'w') as configfile:
            config.write(configfile)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())