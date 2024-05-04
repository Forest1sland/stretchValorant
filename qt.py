import sys

from PyQt6 import QtWidgets

import main
from mainWindow import Ui_MainWindow

data = {'github': 'https://github.com/Forest1sland',
        'help': '首先将游戏设置成窗口化拉伸模式，然后在该程序中设置好分辨率,必须为电脑支持的分辨率，点击启动。不要关闭程序，结束游戏后还原初始分辨率。',
        'version': 'v1.0'}


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.about.clicked.connect(self.clickAbout)
        self.help.clicked.connect(self.clickHelp)
        self.restore.clicked.connect(self.backDefault)
        self.start.clicked.connect(self.clickStart)

    def clickAbout(self):
        QtWidgets.QMessageBox.information(self, 'About', data['github'] + '\n\n' + data['version'])

    def clickHelp(self):
        QtWidgets.QMessageBox.information(self, 'Help', data['help'])

    def backDefault(self):
        print(main.oh, main.ow, main.of)
        main.backDefault(main.oh, main.ow, main.of)

    def clickStart(self):
        print(self.width.toPlainText(), self.length.toPlainText(), self.frequency.toPlainText())
        if main.start(self.width.toPlainText(), self.length.toPlainText(), self.frequency.toPlainText()):
            QtWidgets.QMessageBox.information(self, 'Tip', "拉伸成功！")
        else:
            QtWidgets.QMessageBox.information(self, 'Tip', "拉伸失败！")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainW = MyWindow()

    mainW.show()
    sys.exit(app.exec())
