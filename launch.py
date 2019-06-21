import configparser, subprocess, time, sys
from PyQt5 import QtWidgets

subprocess.call("rsync $args --password-file=/run/initramfs/memory/data/Progs/GlobalSlots/rsyncp -Lrv --progress --times --ignore-errors --force rsync://my@update.bug.com:1111/globalslots/plugins_dir/plugins/ ./", shell=True)

app = QtWidgets.QApplication(sys.argv)
screen = app.primaryScreen()
size = screen.size()
fixed_width = 1280
fixed_height = 1024

config = configparser.ConfigParser()
config.read('launcher.ini')
auto_login = config.get('Options', 'AutoLogin')
serial = config.get('Options', 'Serial')
if auto_login and serial:
    while True:
        if size.width() == fixed_width and size.height() == fixed_height:
            subprocess.call("wine launcher.exe", shell=True)
            time.sleep(1)
        else:
            subprocess.call("wine explorer /desktop=name,1280x1024 launcher.exe", shell=True)
            time.sleep(1)
else:
    subprocess.call("./login_ui.py", shell=True)
