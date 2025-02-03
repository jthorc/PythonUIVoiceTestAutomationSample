import os

PROJECT_ROOT = os.getcwd()
ICO_PATH = os.path.join('ico')
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