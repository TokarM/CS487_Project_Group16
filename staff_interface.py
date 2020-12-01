# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staff_interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_staff_interface(object):
    def setupUi(self, staff_interface):
        staff_interface.setObjectName("staff_interface")
        staff_interface.resize(1434, 1200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(staff_interface.sizePolicy().hasHeightForWidth())
        staff_interface.setSizePolicy(sizePolicy)
        staff_interface.setMinimumSize(QtCore.QSize(1434, 812))
        staff_interface.setMaximumSize(QtCore.QSize(1480, 1200))
        self.centralwidget = QtWidgets.QWidget(staff_interface)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(30, 20, 321, 51))
        self.welcome_label.setObjectName("welcome_label")
        self.table_label = QtWidgets.QLabel(self.centralwidget)
        self.table_label.setGeometry(QtCore.QRect(30, 100, 201, 81))
        self.table_label.setObjectName("table_label")
        self.update_orders_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_orders_btn.setGeometry(QtCore.QRect(270, 1070, 231, 71))
        self.update_orders_btn.setObjectName("update_orders_btn")
        self.ordersTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.ordersTableWidget.setGeometry(QtCore.QRect(260, 110, 1151, 931))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ordersTableWidget.sizePolicy().hasHeightForWidth())
        self.ordersTableWidget.setSizePolicy(sizePolicy)
        self.ordersTableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ordersTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ordersTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ordersTableWidget.setShowGrid(True)
        self.ordersTableWidget.setCornerButtonEnabled(True)
        self.ordersTableWidget.setObjectName("ordersTableWidget")
        self.ordersTableWidget.setColumnCount(5)
        self.ordersTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.ordersTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(4, item)
        self.ordersTableWidget.horizontalHeader().setDefaultSectionSize(217)
        self.ordersTableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.ordersTableWidget.verticalHeader().setVisible(False)
        self.update_menu_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_menu_btn.setGeometry(QtCore.QRect(890, 30, 231, 57))
        self.update_menu_btn.setObjectName("update_menu_btn")
        self.logout_btn = QtWidgets.QPushButton(self.centralwidget)
        self.logout_btn.setGeometry(QtCore.QRect(1150, 30, 231, 57))
        self.logout_btn.setMinimumSize(QtCore.QSize(1, 0))
        self.logout_btn.setObjectName("logout_btn")
        staff_interface.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(staff_interface)
        self.statusbar.setObjectName("statusbar")
        staff_interface.setStatusBar(self.statusbar)

        self.retranslateUi(staff_interface)
        QtCore.QMetaObject.connectSlotsByName(staff_interface)

    def retranslateUi(self, staff_interface):
        _translate = QtCore.QCoreApplication.translate
        staff_interface.setWindowTitle(_translate("staff_interface", "MainWindow"))
        self.welcome_label.setText(_translate("staff_interface", "Welcome Staff Member"))
        self.table_label.setText(_translate("staff_interface", "Current Orders :"))
        self.update_orders_btn.setText(_translate("staff_interface", "Update Orders"))
        self.ordersTableWidget.setSortingEnabled(True)
        item = self.ordersTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("staff_interface", "ID"))
        item = self.ordersTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("staff_interface", "Order Number"))
        item = self.ordersTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("staff_interface", "Dish Name"))
        item = self.ordersTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("staff_interface", "Status"))
        item = self.ordersTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("staff_interface", "Change Status"))
        self.update_menu_btn.setText(_translate("staff_interface", "Update Menu"))
        self.logout_btn.setText(_translate("staff_interface", "Log Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    staff_interface = QtWidgets.QMainWindow()
    ui = Ui_staff_interface()
    ui.setupUi(staff_interface)
    staff_interface.show()
    sys.exit(app.exec_())

