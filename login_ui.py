#!/usr/bin/python3
# -*- coding: utf-8 -*-
import configparser, subprocess
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QDesktopWidget

class AuthWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.config = configparser.ConfigParser()
        self.config.optionxform = str
        self.config.read('launcher.ini')
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
        self.serialField.setText(self.config.get('Options', 'Serial'))

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
        centerWindow = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(centerWindow)
        self.move(windowGeometry.topLeft())


    def writeLogins(self):
        login = self.loginField.text()
        password = self.passField.text()
        serial = self.serialField.text()
        if login and password and serial:
            loginValue = (login + ',' + password)
            self.config.set('Options', 'Autologin', loginValue)
            self.config.set('Options', 'Serial', serial)
            with open('launcher.ini', 'w') as configfile:
                self.config.write(configfile)
        else:
            subprocess.call("./error_ui.py", shell=True)
        while True:
            subprocess.call("cd /home/flash/Progs/GlobalSlots/ && wine launcher.exe", shell=True)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = AuthWindow()
    sys.exit(app.exec_())
