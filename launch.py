import configparser, subprocess

config = configparser.ConfigParser()
config.read('launcher.ini')
auto_login = config.get('Options', 'Autologin')
serial = config.get('Options', 'Serial')
if not auto_login or not serial:
    subprocess.call("/home/dima/PycharmProjects/new_ui_python/login_ui.py", shell=True)
#else:
 #   subprocess.call("cd /home/dima/PycharmProjects/new_ui_python/ && wine launcher.exe", shell=True)
