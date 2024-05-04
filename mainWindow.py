from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 178)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 分辨率设置
        self.widthText = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.widthText.setGeometry(QtCore.QRect(150, 30, 41, 31))
        self.widthText.setObjectName("length")
        self.widthText.setText("1280")

        self.frequency = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.frequency.setGeometry(QtCore.QRect(340, 30, 51, 31))
        self.frequency.setObjectName("frequency")
        self.frequency.setText("144")

        self.heightText = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.heightText.setGeometry(QtCore.QRect(230, 30, 41, 31))
        self.heightText.setObjectName("width")
        self.heightText.setText("1024")

        # 按钮
        self.start = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start.setGeometry(QtCore.QRect(140, 100, 75, 23))
        self.start.setObjectName("start")

        self.about = QtWidgets.QPushButton(parent=self.centralwidget)
        self.about.setGeometry(QtCore.QRect(320, 100, 75, 23))
        self.about.setObjectName("about")

        self.restore = QtWidgets.QPushButton(parent=self.centralwidget)
        self.restore.setGeometry(QtCore.QRect(230, 100, 75, 23))
        self.restore.setObjectName("restore")

        self.help = QtWidgets.QPushButton(parent=self.centralwidget)
        self.help.setGeometry(QtCore.QRect(50, 100, 75, 23))
        self.help.setObjectName("help")

        # 文本
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 40, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 40, 53, 15))
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "无畏契约拉伸"))
        self.label_3.setText(_translate("MainWindow", "宽"))
        self.start.setText(_translate("MainWindow", "启动"))
        self.about.setText(_translate("MainWindow", "关于"))
        self.restore.setText(_translate("MainWindow", "还原默认值"))
        self.help.setText(_translate("MainWindow", "帮助"))
        self.label_2.setText(_translate("MainWindow", "长"))
        self.label.setText(_translate("MainWindow", "分辨率设置"))
        self.label_4.setText(_translate("MainWindow", "刷新率"))
