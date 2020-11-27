#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:41:58 2020

@author: nick
"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from login import login_interface
from stuff_interface import stuff_interface
from customer_interface import customer_interface

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = login_interface()
        self.ui.setupUi(self)
        self.show()  

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())