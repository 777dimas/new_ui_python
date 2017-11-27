#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, configparser
from PyQt5.QtWidgets import (QPushButton, QLabel, QDesktopWidget, QWidget, QMessageBox, QApplication, QComboBox)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        config = configparser.ConfigParser()
        config.read('launcher.original.ini')
        Login = config.get('Options', 'Logins')
        addlogins = Login.split(",")

        self.lbl = QLabel("Logins", self)
        self.combo = QComboBox(self)
        self.combo.addItems(addlogins)

        self.combo.move(50, 50)
        self.lbl.move(50, 30)

        btn = QPushButton('Set', self)
        btn.setGeometry(230, 50, 42, 32)
        btn.clicked.connect(self.buttonSet)

        self.resize(350, 140)
        self.center()
        self.setWindowTitle('Message box')
        self.show()

        self.setWindowTitle('Launcher')
        self.show()

    def buttonSet(self):#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, configparser
from PyQt5.QtWidgets import (QPushButton, QLabel, QDesktopWidget, QWidget, QMessageBox, QApplication, QComboBox)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        config = configparser.ConfigParser()
        config.read('launcher.original.ini')
        Login = config.get('Options', 'Logins')
        addlogins = Login.split(",")

        self.lbl = QLabel("Logins", self)
        self.combo = QComboBox(self)
        self.combo.addItems(addlogins)

        self.combo.move(50, 50)
        self.lbl.move(50, 30)

        btn = QPushButton('Set', self)
        btn.setGeometry(230, 50, 42, 32)
        btn.clicked.connect(self.buttonSet)

        self.resize(350, 140)
        self.center()
        self.setWindowTitle('Message box')
        self.show()

        self.setWindowTitle('Launcher')
        self.show()

    def buttonSet(self):
        config = configparser.ConfigParser()
        config.read('launcher.ini')
        config.set('Options', 'Autologin', self.combo.currentText())
        with open('launcher.ini', 'w') as configfile:
            config.write(configfile)

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        config = configparser.ConfigParser()
        config.read('launcher.ini')
        config.set('Options', 'Autologin', self.combo.currentText())
        with open('launcher.ini', 'w') as configfile:
            config.write(configfile)

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
