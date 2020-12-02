#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Sales_report(QDialog):
    def __init__(self,order_table,cur,parent=None):
            QDialog.__init__(self, parent)
            super().__init__()
        
            self.cur = connect()
            
            self.ui = customer_interface()
            self.ui.setupUi(self)
            self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
            self.dateEdit.setGeometry(QtCore.QRect(10, 80, 151, 21))
            self.dateEdit.setObjectName("dateEdit")
            
            date = str(self.dateEdit.date())
            
            self.cur.execute("SELECT * FROM orders WHERE date LIKE '%s%'",date)
            self.menu = self.cur.fetchall()
            
            totalnumberofsales = self.cur.execute("SELECT COUNT (orderitemid) FROM orders WHERE date LIKE '%s%'",date)
            totalprice = self.cur.execute("SELECT SUM (Price) FROM orders WHERE date LIKE '%s%'",date)
            toptendishes = self.cur.execute("SELECT Item FROM orders GROUP BY Item  ORDER BY COUNT (*) DESC LIMIT 10 WHERE date LIKE '%s%' ",date)
            
            
            
            self.ui.label_2.setText("$" + str(self.total))
            self.ui.label_2.setText("The total number of sales on" + date + "is" + str(totalnumberofsales) + "and the total sale made is $" + str(totalprice)+ "\n The top 10 dishes are :" + str(toptendishes))
            

            
            
            
            
            
        
        


# In[3]:


from datetime import datetime
str(datetime.now())


# In[ ]:




