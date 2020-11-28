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
        
        self.cur = connect()
            
        self.ui = customer_interface()
        self.ui.setupUi(self)
        
        self.cur.execute("SELECT * FROM menu")
        self.menu = self.cur.fetchall()
        
        for row in self.menu:
            row_count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(row_count+1)
            for i in range(2):
                cell = QtWidgets.QTableWidgetItem(str(row[i]))
                self.ui.tableWidget.setItem(row_count, i, cell)
        
        self.cur.execute("SELECT * FROM customer_info WHERE customerID=%s;", (str(customerID)))
        self.customer = Customer(self.cur.fetchone())
        self.ui.customerName.setText(str(self.customer.name))
        self.ui.points.setText(str(self.customer.points))
    
        self.ui.add.clicked = self.ui.add.clicked.connect(self.addItem)
        self.ui.submit.clicked = self.ui.submit.clicked.connect(self.submitOrder) 
        
    def addItem(self):
        items = self.ui.tableWidget.selectedItems()
        if items:
            self.customer.orders.append(items[0].text())
        
        row_count = self.ui.tableWidget1.rowCount()
        self.ui.tableWidget1.setRowCount(row_count+1)
        
        for item in self.menu:
            if item[0] == items[0].text():
                for i in range(3):
                    cell = QtWidgets.QTableWidgetItem(str(item[i]))
                    self.ui.tableWidget1.setItem(row_count, i, cell)
                
                cell = QtWidgets.QTableWidgetItem("Added")
                self.ui.tableWidget1.setItem(row_count, 3, cell)
                
    def submitOrder(self):
        index = 0
        for order in self.customer.orders:
            for item in self.menu:
                if order == item[0]:

                    self.cur.execute("""INSERT INTO orders (customerid, item, price, points, ready)
                    VALUES (%s, %s, %s, %s, FALSE);
                    """,
                    (str(self.customer.id), str(item[0]), str(item[1]), str(item[2])))
                    
                    cell = QtWidgets.QTableWidgetItem("Submitted")
                    self.ui.tableWidget1.setItem(index, 3, cell)
                    
                    self.customer.points += item[2]
                    index = index + 1
        
        self.customer.orders = []
                    
        
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
            self.orders = []
        else:
            self.id = 0
            self.name = "Anonymous"
            self.address = None
            self.cardnumber = None
            self.points = 0
            self.orders = []
    
        
def connect():
    conn = None;
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="cs487_app",
            user="developer",
            password="1")
        
        conn.autocommit = True
        
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