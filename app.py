#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:41:58 2020

@author: nick
"""
import sys
import psycopg2
from PyQt5 import QtWidgets
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
        
        cur = connect()
            
        self.ui = customer_interface()
        self.ui.setupUi(self)
        cur.execute("SELECT * FROM menu")
        menu = cur.fetchall()
        
        for row in menu:
            row_count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(row_count+1)
            for i in range(2):
                cell = QtWidgets.QTableWidgetItem(str(row[i]))
                self.ui.tableWidget.setItem(row_count, i, cell)
        
        if(customerID != 0):
            cur.execute("SELECT * FROM customer_info WHERE customerID=%s;", (str(customerID)))
            customer = Customer(cur.fetchone())
            self.ui.customerName.setText(str(customer.name))
            self.ui.points.setText(str(customer.points))
            
        
class StaffInterface(QMainWindow):
    def __init__(self, staffID):
        super().__init__()
        self.ui = staff_interface()
        self.ui.setupUi(self)
        
class Customer():
    def __init__(self, customer_data):
        if customer_data is not None:
            self.id = customer_data[0]
            self.name = customer_data[1] + " " + customer_data[2]
            self.address = customer_data[3] + " " + customer_data[4]
            self.cardnumber = customer_data[5]
            self.points = customer_data[6]
            self.order = []
        else:
            self.id = 0
            self.name = "Anonymous"
            self.address = None
            self.cardnumber = None
            self.points = None
            self.order = []
    
    def add_to_order(self, item, price, points):
        cur = connect()
        cur.execute("""INSERT INTO orders (customerid, item, points, price, ready)
                    VALUES (%s, %s, %s, %s, 1);
                    """,
                    (customerID, item, points, price))
        
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