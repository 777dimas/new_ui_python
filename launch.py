import configparser, subprocess, time

config = configparser.ConfigParser()
config.read('launcher.ini')
auto_login = config.get('Options', 'Autologin')
serial = config.get('Options', 'Serial')
if auto_login and serial:
    while True:
        subprocess.call("wine launcher.exe", shell=True)
        time.sleep(5)

else:
    subprocess.call("./login_ui.py", shell=True)
