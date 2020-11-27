#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:41:58 2020

@author: nick
"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from Login import MyLogin

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MyLogin()
        self.ui.setupUi(self)
        self.show()  

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())