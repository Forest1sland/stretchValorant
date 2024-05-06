from win32gui import FindWindow, GetWindowLong, ShowWindow, SetWindowLong, GetDC
from win32con import GWL_STYLE, WS_BORDER, WS_DLGFRAME, SW_SHOWMAXIMIZED, DESKTOPHORZRES, DESKTOPVERTRES, \
    VREFRESH
from win32api import EnumDisplaySettings, ChangeDisplaySettings
import win32print

handle = FindWindow("UnrealWindow", "VALORANT  ")
hDC = GetDC(0)
# 初始横向分辨率
ow = win32print.GetDeviceCaps(hDC, DESKTOPHORZRES)
# 初始纵向分辨率
oh = win32print.GetDeviceCaps(hDC, DESKTOPVERTRES)
# 初始刷新率
of = win32print.GetDeviceCaps(hDC, VREFRESH)


# 可选添加一个通用返回类

# 更改电脑分辨率
def changeDisplay(h, w, f):
    dm = EnumDisplaySettings(None, 0)
    dm.PelsHeight = h
    dm.PelsWidth = w
    dm.BitsPerPel = 32
    dm.DisplayFixedOutput = 0
    dm.DisplayFrequency = f
    if ChangeDisplaySettings(dm, 0) == 0:
        print("分辨率修改成功！")
        return True
    else:
        print("分辨率修改失败！")
        return False


# 拉伸游戏
def stretchWindow():
    if (SetWindowLong(handle, GWL_STYLE, GetWindowLong(handle, GWL_STYLE) & ~WS_BORDER, ) and
        SetWindowLong(handle, GWL_STYLE, GetWindowLong(handle, GWL_STYLE) & ~WS_DLGFRAME) and
        ShowWindow(handle, SW_SHOWMAXIMIZED)) != 0:
        print("拉伸成功！")
        return True
    else:
        print("拉伸失败！")
        return False


# 还原初始分辨率
def backDefault():
    dm = EnumDisplaySettings(None, 0)
    dm.PelsHeight = oh
    dm.PelsWidth = ow
    dm.BitsPerPel = 32
    dm.DisplayFixedOutput = 2
    dm.DisplayFrequency = of
    if ChangeDisplaySettings(dm, 0) == 0:
        print("分辨率修改成功！")
        return True
    else:
        print("分辨率修改失败！")
        return False


# 启动
def start(h, w, f):
    if handle:
        if changeDisplay(h, w, f):
            return stretchWindow()
    else:
        print("请启动无畏契约。")
        return False
