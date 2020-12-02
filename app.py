#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:41:58 2020

@author: nick
"""
import sys
import psycopg2
from datetime import datetime
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from Login import login_interface
from staff_interface import Ui_staff_interface as staff_interface
from customer_interface import customer_interface
from checkout import checkout_dialog
from update_user_info import update_user_info
from functools import partial
from sign_up_interface import Ui_sign_up_interface as sign_up_interface

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = login_interface()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked = self.ui.loginButton.clicked.connect(self.enterLogin)
        self.ui.pushButton_2.clicked = self.ui.pushButton_2.clicked.connect(self.anonymousLogin)
        self.ui.pushButton_4.clicked = self.ui.pushButton_4.clicked.connect(self.signUp)
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
    
    def signUp(self):
        self.hide()
        self.app2 = SignUp()
        self.app2.show()
            

class SignUp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = sign_up_interface()
        self.ui.setupUi(self)

        self.cur = connect()
        self.ui.signup_btn.clicked = self.ui.signup_btn.clicked.connect(self.trySignUp)

    def trySignUp(self):
        username = str(self.ui.username_input.text())
        password = str(self.ui.password_input.text())
        firstName = str(self.ui.fn_input.text())
        lastName = str(self.ui.ln_input.text())
        address = str(self.ui.address_input.text())
        city = str(self.ui.city_input.text())
        cc = int(self.ui.cc_input.text())

        # get last largest ID
        self.cur.execute("SELECT MAX(id) AS maxid FROM login_info")
        result = self.cur.fetchall()

        largestID = 1
        
        for i in result:
            if i[0] is not None:
                largestID = int(i[0])

        newID = largestID + 1

        # insert login info with customer privilege
        sql = """INSERT INTO login_info (id, username, password, privilege) VALUES (%s, %s, %s, %s)"""

        self.cur.execute(sql, (newID, username, password, 2))

        # insert customer info
        sql = """INSERT INTO customer_info (customerid, firstname, lastname, address, city, cardnumber)
                 VALUES (%s, %s, %s, %s, %s, %s)"""

        self.cur.execute(sql, (newID, firstName, lastName, address, city, cc))


        # get customer info and login
        self.cur.execute("SELECT (customerid) FROM customer_info WHERE firstname = %s AND lastname = %s", (firstName, lastName))

        response = self.cur.fetchone()

        if response is not None:
            customerID = response[0]

            self.hide()
            self.app2 = CustomerInterface(customerID)
            self.app2.show()
        else:
            msg = QMessageBox()
            msg.setText("Failed sign up. Try again.")
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
        self.ui.customerName.setText(str(self.customer.firstname + " " + self.customer.lastname))
        self.ui.points.setText(str(self.customer.points))
        
        self.cur.execute("SELECT * FROM orders WHERE customerID=%s AND paid=FALSE;", (str(customerID)))
        orders = self.cur.fetchall()
        
        
        
        for order in orders:
            for item in self.menu:
                if order[5] == item[0]:
                    orders_row_count = self.ui.tableWidget1.rowCount()
                    self.ui.tableWidget1.setRowCount(orders_row_count+1)
                    
                    for i in range(3):
                        
                        
                        if i == 2:
                            value = item[1] * 0.1
                        else:
                            value = item[i]
                        
                        cell = QtWidgets.QTableWidgetItem(str(value))
                        self.ui.tableWidget1.setItem(orders_row_count, i, cell)
                    if (order[7] == False):
                        cell = QtWidgets.QTableWidgetItem("Not ready")
                        self.ui.tableWidget1.setItem(orders_row_count, 3, cell)
                    else:
                        cell = QtWidgets.QTableWidgetItem("Ready")
                        self.ui.tableWidget1.setItem(orders_row_count, 3, cell)
                    
            
    
        self.ui.add.clicked = self.ui.add.clicked.connect(self.addItem)
        self.ui.submit.clicked = self.ui.submit.clicked.connect(self.submitOrder) 
        self.ui.pay.clicked = self.ui.pay.clicked.connect(self.payForOrder)
        self.ui.updateUser = self.ui.updateUser.clicked.connect(self.updateUserInfo)
        
    def payForOrder(self):
        checkoutform = CheckoutDialog(self.customer, self.cur, self.ui.tableWidget1)
        res = checkoutform.exec_()
        
    def updateUserInfo(self):
        if self.customer.firstname != "Anonymous":
            updateform = UpdateUserInfo(self.customer)
            res = updateform.exec_()
        
        
    def addItem(self):
        items = self.ui.tableWidget.selectedItems()
        if items:
            self.customer.orders.append(items[0].text())
        
        row_count = self.ui.tableWidget1.rowCount()
        self.ui.tableWidget1.setRowCount(row_count+1)
        
        for item in self.menu:
            if item[0] == items[0].text():
                for i in range(3):
                    
                    
                    if i == 2:
                        value = item[1] * 0.1
                    else:
                        value = item[i]
                    
                    cell = QtWidgets.QTableWidgetItem(str(value))
                    self.ui.tableWidget1.setItem(row_count, i, cell)
                
                cell = QtWidgets.QTableWidgetItem("Added")
                self.ui.tableWidget1.setItem(row_count, 3, cell)
                
    def submitOrder(self):
        
        if not self.customer.orders:
            msg = QMessageBox()
            msg.setText(f"Your order is empty!")
            msg.exec_()
            return
        
        index = 0

        # get last largest transaction ID
        self.cur.execute("SELECT MAX(transactionid) AS maxid FROM orders")
        result = self.cur.fetchall()

        largestID = 1
        ordertype = 0
        
        if self.ui.radioButton.isChecked():
            ordertype = 1
        elif self.ui.radioButton_2.isChecked():
            ordertype = 2
        elif self.ui.radioButton_3.isChecked():
            ordertype = 3
        else:
            msg = QMessageBox()
            msg.setText(f"Please select order type")
            msg.exec_()
            return
            
        for i in result:
            if i[0] is not None:
                largestID = int(i[0])
        
        # set new transaction ID to last largest + 1
        transactionID = largestID + 1
        time = 0
        

        for order in self.customer.orders:
            for item in self.menu:
                if order == item[0]:
                    
                    # insert all items with same transaction ID
                    self.cur.execute("""INSERT INTO orders (transactionid, typeoforder, datetime, customerid, item, price, ready, paid)
                    VALUES (%s, %s, %s, %s, %s, %s, FALSE, FALSE);
                    """,

                    (str(transactionID), str(ordertype), str(datetime.now()),
                     str(self.customer.id), str(item[0]), str(int(item[1]))))

                    time += item[2]  
                        
                    cell = QtWidgets.QTableWidgetItem("Submitted")
                    self.ui.tableWidget1.setItem(index, 3, cell)
                    
                    self.customer.points += item[2]
                    index = index + 1
        
        self.customer.orders = []
        
        msg = QMessageBox()
        msg.setText(f"Approximate Waiting Time {time} minutes")
        msg.exec_()
        
class CheckoutDialog(QDialog):
    def __init__(self, customer, cur, order_table, parent=None):
        QDialog.__init__(self, parent)
        cur.execute("SELECT price FROM orders WHERE customerid=%s AND paid=FALSE AND ready=TRUE", (str(customer.id)))
        
        self.order_table = order_table
        self.total = 0
        items = cur.fetchall()
        for item in items:
            self.total += item[0]
        
        self.ui = checkout_dialog()
        self.ui.setupUi(self)
        
        self.customer = customer
        self.cur = cur
        
        self.ui.label_5.setText("$" + str(self.total))
        self.ui.label_7.setText("$" + str(self.customer.points))
        
        self.ui.pushButton.clicked = self.ui.pushButton.clicked.connect(self.payByMoney)
        self.ui.pushButton_2.clicked = self.ui.pushButton_2.clicked.connect(self.payByPoints) 
        
        
    def payByMoney(self):
        update = "UPDATE orders SET paid = TRUE WHERE customerid = {}".format(str(self.customer.id))
        self.cur.execute(update)
        update = "UPDATE customer_info SET points = points + %s  WHERE customerid = %s" 
        self.cur.execute(update, (self.total*0.1, self.customer.id))
        
        msg = QMessageBox()
        msg.setText("Thank you for your payment")
        msg.exec_()
        
        self.order_table.setRowCount(0)
        self.order_table.setColumnCount(0)
        self.close()
        
    def payByPoints(self):
        if (self.customer.points > self.total):
            update = "UPDATE orders SET paid = TRUE WHERE customerid = {}".format(str(self.customer.id))
            self.cur.execute(update)
            
            if self.customer.firstname != "Anonymous":
                update = "UPDATE customer_info SET points = points + %s  WHERE customerid = %s" 
                self.cur.execute(update, (self.total*0.1, self.customer.id))
            
            msg = QMessageBox()
            msg.setText("Thank you for your payment")
            msg.exec_()
            
class UpdateUserInfo(QDialog):
    def __init__(self, customer, parent=None):
        QDialog.__init__(self, parent)
        self.ui = update_user_info()
        self.ui.setupUi(self)
        
        self.ui.firstNameLine.setText(customer.firstname)
        self.ui.lastNameLine.setText(customer.lastname)
        self.ui.addressLine.setText(customer.address)
        self.ui.creditCardLine.setText(customer.cardnumber)
        
        
class StaffInterface(QMainWindow):
    def __init__(self, staffID):
        super().__init__()
        self.ui = staff_interface()
        self.ui.setupUi(self)
        
        self.cur = connect()
        self.table = self.ui.ordersTableWidget

        self.ui.update_orders_btn.clicked.connect(self.updateTable)
        self.ui.gen_report_btn.clicked.connect(self.genReport)
        self.ui.logout_btn.clicked.connect(self.logout)
        self.updateTable()

    def updateTable(self):
        # select orders that have items that are not ready
        query = """SELECT orderitemid, transactionid, typeoforder, item, ready, 
                CASE WHEN COUNT(CASE WHEN ready = FALSE THEN 1 END) OVER (PARTITION BY transactionid) = 0 THEN 'Y' ELSE 'N' END
                FROM orders ORDER BY transactionid, orderitemid"""
        self.cur.execute(query)

        order_data = self.cur.fetchall()

        # only keep ordered items whose transactions still have items that are not ready
        order_data = list(filter(lambda order_row: order_row[-1] == 'N', order_data))

        self.table.setRowCount(len(order_data))

        index = 0
        order_rows = []

        #init rows
        for orderArr in order_data:
            order = Order(index, orderArr, self)
            order_rows.append(order)
            index += 1

        # add rows to table
        for order in order_rows:
            order.initRow()

        # init change status buttons
        for order in order_rows:
            order.initChangeBtn()

        
    def statusBtnClick(self, index, orderedItemId):       
        # change status of order row with ordereditemid = orderedItemId to ready = TRUE
        update = "UPDATE orders SET ready = TRUE WHERE orderitemid = {}".format(str(orderedItemId))
        self.cur.execute(update)

        # change table cell from 'Not Ready' to 'Ready'
        readyCell = QtWidgets.QTableWidgetItem('Ready')
        self.table.setItem(index, 3, readyCell)

        # refresh table, remove order if item was last to be ready
        self.updateTable()

    def logout(self):
        self.hide()
        self.app2 = Login()
        self.app2.show()

    def genReport(self):
         ### GO TO REPORT INTERFACE ###
         return

class Order():
    def __init__(self, index, orderArr, parent):
        super().__init__()
        if orderArr is not None:
            self.index = index
            self.orderItemId = orderArr[0]
            self.transactionId = orderArr[1]
            self.typeOfOrder = orderArr[2]
            self.itemName = orderArr[3]
            self.status = 'Not Ready' if orderArr[4] == False else 'Ready'
            self.parent = parent
        else:
            self.orderItemId = 0
            self.transactionId = 0
            self.typeOfOrder = 1
            self.itemName = 'Undefined'
            self.status = 'Not Ready'
            self.parent = None

    def initRow(self):
        idCol = QtWidgets.QTableWidgetItem(str(self.orderItemId))
        orderNumCol = QtWidgets.QTableWidgetItem(str(self.transactionId))
        typeCol = QtWidgets.QTableWidgetItem(self.getTypeStr(self.typeOfOrder))
        dishNameCol = QtWidgets.QTableWidgetItem(str(self.itemName))
        statusCol = QtWidgets.QTableWidgetItem(str(self.status))

        self.parent.table.setItem(self.index, 0, idCol)
        self.parent.table.setItem(self.index, 1, orderNumCol)
        self.parent.table.setItem(self.index, 2, typeCol)
        self.parent.table.setItem(self.index, 3, dishNameCol)
        self.parent.table.setItem(self.index, 4, statusCol)

    def initChangeBtn(self):
        change_btn = QtWidgets.QPushButton('Item Ready')
        self.parent.table.setCellWidget(self.index, 5, change_btn)
        if self.status == 'Ready':
            change_btn.setDisabled(True)
        change_btn.clicked.connect(partial(self.parent.statusBtnClick, self.index, self.orderItemId))

    def getTypeStr(self, typeInt):
        typeMap = {
            1 : 'Dine-In',
            2 : 'Pickup',
            3 : 'Delivery'
        }
        return typeMap.get(typeInt)

class Customer():
    def __init__(self, customer_data):
        if customer_data is not None:
            self.id = customer_data[0]
            self.firstname = customer_data[1] 
            self.lastname = customer_data[2]
            self.address = customer_data[3] + " " + customer_data[4]
            self.cardnumber = customer_data[5]
            self.points = customer_data[6]
            self.orders = []
        else:
            self.id = 0
            self.firstname = "Anonymous"
            self.lastname = ""
            self.address = None
            self.cardnumber = None
            self.points = 0
            self.orders = []
    
        
def connect():
    conn = None
    
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="cs487_app",
            user="developer",
            password="1")
        
        conn.autocommit = True
        
        cur = conn.cursor()

        return cur
       
	# close the communication with the PostgreSQL
        #cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
                

app = QtWidgets.QApplication(sys.argv)
gui = Login()
gui.show()
sys.exit(app.exec_())










