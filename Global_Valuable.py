import os
from datetime import datetime
import json

PROJECT_ROOT = os.getcwd()
ICO_PATH = os.path.join('ico')

CURRENT_DIR = os.getcwd()
CURRENT_TIME = datetime.now().strftime('%Y-%m-%d_%H%M%S')
CONFIG_FILE_NAME = 'config_file.json'
CONFIG_FILE_FULL_PATH = os.path.join(CURRENT_DIR,CONFIG_FILE_NAME)

#load configuration
with open(CONFIG_FILE_FULL_PATH, "r") as file:
    config_data = json.load(file)

ADB_DEVICES = ['adb devices',
                  'adb root',
                  'adb remount']
ADB_CONNECTION = ['adb connect 192.168.1.10']
PING_CONNECTION = ['ping 192.168.1.10']
SCRCPY_FOLDER = 'scrcpy-win64-v3.1'
SCRCPY_EXE = 'scrcpy.exe'
#RUN_SCRCPY = os.path.join(SCRCPY_FOLDER,SCRCPY_EXE) + "-s 192.168.1.10"
RUN_SCRCPY = [os.path.join(SCRCPY_FOLDER,SCRCPY_EXE)]
RUN_GITHUB = ['C:\\Users\\jiang\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe']
GITHUB_NAME = config_data["github_exe_name"]
CONFIG_EDITOR_NAME = config_data["config_editor_name"]

RUN_CONFIG_EDITOR = ['Python',f'{os.path.join(CURRENT_DIR,CONFIG_EDITOR_NAME)}']