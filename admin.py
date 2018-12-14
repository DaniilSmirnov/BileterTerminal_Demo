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

trip = []
trip_data = {}
trip_k = {}

passenger = []
passenger_data = {}
passenger_k = {}


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
        self.closebutton = QtWidgets.QPushButton(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.closebutton.setObjectName("cancelbutton")
        self.verticalLayout.addWidget(self.closebutton)
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
        self.savebutton.setText(_translate("MainWindow", "Сохранить"))
        self.closebutton.setText(_translate("MainWindow", "Выйти"))
        self.closebutton.clicked.connect(self.setupUi)

        line_item = QtWidgets.QLabel("Рейсы")
        items.append(line_item)
        self.gridLayout.addWidget(line_item, 0, 0, 1, 1)
        query = ("select * from trip;")
        cursor.execute(query)
        i = 1
        j = 3
        k = 0
        for item in cursor:
            trip.append(item[0])
            for value in item:
                line_item = QtWidgets.QLineEdit(str(value))
                self.gridLayout.addWidget(line_item, j, k, 1, 1)
                line_item.textChanged.connect(lambda state, line=line_item: modify_trip(line))
                items.append(line_item)
                trip_data.update({line_item: line_item.text()})
                if i == 7:
                    i = 1
                else:
                    i += 1
                trip_k.update({line_item: k})
                k += 1

            j += 1

        line_item = QtWidgets.QLabel("Пассажиры")
        items.append(line_item)
        query = ("select * from passenger;")
        cursor.execute(query)
        i = 1
        k = 0
        for item in cursor:
            passenger.append(item[0])
            for value in item:
                line_item = QtWidgets.QLineEdit(str(value))
                self.gridLayout.addWidget(line_item, j, k, 1, 1)
                line_item.textChanged.connect(lambda state, line=line_item: modify_pass(line))
                items.append(line_item)
                passenger_data.update({line_item: line_item.text()})
                if i == 7:
                    i = 1
                else:
                    i += 1
                passenger_k.update({line_item: k})
                k += 1

            j += 1

        def save_pass(item):
            k = passenger_k.get(item)
            position = passenger_data.get(item)
            text = item.text()
            data = (text, position)
            if k == 1:
                query = ("update passenger set NameP = %s where NameP = %s;")
            if k == 2:
                query = ("update passenger set SurnameP = %s where SurnameP = %s;")
            if k == 3:
                query = ("update passenger set Patronymic = %s where Patronymic = %s;")
            if k == 4:
                query = ("update passenger set Passport = %s where Passport = %s;")
            cursor.execute(query, data)
            cnx.commit()

        def modify_pass(item):
            self.savebutton.clicked.connect(lambda: save_pass(item))

        def save_trip(item):
            k = trip_k.get(item)
            position = trip_data.get(item)
            text = item.text()
            data = (text, position)
            if k == 1:
                query = ("update trip set TripNumber = %s where TripNumber = %s;")
            if k == 2:
                query = ("update trip set FromCity = %s where FromCity = %s;")
            if k == 3:
                query = ("update trip set ToCity = %s where ToCity = %s;")
            if k == 4:
                query = ("update trip set DateDeparture = %s where DateDeparture = %s;")
            if k == 5:
                query = ("update trip set DateArrival = %s where DateArrival = %s;")
            if k == 6:
                query = ("update trip set Company = %s where Company = %s;")
            if k == 7:
                query = ("update trip set Cost = %s where Cost = %s;")
            cursor.execute(query, data)
            cnx.commit()

        def modify_trip(item):
            self.savebutton.clicked.connect(lambda: save_trip(item))



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