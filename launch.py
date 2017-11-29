import configparser, subprocess

config = configparser.ConfigParser()
config.read('launcher.ini')
Login = config.get('Options', 'Logins')
serial = config.get('Options', 'serial')
if not Login or serial:
    subprocess.call("/home/dima/PycharmProjects/new_ui_python/login_ui.py", shell=True)