#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:41:58 2020

@author: nick
"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from login import login_interface
from staff_interface import staff_interface
from customer_interface import customer_interface

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = login_interface()
        self.ui.setupUi(self)
        
        self.app2 = CustomerInterface()
        self.ui.pushButton.clicked = self.ui.pushButton.clicked.connect(self.enterLogin)
        self.show()
        
    def enterLogin(self):
        self.hide()
        self.app2 = CustomerInterface()
        self.app2.show()
        
class CustomerInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = customer_interface()
        self.ui.setupUi(self)
        
class StaffInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = staff_interface()
        self.ui.setupUi(self)
        
        

app = QApplication(sys.argv)
gui = Login()
gui.show()
sys.exit(app.exec_())