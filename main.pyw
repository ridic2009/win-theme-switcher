import time
import subprocess
import os
import winreg

user = os.getlogin()

dark_theme = f'C:\\Users\\{user}\\AppData\\Local\\Microsoft\\Windows\\Themes\\Planets Dark\\PlanetsDark.theme'
light_theme = f'C:\\Users\\{user}\\AppData\\Local\\Microsoft\\Windows\\Themes\\Planets Light\\PlanetsLight.theme'

current_theme = None

def get_current_theme():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize')
    theme, _ = winreg.QueryValueEx(key, 'AppsUseLightTheme')
    return 'light' if theme else 'dark'

def switch_theme(theme: str): 
    subprocess.run(["powershell", "-Command", f'start-process -filepath "{theme}"; timeout /t 1; taskkill /im "systemsettings.exe" /f'], shell=True)


def main():
    while True:
        current_time = time.localtime()
        hour = current_time.tm_hour

        if 6 <= hour < 18:
            if get_current_theme() != 'light':
                switch_theme(light_theme)
        else:
            if get_current_theme() != 'dark':
                switch_theme(dark_theme)

        time.sleep(1)

if __name__ == '__main__':
    main()


