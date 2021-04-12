import pyautogui as py
import time
import os
from os import startfile
from datetime import date
import cv2

#reference from - https://pyautogui.readthedocs.io/en/latest/index.html
#program by Mugunth aka C05M1C.
#DISCLAIMER : This program is only for educational purposes

def wait(t,m):
    cur=getTime()
    while cur[0]!=t and cur[1]!=m:
        pass
    else:
        py.click('leave.png')
def join(end_t,end_m):
    py.click('join.png')
    py.sleep(10)
    py.click('muteMic.png')
    py.click('joinNow.png')
    exit(end_t,end_m)

def getTime():
    today = date.today()
    t = time.localtime()
    curTime=[]
    curTime.append(t.tm_hour)
    curTime.append(t.tm_min)
    curTime.append(today)
    return curTime

def math():
    try:
        py.doubleClick('math.png')
    except:
        py.doubleClick('mathStarted.png')
    py.sleep(3)
    join()

def aptitude():
    py.doubleClick('aptitude.png')
    py.sleep(3)
    join()

def env():
    py.doubleClick('env.png')
    py.sleep(3)
    join()

def os():
    today=getTime()
    day=today[2]
    if day=="Tuesday":
        py.doubleClick('C:\\Users\jcmug\PycharmProjects\\teams automation\os\osTuesday.png')
        py.sleep(3)
        join()
    elif day=="Wednesday":
        py.doubleClick('C:\\Users\jcmug\PycharmProjects\\teams automation\os\osWednesday.png')
        py.sleep(3)
        join()
    elif day=="Thursday":
        py.doubleClick('C:\\Users\jcmug\PycharmProjects\\teams automation\os\osThursday.png')
        py.sleep(3)
        join()
    return

def osLab():
    py.doubleClick('osLab.png')
    py.sleep(3)
    join()


def avp():
    py.doubleClick('avp.png')
    py.sleep(3)
    join()

def verbal():
    py.doubleClick('verbal.png')
    py.sleep(3)
    join()

def universal_small_join():
    py.click('smallJoin.png')
    py.sleep(3)
    join()

def locateClass(cur):
    day=cur[2]
    t=cur[0]
    m=cur[1]
    while t!=15 and m!=50:
        if day == "Wednesday":
            if t == 15 and m == 59:
                aptitude()
        elif day == "Monday":
            if t == 8 and m == 49:
                math()
            elif t == 9 and m == 49:
                env()
            elif t == 11 and m==59:
                universal_small_join()


def main():
    #os.startfile("C:\\Users\jcmug\AppData\Local\Microsoft\Teams\\Update.exe --processStart \"Teams.exe\"")
    startfile("C:\\Users\jcmug\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams.lnk")
    time.sleep(10)
    try:
        py.click('calendar.png')
    except:
        py.click(34,297)
        print("Already on calendar page !!")
    cur=getTime()
    py.scroll(-2)
    #locateClass(cur)

if __name__ == "__main__":
    main()

