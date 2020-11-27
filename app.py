#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:41:58 2020

@author: nick
"""
import sys
import psycopg2
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from login import login_interface
from staff_interface import staff_interface
from customer_interface import customer_interface

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = login_interface()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked = self.ui.loginButton.clicked.connect(self.enterLogin)
        self.ui.pushButton_2.clicked = self.ui.pushButton_2.clicked.connect(self.anonymousLogin)
        
        self.show()
        
    def anonymousLogin(self):
        self.hide()
        self.app2 = CustomerInterface(0)
        self.app2.show()
        
    def enterLogin(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        cur = connect()
        cur.execute("SELECT * FROM login_info WHERE username=%s AND password=%s", (username, password))
        response = cur.fetchone()
        if response is not None:
            ID = response[0]
            privilege = response[3]
            if privilege == 2:
                self.hide()
                self.app2 = CustomerInterface(ID)
                self.app2.show()
            elif privilege == 1:
                self.hide()
                self.app2 = StaffInterface(ID)
                self.app2.show()
        else:
            msg = QMessageBox()
            msg.setText("Invalid Login Information")
            msg.exec_()
        
        
class CustomerInterface(QMainWindow):
    def __init__(self, customerID):
        super().__init__()
        
        self.ui = customer_interface()
        self.ui.setupUi(self)
        
        if(customerID != 0):
            self.ui.customerName.setText(str(customerID))
            self.ui.points.setText('5')
        
        
class StaffInterface(QMainWindow):
    def __init__(self, staffID):
        super().__init__()
        self.ui = staff_interface()
        self.ui.setupUi(self)
        
def connect():
    conn = None;
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="cs487_app",
            user="developer",
            password="1")
        
        cur = conn.cursor()
        
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
    
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        #cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    return cur
    
                

app = QApplication(sys.argv)
gui = Login()
gui.show()
sys.exit(app.exec_())