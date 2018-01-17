#!/usr/bin/python3
# -*- coding: utf-8 -*-
import configparser, subprocess, sys, time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QDesktopWidget, QMessageBox


class AuthWindow(QWidget):
    BUTTON_SIZES = [380, 70, 90, 30]

    def __init__(self):
        super().__init__()
        self.screen = app.primaryScreen()
        self.size = self.screen.size()
        self.fixed_width = 1920
        self.fixed_height = 1080

        self.config = configparser.ConfigParser()
        self.config.optionxform = str
        self.config.read('launcher.ini')

        self.login_edit = self.build_edit(90, 20, 215, 30)
        self.login_label = self.build_label("Login:", 48, 25)

        self.pass_edit = self.build_edit(90, 70, 215, 30)
        self.pass_label = self.build_label("Password:", 25, 75)

        self.serial_edit = self.build_edit(90, 120, 215, 30)
        self.serial_edit.setText(self.config.get('Options', 'Serial'))
        self.serial_label = self.build_label("Serial:", 48, 125)

        self.apply_btn = self.build_button("Apply", 90, 180, self.write_logins)
        self.close_btn = self.build_button("Close", 215, 180, self.close)

        self.setWindowTitle('- Autorization - ')
        self.setFixedHeight(250)
        self.setFixedWidth(400)
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(window_geometry.topLeft())
        self.show()

    def build_label(self, label_text, label_pos_x, label_pos_y):
        qlabel = QLabel(self)
        qlabel.setText(label_text)
        qlabel.move(label_pos_x, label_pos_y)
        return qlabel

    def build_edit(self, edit_x, edit_y, edit_pos_x, edit_pos_y):
        qline_edit = QLineEdit(self)
        qline_edit.move(edit_x, edit_y)
        qline_edit.resize(edit_pos_x, edit_pos_y)
        return qline_edit

    def build_button(self, btn_text, btn_pos_x, btn_pos_y, connect_method):
        qbutton = QPushButton(btn_text, self)
        qbutton.setGeometry(self.BUTTON_SIZES[0], self.BUTTON_SIZES[1], self.BUTTON_SIZES[2], self.BUTTON_SIZES[3])
        qbutton.clicked.connect(connect_method)
        qbutton.move(btn_pos_x, btn_pos_y)
        return qbutton

    def write_logins(self):
        if self.login_edit.text() and self.pass_edit.text() and self.serial_edit.text():
            login_and_pass_str = (self.login_edit.text() + ',' + self.pass_edit.text())
            self.config.set('Options', 'AutoLogin', login_and_pass_str)
            self.config.set('Options', 'Serial', self.serial_edit.text())
            with open('launcher.ini', 'w') as configfile:
                self.config.write(configfile)
            QWidget.close(self)
            while True:
                if self.size.width() == self.fixed_width and self.size.height() == self.fixed_height:
                    subprocess.call("wine launcher.exe", shell=True)
                    time.sleep(1)
                else:
                    subprocess.call("wine explorer /desktop=name,1280x1024 launcher.exe", shell=True)
                    time.sleep(1)
        else:
            QMessageBox.information(None, "Error", "Enter Login and Password",
                                    defaultButton=QMessageBox.Ok)

        subprocess.call(
            "rsync $args --password-file=/run/initramfs/memory/data/Progs/GlobalSlots/rsyncp -Lrv --progress --times --ignore-errors --delete-excluded  --force rsync://gup@update.gslots.win:49873/globalslots/plugins_dir/plugins/ ./plugins/ &",
            shell=True)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = AuthWindow()
    sys.exit(app.exec_())
