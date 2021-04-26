from pywinauto import application
import time
import os
import pyautogui

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
os.system('wmic process where "name like \'%DibServer%\'" call terminate')
time.sleep(5)        

app = application.Application()
app.start('C:\CREON\STARTER\coStarter.exe /prj:cp /id:yourid /pwd:yourpwd /pwdcert:yourpwdcert /autostart')
time.sleep(60)

# 팝업창 취소 버튼 클릭
c = pyautogui.locateCenterOnScreen('cancel.PNG')
pyautogui.click(c)
time.sleep(60)