#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QDesktopWidget

class ErrorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton("Ok", self)
        okButton.setGeometry(120, 10, 90, 30)
        okButton.clicked.connect(self.close)
        okButton.move(155, 90)

        self.setWindowTitle('Error')
        self.nameLabel = QLabel("Enter 'Login', 'Password' and 'Serial'", self)
        self.nameLabel.move(100, 40)
        self.setFixedHeight(150)
        self.setFixedWidth(400)
        self.center()
        self.show()

    def center(self):

        windowGeometry = self.frameGeometry()
        windowCenter = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(windowCenter)
        self.move(windowGeometry.topLeft())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = ErrorWindow()
    sys.exit(app.exec_())

