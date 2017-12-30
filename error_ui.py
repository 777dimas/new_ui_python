#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QDesktopWidget


class ErrorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        ok_btn = QPushButton("Ok", self)
        ok_btn.setGeometry(120, 10, 90, 30)
        ok_btn.clicked.connect(self.close)
        ok_btn.move(155, 90)

        self.setWindowTitle('Error')
        self.label_name = QLabel("Enter 'Login', 'Password' and 'Serial'", self)
        self.label_name.move(100, 40)
        self.setFixedHeight(150)
        self.setFixedWidth(400)
        self.center()
        self.show()

    def center(self):

        window_geometry = self.frameGeometry()
        window_center = QDesktopWidget().availableGeometry().center()
        window_geometry.moveCenter(window_center)
        self.move(window_geometry.topLeft())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = ErrorWindow()
    sys.exit(app.exec_())

