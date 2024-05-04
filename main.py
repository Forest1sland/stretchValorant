from win32gui import FindWindow, GetWindowLong, ShowWindow, SetWindowLong, GetDC
from win32con import GWL_STYLE, WS_BORDER, WS_DLGFRAME, SW_SHOWMAXIMIZED, DESKTOPHORZRES, DESKTOPVERTRES
from win32api import EnumDisplaySettings, ChangeDisplaySettings
import win32print

handle = FindWindow("UnrealWindow", "VALORANT  ")
hDC = GetDC(0)
# 横向分辨率
w = win32print.GetDeviceCaps(hDC, DESKTOPHORZRES)
# 纵向分辨率
h = win32print.GetDeviceCaps(hDC, DESKTOPVERTRES)


def changeDisplay(h=1280, w=1024, f=144):
    dm = EnumDisplaySettings(None, 0)
    dm.PelsHeight = h
    dm.PelsWidth = w
    dm.BitsPerPel = 32
    dm.DisplayFixedOutput = 2
    dm.DisplayFrequency = f
    if ChangeDisplaySettings(dm, 0) == 0:
        print("分辨率修改成功！")
        return 1
    else:
        print("分辨率修改失败！")
        return 0


def stretchWindow():
    if (SetWindowLong(handle, GWL_STYLE, GetWindowLong(handle, GWL_STYLE) & ~WS_BORDER, ) and
        SetWindowLong(handle, GWL_STYLE, GetWindowLong(handle, GWL_STYLE) & ~WS_DLGFRAME) and
        ShowWindow(handle, SW_SHOWMAXIMIZED)) != 0:
        print("拉伸成功！")
    else:
        print("拉伸失败！")


def backDefault():
    dm = EnumDisplaySettings(None, 0)
    dm.PelsHeight = 1080
    dm.PelsWidth = 1920
    dm.BitsPerPel = 32
    dm.DisplayFixedOutput = 2
    dm.DisplayFrequency = 144
    if ChangeDisplaySettings(dm, 0) == 0:
        print("分辨率修改成功！")
        return 1
    else:
        print("分辨率修改失败！")
        return 0


def start():
    if handle:
        if changeDisplay() == 1:
            stretchWindow()
    else:
        print("游戏未启动。")

