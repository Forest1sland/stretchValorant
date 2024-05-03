from win32gui import FindWindow, GetWindowLong, ShowWindow, SetWindowLong
from win32con import GWL_STYLE, WS_BORDER, WS_DLGFRAME, SW_SHOWMAXIMIZED
from win32api import EnumDisplaySettings, ChangeDisplaySettings

handle = FindWindow("UnrealWindow", "VALORANT  ")


def changeDisplay():
    dm = EnumDisplaySettings(None, 0)
    dm.PelsHeight = 1024
    dm.PelsWidth = 1280
    dm.BitsPerPel = 32
    dm.DisplayFixedOutput = 2
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


if __name__ == "__main__":
    if handle:
        if changeDisplay() == 1:
            stretchWindow()
    else:
        print("游戏未启动。")
