# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_up_interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sign_up_interface(object):
    def setupUi(self, sign_up_interface):
        sign_up_interface.setObjectName("sign_up_interface")
        sign_up_interface.resize(682, 500)
        sign_up_interface.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(sign_up_interface)
        self.centralwidget.setObjectName("centralwidget")
        self.fn_label = QtWidgets.QLabel(self.centralwidget)
        self.fn_label.setGeometry(QtCore.QRect(10, 200, 111, 33))
        self.fn_label.setObjectName("fn_label")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(110, 10, 511, 41))
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.ln_label = QtWidgets.QLabel(self.centralwidget)
        self.ln_label.setGeometry(QtCore.QRect(340, 200, 101, 33))
        self.ln_label.setObjectName("ln_label")
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setGeometry(QtCore.QRect(10, 250, 81, 33))
        self.address_label.setObjectName("address_label")
        self.city_label = QtWidgets.QLabel(self.centralwidget)
        self.city_label.setGeometry(QtCore.QRect(10, 300, 61, 33))
        self.city_label.setObjectName("city_label")
        self.cc_label = QtWidgets.QLabel(self.centralwidget)
        self.cc_label.setGeometry(QtCore.QRect(10, 350, 141, 33))
        self.cc_label.setObjectName("cc_label")
        self.signup_btn = QtWidgets.QPushButton(self.centralwidget)
        self.signup_btn.setGeometry(QtCore.QRect(250, 390, 187, 57))
        self.signup_btn.setObjectName("signup_btn")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(200, 70, 111, 33))
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(200, 120, 111, 33))
        self.password_label.setObjectName("password_label")
        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(340, 70, 161, 31))
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(340, 120, 161, 31))
        self.password_input.setObjectName("password_input")
        self.fn_input = QtWidgets.QLineEdit(self.centralwidget)
        self.fn_input.setGeometry(QtCore.QRect(150, 200, 161, 31))
        self.fn_input.setObjectName("fn_input")
        self.ln_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_input.setGeometry(QtCore.QRect(470, 200, 161, 31))
        self.ln_input.setObjectName("ln_input")
        self.address_input = QtWidgets.QLineEdit(self.centralwidget)
        self.address_input.setGeometry(QtCore.QRect(150, 250, 481, 31))
        self.address_input.setObjectName("address_input")
        self.city_input = QtWidgets.QLineEdit(self.centralwidget)
        self.city_input.setGeometry(QtCore.QRect(150, 300, 181, 31))
        self.city_input.setObjectName("city_input")
        self.cc_input = QtWidgets.QLineEdit(self.centralwidget)
        self.cc_input.setGeometry(QtCore.QRect(160, 350, 471, 31))
        self.cc_input.setObjectName("cc_input")
        sign_up_interface.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(sign_up_interface)
        self.statusbar.setObjectName("statusbar")
        sign_up_interface.setStatusBar(self.statusbar)

        self.retranslateUi(sign_up_interface)
        QtCore.QMetaObject.connectSlotsByName(sign_up_interface)

    def retranslateUi(self, sign_up_interface):
        _translate = QtCore.QCoreApplication.translate
        sign_up_interface.setWindowTitle(_translate("sign_up_interface", "MainWindow"))
        self.fn_label.setText(_translate("sign_up_interface", "First Name:"))
        self.header.setText(_translate("sign_up_interface", "Welcome! Please enter your information."))
        self.ln_label.setText(_translate("sign_up_interface", "Last Name:"))
        self.address_label.setText(_translate("sign_up_interface", "Address:"))
        self.city_label.setText(_translate("sign_up_interface", "City:"))
        self.cc_label.setText(_translate("sign_up_interface", "Credit Card #:"))
        self.signup_btn.setText(_translate("sign_up_interface", "Sign Up"))
        self.username_label.setText(_translate("sign_up_interface", "Username:"))
        self.password_label.setText(_translate("sign_up_interface", "Password:"))

