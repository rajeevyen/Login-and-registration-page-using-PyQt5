import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector
from mydbutils import do_query

class LoginApp(QDialog):
	def __init__(self):
		super(LoginApp,self).__init__()
		loadUi("login-form.ui",self)
		self.b1.clicked.connect(self.login)
		self.b2.clicked.connect(self.show_reg)

	def login(self):
	   	un = self.tb1.text()
	   	pw = self.tb2.text()
	   	#print(un)
	   	#print(pw)
	   	sql = "SELECT * FROM project.userlist where username = '" + un + "' and password = '" + pw + "'"
	   	rows, count = do_query(sql)
	   	self.tb1.setText("")
	   	self.tb2.setText("")
	   	if rows:
	   	    QMessageBox.information(self,"Login Output","Congrats! you login successfully")
	   	else:
	   	    QMessageBox.information(self,"Login Output","Invalid User, Register for new user")

	def show_reg(self):
	    widget.setCurrentIndex(1)	

        

class RegApp(QDialog):
	def __init__(self):
		super(RegApp,self).__init__()
		loadUi("register-form.ui",self)
		self.b3.clicked.connect(self.reg)
		self.b4.clicked.connect(self.show_login)

	def reg(self):
		un = self.tb3.text()
		pw = self.tb4.text()
		mail = self.tb5.text()
		ph = self.tb6.text()

		sql1 = "SELECT * FROM project.userlist where username = '" + un + "' and password = '" + pw + "'"

		rows, count = do_query(sql1)
		if rows:
			QMessageBox.information(self,"Login Form", "The user already registered, Try another username")
		else:
			sql2 = "INSERT INTO project.userlist VALUES('" + un + "','" + pw + "','" + mail + "','" + ph + "')"
			rows, count = do_query(sql2)
			QMessageBox.information(self,"Login Form", "The user registered successfully, You can login now!!!")

	def show_login(self):
		widget.setCurrentIndex(0)




app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginform = LoginApp()
registrationform = RegApp()
widget.addWidget(loginform)
widget.addWidget(registrationform)
widget.setCurrentIndex(0)
widget.setFixedWidth(400)
widget.setFixedHeight(500)
widget.show()

app.exec_()