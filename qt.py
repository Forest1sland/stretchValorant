from PyQt6 import QtWidgets
import sys

from mainWindow import Ui_MainWindow
import main

data = {'github': 'https://github.com/Forest1sland',
        'help': '首先将游戏设置成窗口化拉伸模式，然后在该程序中设置好分辨率,必须为电脑支持的分辨率，点击启动。',
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
        main.backDefault()

    def clickStart(self):
        main.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainW = MyWindow()

    mainW.show()
    sys.exit(app.exec())
