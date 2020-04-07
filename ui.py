from tkinter import *
import os
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="grocery-store"
)
mycursor=mydb.cursor()
def register_user():
	uname=username_entry.get()
	pswd=password_entry.get()
	username=""
	Select="select username,password from user_accounts where username='%s'" %(uname)
	mycursor.execute(Select)
	result=mycursor.fetchall()
	for i in result:
		username=i[0]
		password=i[1]
	if(username == uname and password==pswd):
		messagebox.askokcancel("Information","Record Already exists")
	else:
		Insert="Insert into user_accounts(username,password) values(%s,%s)"
		if(uname !="" and pswd!=""):
			Value=(uname,pswd)
			mycursor.execute(Insert,Value)
			mydb.commit()
			messagebox.askokcancel("Information","Record inserted")
			username_entry.delete(0, END)
			password_entry.delete(0, END)
		else:
			if (uname == "" and pswd == ""):
				messagebox.askokcancel("Information","New Entery Fill All Details")
			else:
				messagebox.askokcancel("Information", "Some fields left blank")
	Label(main_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
def login_user():
	uname=username_entry.get()
	pswd=password_entry.get()
	username=""
	Select="select username,password from user_accounts where username='%s'" %(uname)
	mycursor.execute(Select)
	result=mycursor.fetchall()
	for i in result:
		username=i[0]
		password=i[1]
	if(username == uname and password==pswd):
		Label(main_screen, text="Login Success", fg="green",font = ('',20),pady=5,padx=5).pack()
		mydb.close()
		main_screen.destroy()
		import manager
		a=manager()
	else:
		Label(main_screen, text="Login Failed", fg="red",font = ('',20),pady=5,padx=5).pack()
		username_entry.delete(0, END)
		password_entry.delete(0, END)
			
main_screen = Tk()
main_screen.geometry("600x600")
main_screen.title("User accounts")
photo=PhotoImage(file='image.png')
label12=Label(main_screen,image=photo,pady=2,padx=2.5).pack()
Label(main_screen, text="Please enter details below", bg="blue",font = ('',20),pady=5,padx=5).pack()
Label(main_screen, text="").pack()
username_lable = Label(main_screen, text="Username * ",font = ('',20),pady=5,padx=5)
username_lable.pack()
username_entry = Entry(main_screen,bd = 5,font = ('',15))
username_entry.pack()
password_lable = Label(main_screen, text="Password * ",font = ('',20),pady=5,padx=5)
password_lable.pack()
password_entry = Entry(main_screen, show='*',bd = 5,font = ('',15))
password_entry.pack()
Label(main_screen, text="").pack()
Button(main_screen, text="login", width=10, height=1, bg="blue",bd = 3 ,font = ('',15),padx=5,pady=5,command=login_user).pack()
Button(main_screen, text="register", width=14, height=1, bg="blue",bd = 3 ,font = ('',15),padx=5,pady=5,command=register_user).pack()
main_screen.mainloop()
