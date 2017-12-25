import configparser, subprocess

config = configparser.ConfigParser()
config.read('launcher.ini')
auto_login = config.get('Options', 'Autologin')
serial = config.get('Options', 'Serial')
if auto_login or serial:
    while True:
        subprocess.call("cd /home/dima/PycharmProjects/new_ui_python/ && wine launcher.exe", shell=True)
else:
    subprocess.call("./login_ui.py", shell=True)
