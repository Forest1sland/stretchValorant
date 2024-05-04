import sys

from PyQt6 import QtWidgets

import main
from mainWindow import Ui_MainWindow

# 文本信息
data = {'github': 'https://github.com/Forest1sland/stretchValorant',
        'help': '首先将游戏设置成窗口化拉伸模式，然后在该程序中设置好分辨率,必须为电脑支持的分辨率，点击启动。不要关闭程序，结束游戏后还原初始分辨率。',
        'version': 'v1.0'}


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # 绑定点击事件
        self.about.clicked.connect(self.clickAbout)
        self.help.clicked.connect(self.clickHelp)
        self.restore.clicked.connect(self.backDefault)
        self.start.clicked.connect(self.clickStart)

    # 点击关于
    def clickAbout(self):
        QtWidgets.QMessageBox.information(self, 'About', data['github'] + '\n\n' + data['version'])

    # 点击帮助
    def clickHelp(self):
        QtWidgets.QMessageBox.information(self, 'Help', data['help'])

    # 点击还原
    def backDefault(self):
        print(main.oh, main.ow, main.of)
        if main.backDefault():
            QtWidgets.QMessageBox.information(self, 'Tip', "还原成功！")
        else:
            QtWidgets.QMessageBox.information(self, 'Tip', "还原失败！")

    # 点击开始
    def clickStart(self):
        print(self.heightText.toPlainText(), self.widthText.toPlainText(), self.frequency.toPlainText())
        if main.start(int(self.heightText.toPlainText()), int(self.widthText.toPlainText()),
                      int(self.frequency.toPlainText())):
            QtWidgets.QMessageBox.information(self, 'Tip', "拉伸成功！")
        else:
            QtWidgets.QMessageBox.information(self, 'Tip', "拉伸失败！")


# 启动
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainW = MyWindow()

    mainW.show()
    sys.exit(app.exec())
