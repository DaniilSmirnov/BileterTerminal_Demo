# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb #pip install --only-binary :all: mysqlclient
from docx import Document #pip install python-docx
from docx.shared import Inches


class Ui_MainWindow(object):
    def setupUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.whenedit = QtWidgets.QDateEdit(self.gridWidget)
        self.whenedit.setObjectName("whenedit")
        self.gridLayout.addWidget(self.whenedit, 6, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 8, 0, 2, 3)
        self.infobutton = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infobutton.sizePolicy().hasHeightForWidth())
        self.infobutton.setSizePolicy(sizePolicy)
        self.infobutton.setObjectName("infobutton")
        self.gridLayout.addWidget(self.infobutton, 0, 2, 1, 1)
        self.searchbutton = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchbutton.sizePolicy().hasHeightForWidth())
        self.searchbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        self.searchbutton.setFont(font)
        self.searchbutton.setObjectName("searchbutton")
        self.gridLayout.addWidget(self.searchbutton, 10, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.gridWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.numberedit = QtWidgets.QLineEdit(self.gridWidget)
        self.numberedit.setObjectName("numberedit")
        self.gridLayout.addWidget(self.numberedit, 8, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 3)
        self.fromedit = QtWidgets.QLineEdit(self.gridWidget)
        self.fromedit.setObjectName("fromedit")
        self.gridLayout.addWidget(self.fromedit, 6, 0, 1, 1)
        self.whereedit = QtWidgets.QLineEdit(self.gridWidget)
        self.whereedit.setObjectName("whereedit")
        self.gridLayout.addWidget(self.whereedit, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.gridWidget) #весь секрет здеся!
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Куда"))
        self.label_3.setText(_translate("MainWindow", "Откуда"))
        self.label_2.setText(_translate("MainWindow", "Поиск рейсов"))
        self.label.setText(_translate("MainWindow", "Билеты на автобус"))
        self.label_6.setText(_translate("MainWindow", "Поиск по номеру рейса"))
        self.infobutton.setText(_translate("MainWindow", "Инфо"))
        self.searchbutton.setText(_translate("MainWindow", "Поиск"))

        self.searchbutton.clicked.connect(self.setupGlobalViewUi)

    def setupGlobalViewUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.routenumberlabel = QtWidgets.QLabel(self.centralwidget)
        self.routenumberlabel.setObjectName("routenumberlabel")
        self.horizontalLayout.addWidget(self.routenumberlabel)
        self.fromlabel = QtWidgets.QLabel(self.centralwidget)
        self.fromlabel.setObjectName("fromlabel")
        self.horizontalLayout.addWidget(self.fromlabel)
        self.departtimelabel = QtWidgets.QLabel(self.centralwidget)
        self.departtimelabel.setObjectName("departtimelabel")
        self.horizontalLayout.addWidget(self.departtimelabel)
        self.timeinttravellabel = QtWidgets.QLabel(self.centralwidget)
        self.timeinttravellabel.setObjectName("timeinttravellabel")
        self.horizontalLayout.addWidget(self.timeinttravellabel)
        self.wherelabel = QtWidgets.QLabel(self.centralwidget)
        self.wherelabel.setObjectName("wherelabel")
        self.horizontalLayout.addWidget(self.wherelabel)
        self.arrivetimelabel = QtWidgets.QLabel(self.centralwidget)
        self.arrivetimelabel.setObjectName("arrivetimelabel")
        self.horizontalLayout.addWidget(self.arrivetimelabel)
        self.costlabel = QtWidgets.QLabel(self.centralwidget)
        self.costlabel.setObjectName("costlabel")
        self.horizontalLayout.addWidget(self.costlabel)
        self.filler = QtWidgets.QLabel(self.centralwidget)
        self.filler.setObjectName("filler")
        self.horizontalLayout.addWidget(self.filler)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 836, 541))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 841, 571))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.backtomainbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backtomainbutton.sizePolicy().hasHeightForWidth())
        self.backtomainbutton.setSizePolicy(sizePolicy)
        self.backtomainbutton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.backtomainbutton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateGlobalViewUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateGlobalViewUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.routenumberlabel.setText(_translate("MainWindow", "Рейс"))
        self.fromlabel.setText(_translate("MainWindow", "Откуда"))
        self.departtimelabel.setText(_translate("MainWindow", "Время отправления"))
        self.timeinttravellabel.setText(_translate("MainWindow", "Время в пути"))
        self.wherelabel.setText(_translate("MainWindow", "Куда"))
        self.arrivetimelabel.setText(_translate("MainWindow", "Время прибытия"))
        self.costlabel.setText(_translate("MainWindow", "Цена"))
        self.filler.setText(_translate("MainWindow", " "))
        self.backtomainbutton.setText(_translate("MainWindow", "Назад"))
        self.backtomainbutton.clicked.connect(self.setupUi)

    def setupRouteInfoUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 741, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.routelabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.routelabel.setObjectName("routelabel")
        self.verticalLayout.addWidget(self.routelabel)
        self.fromlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.fromlabel.setObjectName("fromlabel")
        self.verticalLayout.addWidget(self.fromlabel)
        self.wherelabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.wherelabel.setObjectName("wherelabel")
        self.verticalLayout.addWidget(self.wherelabel)
        self.whenlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.whenlabel.setObjectName("whenlabel")
        self.verticalLayout.addWidget(self.whenlabel)
        self.arrivelabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.arrivelabel.setObjectName("arrivelabel")
        self.verticalLayout.addWidget(self.arrivelabel)
        self.traveltimelabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.traveltimelabel.setObjectName("traveltimelabel")
        self.verticalLayout.addWidget(self.traveltimelabel)
        self.seatslabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.seatslabel.setObjectName("seatslabel")
        self.verticalLayout.addWidget(self.seatslabel)
        self.buybutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buybutton.setObjectName("buybutton")
        self.verticalLayout.addWidget(self.buybutton)
        self.backbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.backbutton.setObjectName("backbutton")
        self.verticalLayout.addWidget(self.backbutton)
        MainWindow.setCentralWidget(self.verticalLayoutWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateRouteInfoUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateRouteInfoUi(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.routelabel.setText(_translate("MainWindow", "Рейс"))
        self.fromlabel.setText(_translate("MainWindow", "Из"))
        self.wherelabel.setText(_translate("MainWindow", "В"))
        self.whenlabel.setText(_translate("MainWindow", "Время отправления:"))
        self.arrivelabel.setText(_translate("MainWindow", "Время прибытия:"))
        self.traveltimelabel.setText(_translate("MainWindow", "Время в пути:"))
        self.seatslabel.setText(_translate("MainWindow", "Количество мест:"))
        self.buybutton.setText(_translate("MainWindow", "Купить"))
        self.backbutton.setText(_translate("MainWindow", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    app.setStyle("Fusion")
    MainWindow.show()
    sys.exit(app.exec_())