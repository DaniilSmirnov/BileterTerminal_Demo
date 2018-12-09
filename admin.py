from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

cnx = mysql.connector.connect(user='root', password='i130813',
                              host='127.0.0.1',
                              database='mydb')
cursor = cnx.cursor()

'''
select * from trip;
'''

items = []

class Ui_MainWindow(object):

    def setupUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 391, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.loginedit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.loginedit.setObjectName("loginedit")
        self.verticalLayout.addWidget(self.loginedit)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.passedit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passedit.setObjectName("passedit")
        self.verticalLayout.addWidget(self.passedit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.verticalLayoutWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupMainUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 555, 291))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.savebutton = QtWidgets.QPushButton(self.centralwidget)
        self.savebutton.setObjectName("savebutton")
        self.verticalLayout.addWidget(self.savebutton)
        self.cancelbutton = QtWidgets.QPushButton(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.cancelbutton.setObjectName("cancelbutton")
        self.verticalLayout.addWidget(self.cancelbutton)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateMainUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateMainUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.savebutton.setText(_translate("MainWindow", "Save"))
        self.cancelbutton.setText(_translate("MainWindow", "Cancel"))

        line_item = QtWidgets.QLabel("Рейсы")
        items.append(line_item)
        self.gridLayout.addWidget(line_item, 0, 0, 1, 1)
        query = ("select * from trip;")
        cursor.execute(query)
        i = 1
        j = 3
        k = 0
        exec = True
        for item in cursor:
            for value in item:
                if exec:
                    exec = False
                    continue
                line_item = QtWidgets.QLineEdit(str(value))
                self.gridLayout.addWidget(line_item, j, k, 1, 1)
                line_item.textChanged.connect(lambda state, line=line_item: modify(line, j, k))
                items.append(line_item)
                if i == 7:
                    i = 1
                else:
                    i += 1

                k += 1

            j += 1

        line_item = QtWidgets.QLabel("Пассажиры")
        items.append(line_item)
        query = ("select * from passenger;")
        cursor.execute(query)
        i = 1
        k = 0
        exec = True
        for item in cursor:
            for value in item:
                if exec:
                    exec = False
                    continue
                line_item = QtWidgets.QLineEdit(str(value))
                self.gridLayout.addWidget(line_item, j, k, 1, 1)
                line_item.textChanged.connect(lambda state, line=line_item: modify(line))
                items.append(line_item)
                if i == 7:
                    i = 1
                else:
                    i += 1

                k += 1

            j += 1

        def modify(item, j ,k):
            print(1)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Password"))
        self.loginedit.setText("1")
        self.passedit.setText("1")
        self.pushButton.setText(_translate("MainWindow", "Войти"))

        self.pushButton.clicked.connect(self.login)

    def login(self):
        username_entered = self.loginedit.text()
        password_entered = self.passedit.text()

        query = ("SELECT login from worker;")
        cursor.execute(query)

        for (login) in cursor:
            if login[0] == username_entered:
                query = ("SELECT pass from worker;")
                cursor.execute(query)
                for (password) in cursor:
                    if password[0] == password_entered:
                        self.setupMainUi()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    MainWindow.show()
    sys.exit(app.exec_())