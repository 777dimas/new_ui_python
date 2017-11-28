import configparser, subprocess

config = configparser.ConfigParser()
config.read('launcher.ini')
Login = config.get('Options', 'Logins')
if not Login:
    subprocess.call("/home/dima/PycharmProjects/new_ui_python/login_ui.py", shell=True)