# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_user_info.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class update_user_info(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 339)
        self.userNameLine = QtWidgets.QLineEdit(Dialog)
        self.userNameLine.setGeometry(QtCore.QRect(20, 40, 181, 21))
        self.userNameLine.setObjectName("userNameLine")
        self.creditCardLine = QtWidgets.QLineEdit(Dialog)
        self.creditCardLine.setGeometry(QtCore.QRect(20, 200, 181, 21))
        self.creditCardLine.setObjectName("creditCardLine")
        self.oldPasswordLine = QtWidgets.QLineEdit(Dialog)
        self.oldPasswordLine.setGeometry(QtCore.QRect(20, 240, 181, 21))
        self.oldPasswordLine.setObjectName("oldPasswordLine")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 101, 16))
        self.label_4.setObjectName("label_4")
        self.newPasswordLine = QtWidgets.QLineEdit(Dialog)
        self.newPasswordLine.setGeometry(QtCore.QRect(20, 280, 181, 21))
        self.newPasswordLine.setObjectName("newPasswordLine")
        self.updateInfoButton = QtWidgets.QPushButton(Dialog)
        self.updateInfoButton.setGeometry(QtCore.QRect(250, 200, 141, 31))
        self.updateInfoButton.setObjectName("updateInfoButton")
        self.updatePasswordButton = QtWidgets.QPushButton(Dialog)
        self.updatePasswordButton.setGeometry(QtCore.QRect(250, 280, 141, 31))
        self.updatePasswordButton.setObjectName("updatePasswordButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.label_5.setObjectName("label_5")
        self.firstNameLine = QtWidgets.QLineEdit(Dialog)
        self.firstNameLine.setGeometry(QtCore.QRect(20, 80, 181, 21))
        self.firstNameLine.setObjectName("firstNameLine")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 71, 16))
        self.label_6.setObjectName("label_6")
        self.lastNameLine = QtWidgets.QLineEdit(Dialog)
        self.lastNameLine.setGeometry(QtCore.QRect(20, 120, 181, 21))
        self.lastNameLine.setObjectName("lastNameLine")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 71, 16))
        self.label_7.setObjectName("label_7")
        self.addressLine = QtWidgets.QLineEdit(Dialog)
        self.addressLine.setGeometry(QtCore.QRect(20, 160, 181, 21))
        self.addressLine.setObjectName("addressLine")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Old Password"))
        self.label_3.setText(_translate("Dialog", "New Password"))
        self.label_4.setText(_translate("Dialog", "Credit card"))
        self.updateInfoButton.setText(_translate("Dialog", "Update User Info"))
        self.updatePasswordButton.setText(_translate("Dialog", "Update Password"))
        self.label_5.setText(_translate("Dialog", "First Name"))
        self.label_6.setText(_translate("Dialog", "Last Name"))
        self.label_7.setText(_translate("Dialog", "Address"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

