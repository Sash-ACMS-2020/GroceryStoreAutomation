from tkinter import *
import os
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

"""def insert():
    Vendor_id = e_id.get()
    Phone_no = e_Phone_no.get()
    address = e_add.get()

    if(Vendor_id == "" or Phone_no == "" or address == ""):
        MessageBox.showinfo("Insert status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user = "root", password = "shreya0312", database = "grocerystore")
        cursor = con.cursor()
        cursor.execute("insert into vendor values('"+ Vendor_id +"', '" +Phone_no+ "' ,'"+address+"')")
        cursor.execute("commit")

        e_id.delete(0,'end')
        e_Phone_no.delete(0,'end')
        e_add.delete(0,'end')

        show()
        MessageBox.showinfo("Insert status","Inserted successfully")
        con.close()"""

def delete():
    if(e_id.get() == ""):
        MessageBox.showinfo("Delete Status","Id is compulsary for delete")
    else:
        con = mysql.connect(host="localhost", user = "root", password = "shreya0312", database = "grocerystore")
        cursor = con.cursor()
        cursor.execute("delete from vendor where Vendor_id ='"+ e_id.get() +"'")
        cursor.execute("commit")

        e_id.delete(0,'end')
        e_Phone_no.delete(0,'end')
        e_add.delete(0,'end')
        e_user.delete(0,'end')
        e_store.delete(0,'end')

        #show()
        MessageBox.showinfo("Delete status","Deleted successfully")
        con.close()

