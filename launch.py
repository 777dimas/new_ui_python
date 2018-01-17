import configparser, subprocess, time, sys
from PyQt5 import QtWidgets

subprocess.call("rsync $args --password-file=/run/initramfs/memory/data/Progs/GlobalSlots/rsyncp -Lrv --progress --times --ignore-errors --force rsync://gup@update.gslots.win:49873/globalslots/exe_dir/ ./", shell=True)

app = QtWidgets.QApplication(sys.argv)
screen = app.primaryScreen()
size = screen.size()
get_size = ('Size: %dx%d' % (size.width(), size.height()))
fixed_size = "1280x1024"

config = configparser.ConfigParser()
config.read('launcher.ini')
auto_login = config.get('Options', 'Autologin')
serial = config.get('Options', 'Serial')
if auto_login and serial:
    while True:
        if get_size > fixed_size:
            subprocess.call("wine explorer /desktop=name,1280x1024 launcher.exe", shell=True)
            time.sleep(1)
        else:
            subprocess.call("wine launcher.exe", shell=True)
            time.sleep(1)
else:
    subprocess.call("./login_ui.py", shell=True)