# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer_interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class customer_interface(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 733)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(290, 20, 91, 37))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(420, 20, 101, 37))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(560, 20, 91, 37))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 291, 33))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1250, 1100, 471, 81))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 130, 114, 33))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 170, 371, 501))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget1 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget1.setGeometry(QtCore.QRect(570, 170, 401, 501))
        self.tableWidget1.setMaximumSize(QtCore.QSize(851, 16777215))
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(4)
        self.tableWidget1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(3, item)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 1230, 931, 35))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 1140, 181, 33))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1250, 1280, 481, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1390, 1230, 231, 33))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1700, 990, 181, 33))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1650, 1040, 231, 33))
        self.label_10.setObjectName("label_10")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(750, 140, 101, 16))
        self.label_2.setObjectName("label_2")
        
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(430, 270, 113, 51))
        self.add.setObjectName("add")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 410, 113, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(770, 0, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(770, 50, 59, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 480, 113, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.customerName = QtWidgets.QLabel(self.centralwidget)
        
        self.customerName.setGeometry(QtCore.QRect(770, 20, 59, 16))
        self.customerName.setObjectName("customerName")
        self.points = QtWidgets.QLabel(self.centralwidget)
        self.points.setGeometry(QtCore.QRect(770, 70, 59, 16))
        self.points.setObjectName("points")
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 340, 113, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 22))
        self.menubar.setObjectName("menubar")
        self.menuPlace_an_Order = QtWidgets.QMenu(self.menubar)
        self.menuPlace_an_Order.setObjectName("menuPlace_an_Order")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPlace_an_Order.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Dine-In"))
        self.radioButton_2.setText(_translate("MainWindow", "Pickup"))
        self.radioButton_3.setText(_translate("MainWindow", "Delivery"))
        self.label.setText(_translate("MainWindow", "Choose your order type:"))
        self.pushButton.setText(_translate("MainWindow", "Start Preparing Order"))
        self.label_6.setText(_translate("MainWindow", "Menu"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Menu Item"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Menu Item"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Points"))
        item = self.tableWidget1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.label_4.setText(_translate("MainWindow", "Order Progress"))
        self.pushButton_3.setText(_translate("MainWindow", "Pay for Your Order"))
        self.label_7.setText(_translate("MainWindow", "Order Complete!"))
        self.label_9.setText(_translate("MainWindow", "Total Items: 5"))
        self.label_10.setText(_translate("MainWindow", "Total Cost: $10.97"))
        self.label_2.setText(_translate("MainWindow", "Your Order"))
        self.add.setText(_translate("MainWindow", "Add ->"))
        self.pushButton_4.setText(_translate("MainWindow", "Submit"))
        self.label_3.setText(_translate("MainWindow", "Customer Name"))
        self.label_5.setText(_translate("MainWindow", "Points"))
        self.pushButton_6.setText(_translate("MainWindow", "Pay"))
        self.customerName.setText(_translate("MainWindow", "TextLabel"))
        self.points.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_5.setText(_translate("MainWindow", "Remove"))
        self.menuPlace_an_Order.setTitle(_translate("MainWindow", "Place an Order"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