def update():
    Vendor_id = e_id.get()
    Phone_no = e_Phone_no.get()
    address = e_add.get()
    Username = e_user.get()
    store_name = e_store.get()

    if(Vendor_id == "" or Phone_no == "" or address == "" or Username =="" or store_name =="" ):
        MessageBox.showinfo("Update status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user = "root", password = "shreya0312", database = "grocerystore")
        cursor = con.cursor()
        cursor.execute("update vendor set Phone_no='"+ Phone_no+"', address ='"+ address+"', Vendor_username = '"+ Username+"', Store_name = '"+ store_name+"' where Vendor_id = '"+ Vendor_id +"'")
        cursor.execute("commit")

        e_id.delete(0,'end')
        e_Phone_no.delete(0,'end')
        e_add.delete(0,'end')
        e_user.delete(0,'end')
        e_store.delete(0,'end')

        #show()
        MessageBox.showinfo("Update status","Updated successfully")
        con.close()

def get():
    if(e_id.get() == ""):
        MessageBox.showinfo("Fetch Status","Id is compulsary for delete")


    else:
        con = mysql.connect(host="localhost", user = "root", password = "shreya0312", database = "grocerystore")
        cursor = con.cursor()
        cursor.execute("select * from vendor where Vendor_id='"+ e_id.get()+"'")
        rows = cursor.fetchall()

        for row in rows:
            e_add.insert(0, row[4])
            e_Phone_no.insert(0, row[3])
            e_user.insert(0, row[1])
            e_store.insert(0, row[5])
            
        con.close()

"""def show():
    con = mysql.connect(host="localhost", user = "root", password = "shreya0312", database = "grocerystore")
    cursor = con.cursor()
    cursor.execute("select * from vendor")
    rows = cursor.fetchall()
    #list.delete(0, list.size())
    for row in rows :
        insertdata = format(row[0])+'      '+row[4]
        list.insert(END,insertdata)
    
        
    con.close()"""

def clear():
    Vendor_id = e_id.get()
    Phone_no = e_Phone_no.get()
    address = e_add.get()
    Username = e_user.get()
    store_name = e_store.get()

    con = mysql.connect(host="localhost", user = "root", password = "shreya0312", database = "grocerystore")
    cursor = con.cursor()
    cursor.execute("update vendor set Phone_no='"+ Phone_no+"', address ='"+ address+"', Vendor_username = '"+ Username+"', Store_name = '"+ store_name+"' where Vendor_id = '"+ Vendor_id +"'")
    cursor.execute("commit")

    e_id.delete(0,'end')
    e_Phone_no.delete(0,'end')
    e_add.delete(0,'end')
    e_user.delete(0,'end')
    e_store.delete(0,'end')

    #MessageBox.showinfo("Update status","Updated successfully")
    con.close()

    
    
def admin():
    global screen6
    global e_id
    global e_Phone_no
    global e_add
    global e_user
    global e_store
    
    screen6 = Toplevel(screen)
    screen6.geometry("600x250")
    screen6.title("administrator")

    Vendor_id = Label(screen6,text = "V_Id", font = ("calibri",10))
    Label(text = "")
    
    Phone_no = Label(screen6,text = "V_Phone_no", font = ("calibri",10))
    Label(text = "")
    
    address = Label(screen6,text = "V_Address", font = ("calibri",10))
    Label(text = "")
    
    Username = Label(screen6,text = "V_Username", font = ("calibri",10))
    Label(text = "")
    
    Store_name = Label(screen6,text = "V_store_name", font = ("calibri",10))

    

    Label(screen6, text = " ID ").pack()
    e_id = Entry(screen6, textvariable = Vendor_id)
    e_id.pack()

    Label(text = "")

    Label(screen6, text = " Phone_no ").pack()
    e_Phone_no = Entry(screen6, textvariable = Phone_no)
    e_Phone_no.pack()

    Label(text = "")

    Label(screen6, text = " Address ").pack()
    e_add = Entry(screen6, textvariable = address)
    e_add.pack()

    Label(text = "")
    Label(screen6, text = " UserName ").pack()
    e_user = Entry(screen6, textvariable = Username)
    e_user.pack()

    Label(text = "")

    Label(screen6, text = " StoreName ").pack()
    e_store = Entry(screen6, textvariable = Store_name)
    e_store.pack()

    Label(text = "")
    
    Clear = Button(screen6, text = "Clear", font= ("italics", 10),bg = "white",width = 10, height=1,command = clear)
    Clear.pack(side=LEFT)

    Delete = Button(screen6, text = "Delete", font= ("italics", 10),bg = "white",width =10, height =1,command = delete)
    Delete.pack(side=LEFT)
    
    Update = Button(screen6, text = "Update", font= ("italics", 10),bg = "white",width =10, height=1,command = update)
    Update.pack(side=LEFT)

    Get = Button(screen6, text = "Get", font= ("italics", 10),bg = "white",width=10 , height=1,command = get)
    Get.pack(side=LEFT)
    
    """list = Listbox(screen6)
    list.place(x=410, y=50)
    show()"""

def supplier():
  import manager
  a = manager
     
"""def login_sucess():
  global screen3
  
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login Sucess").pack()
  Button(screen3, text = "OK", command = who).pack()"""

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()

  

  


def func(value):
    
    if value=='Admin':
            con = mysql.connect(host="localhost", user = "root", password = "shreya0312", database = "grocerystore")
            cursor = con.cursor()
            user=username_entry.get()
            passwd=password_entry.get()
            phonenum=phoneno_entry.get()
            addresss=address_entry.get()
            key1=5
            key1=int(key1)
            s1=""
#Encryption
            for k in range(len(passwd)) :
              char=passwd[k]
              if (char.isupper()):
                  s1=s1+chr((ord(char)+key1-65)%26+65)
              else:
                  s1=s1+chr((ord(char)+key1-97)%26+97)
        
            passwd=s1
            
            cursor.execute("insert into admin (Admin_username,Admin_password,Phone_no,Address) values ('"+ user +"', '" +passwd+ "' ,'"+phonenum+"','"+ addresss +"')")
            cursor.execute("commit")
            
            MessageBox.showinfo("Insert status","Inserted successfully")
            con.close()
    elif value=='Vendor':
            con = mysql.connect(host="localhost", user = "root", password = "shreya0312", database = "grocerystore")
            cursor = con.cursor()
            user=username_entry.get()
            passwd=password_entry.get()
            phonenum=phoneno_entry.get()
            addresss=address_entry.get()
            key2=5
            key2=int(key2)
            s2=""
#Encryption
            for k in range(len(passwd)) :
              char=passwd[k]
              if (char.isupper()):
                  s2=s2+chr((ord(char)+key2-65)%26+65)
              else :
                  s2=s2+chr((ord(char)+key2-97)%26+97)
        
            passwd=s2
            cursor.execute("insert into vendor(Vendor_username,Vendor_Password,Phone_no,Address) values('"+ user +"', '" +passwd+ "' ,'"+phonenum+"','"+ addresss +"')")
            cursor.execute("commit")
            
            MessageBox.showinfo("Insert status","Inserted successfully")
            con.close()

    elif value=='Supplier':
            con = mysql.connect(host="localhost", user = "root", password = "shreya0312", database = "grocerystore")
            cursor = con.cursor()
            user=username_entry.get()
            passwd=password_entry.get()
            phonenum=phoneno_entry.get()
            addresss=address_entry.get()
            key3=5
            key3=int(key3)
            s3=""
#Encryption
            for k in range(len(passwd)) :
              char=passwd[k]
              if (char.isupper()):
                  s3=s3+chr((ord(char)+key3-65)%26+65)
              else:
                  s3=s3+chr((ord(char)+key3-97)%26+97)
        
            passwd=s3
            
            cursor.execute("insert into supplier (username,Password,Phone_no,Address) values ('"+ user +"', '" +passwd+ "' ,'"+phonenum+"','"+ addresss +"')")
            cursor.execute("commit")
            
            MessageBox.showinfo("Insert status","Inserted successfully")
            con.close()
            
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    phoneno_entry.delete(0, END)
    address_entry.delete(0, END)
            
def func_login(value):
    global username1
    global password1
    username1 = username_verify.get()
    password1 = password_verify.get()
    
  
    key=5
    key=int(key)
    s=""
#Encryption
    for k in range(len(password1)) :
      char=password1[k]
      if (char.isupper()):
         s=s+chr((ord(char)+key-65)%26+65)
      else :
         s=s+chr((ord(char)+key-97)%26+97)
        
    password1=s
    if value=='Admin':
        connection =mysql.connect(host='localhost',
                                         database='grocerystore',
                                         user='root',
                                         password='shreya0312')
        sql_select_Query = "select * from admin"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall() 
        a=0
        for row in records:
            name=row[1]
            pswd=row[2]
            if (name==username1 ):
                if(pswd==password1):
                    a=1
                    admin()
                    break
                else:
                    a=2
                    password_not_recognised()
                    break
            
        if(a==0):    
            user_not_found()
       
                
    elif value=='Vendor':
        connection =mysql.connect(host='localhost',
                                         database='grocerystore',
                                         user='root',
                                         password='shreya0312')
        sql_select_Query = "select * from vendor"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        p=0
        for row in records:
            name=row[1]
            pswd=row[2]
            if (name==username1):
                if(pswd==password1):
                    p=1
                    login_sucess()
                    break
                else:
                    p=2
                    password_not_recognised()
                    break
            
        if(p==0):    
            user_not_found()

    elif value=='Supplier':
        connection =mysql.connect(host='localhost',
                                         database='grocerystore',
                                         user='root',
                                         password='shreya0312')
        sql_select_Query = "select * from supplier"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        p=0
        for row in records:
            name=row[1]
            pswd=row[3]
            if (name==username1):
                if(pswd==password1):
                    p=1
                    supplier()
                    break
                else:
                    p=2
                    password_not_recognised()
                    break
            
        if(p==0):    
            user_not_found()
                
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
        
def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x400")
  
  global username
  global password
  global phoneno
  global address
  global role
  

  global username_entry
  global password_entry
  global phoneno_entry
  global address_entry
    
  username = StringVar()
  password = StringVar()
  phoneno = StringVar()
  address = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
    
  Label(screen1, text = "Please select role").pack()
  Label(screen1, text = "").pack()
    
  OptionList = ["Admin","Vendor","Supplier","Customer"] 
  
  role = StringVar()
  role.set(OptionList[0])
  #option=role.get()
  #print(option)
  opt = OptionMenu(screen1, role, *OptionList,command=func)
  
  opt.config(width=40, font=('Helvetica', 12))
  opt.pack()
  
      

  Label(screen1, text = "Username * ").pack()
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  
  Label(screen1, text = "Phone_no * ").pack()
  phoneno_entry = Entry(screen1, textvariable = phoneno)
  phoneno_entry.pack()

  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password,show="*")
  password_entry.pack()
    
  Label(screen1, text = "Address * ").pack()
  address_entry = Entry(screen1, textvariable = address)
  address_entry.pack()
  
  
  

  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = func).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x350")
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
    
    
  Label(screen2, text = "Please select role").pack()
  Label(screen2, text = "").pack()
    
  OptionList = ["Admin","Vendor","Supplier","Customer"] 
  
  role = StringVar()
  role.set(OptionList[0])
  #option=role.get()
  #print(option)
  opt = OptionMenu(screen2, role, *OptionList,command=func_login)
  
  opt.config(width=40, font=('Helvetica', 12))
  opt.pack()
  
    
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify,show="*")
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = func_login).pack()
  
  
def main_screen():
  global screen
  
  screen = Tk()
  screen.geometry("400x450")
  photo=PhotoImage(file='image.png')
  label2=Label(image=photo,pady=2,padx=2.5).pack()
  screen.title("Grocery - Store")
  Label(text = "Grocery-Store", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()

  
  Button(text = "Register",height = "2", width = "30", command = register).pack()
  
 
  screen.mainloop()
  
main_screen()
