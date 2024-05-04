
from PyQt6 import QtWidgets
import sys

from mainWindow import Ui_MainWindow
import main
import yaml

with open('text.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)


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
    main = MyWindow()

    main.show()
    sys.exit(app.exec())
