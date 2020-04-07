from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import ImageTk,Image  

def insert():
    id=e_id.get()
    name=e_name.get()
    price=e_price.get()
    cat=e_cat.get()
    life=e_life.get()
    image=e_image.get()
    vendorid=e_vendorid.get()

    if(id=="" or name=="" or price=="" or cat=="" or life=="" or image=="" or vendorid==""):
        MessageBox.showinfo("Insert Status","All fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="grocery-store")
        cursor = con.cursor()
        

        #pic=convertToBinaryData(image)
        #im = Image.open(image)
        #blob_value = open(image, 'rb').read()
        try:
            sql="insert into items values(%s,%s,%s,%s,%s,%s,%s)"
            args=(id,name,price,cat,life,image,vendorid)
            cursor.execute(sql,args)
            cursor.execute("commit")
            MessageBox.showinfo("Insert Status","Inserted Successfully")
            
        except (mysql.Error, mysql.Warning) as e:
            MessageBox.showinfo("Insert Status Error",e)
                
        finally:        
            e_id.delete(0,'end')
            e_name.delete(0,'end')
            e_price.delete(0,'end')
            e_cat.delete(0,'end')
            e_life.delete(0,'end')
            e_image.delete(0,'end')
            e_vendorid.delete(0,'end')
            
            con.close();

def update():
    id=e_id.get()
    name=e_name.get()
    price=e_price.get()
    cat=e_cat.get()
    life=e_life.get()
    image=e_image.get()
    vendorid=e_vendorid.get()
    
    if(id=="" or (name=="" and price=="" and cat=="" and life=="" and image=="" and vendorid=="")):
        MessageBox.showinfo("Update Status","Id and one other field is required")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="grocery-store")
        cursor = con.cursor()
        
        
        try:
            if(name!=""):
                try:
                    cursor.execute("update items set Name='"+name+"' where ItemID='"+id+"'" )
                except (mysql.Error, mysql.Warning) as e:
                    MessageBox.showinfo("Update Status Error",e)
            if(price!=""):
                try:
                    cursor.execute("update items set Price='"+price+"' where ItemID='"+id+"'" )
                except (mysql.Error, mysql.Warning) as e:
                    MessageBox.showinfo("Update Status Error",e)
            if(cat!=""):
                try:
                    cursor.execute("update items set Category='"+cat+"' where ItemID='"+id+"'" )
                except (mysql.Error, mysql.Warning) as e:
                    MessageBox.showinfo("Update Status Error",e)
            if(life!=""):
                try:
                    cursor.execute("update items set Shelllife='"+life+"' where ItemID='"+id+"'" )
                except (mysql.Error, mysql.Warning) as e:
                    MessageBox.showinfo("Update Status Error",e)
            if(vendorid!=""):
                try:
                    cursor.execute("update items set VendorId='"+vendorid+"' where ItemID='"+id+"'" )
                except (mysql.Error, mysql.Warning) as e:
                    MessageBox.showinfo("Update Status Error",e)
            if(image!=""):
                try:
                    #pic=convertToBinaryData(image)
                    #blob_value = open(image, 'rb').read()
                    sql="update items set Image=%s where ItemId=%s"
                    args=(image,id)
                    cursor.execute(sql,args)
                except (mysql.Error, mysql.Warning) as e:
                    MessageBox.showinfo("Update Status Error",e)
                    
            cursor.execute("commit")
            MessageBox.showinfo("Update Status","Updated Successfully")
        except (mysql.Error, mysql.Warning) as e:
                    MessageBox.showinfo("Update Status Error",e)
        finally:
            e_id.delete(0,'end')
            e_name.delete(0,'end')
            e_price.delete(0,'end')
            e_cat.delete(0,'end')
            e_life.delete(0,'end')
            e_image.delete(0,'end')
            e_vendorid.delete(0,'end')
            
            con.close();

def delete():
    if (e_id.get() == ""):
        MessageBox.showinfo("Delete Status","ID is compulsory for delete")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="grocery-store")
        cursor=con.cursor()
        cursor.execute("delete from items where ItemId='"+ e_id.get() +"'")
        cursor.execute("commit")

        e_id.delete(0,'end')
        MessageBox.showinfo("Delete Status","Deleted Successfully")
        con.close()

def get():
    if (e_id.get() == ""):
        MessageBox.showinfo("Fetch Status","ID is compulsory for Fetch")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="grocery-store")
        cursor=con.cursor()
        cursor.execute("select * from items where ItemId='"+ e_id.get() +"'")
        rows=cursor.fetchall()
        print(type(rows[0][5]))
        for row in rows:
            e_name.insert(0,row[1])
            e_price.insert(0,row[2])
            e_cat.insert(0,row[3])
            e_life.insert(0,row[4])
            img = Image.open(row[5])
            img=img.resize((200,200),Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            #img = img.resize((150, 150),Image.ANTIALIAS)
            panel = Label(root, image = img)
            panel.image=img
            panel.place(x=270,y=30)
            #panel.pack(side = "bottom", fill = "both", expand = "yes")
            #panel.place(x=230,y=30)
            e_vendorid.insert(0,row[6])
        con.close()


con=mysql.connect(host="localhost",user="root",password="",database="grocery-store")
cursor = con.cursor()
cursor.execute("create table if not exists vendor(vendorid int not null,\
                                                    name varchar(10) not null,\
                                                   primary key (vendorid)) COLLATE='utf8_general_ci' ENGINE=InnoDB")
cursor.execute("create table if not exists items(ItemId char(3) not null,\
                                                Name varchar(30) not null,\
                                                Price decimal not null,\
                                                Category varchar(30) not null,\
                                                ShelfLife int not null,\
                                                Image varchar(15) not null,\
                                                VendorId int not null ,\
                                                Foreign Key (VendorId) REFERENCES vendor(vendorid),\
                                                primary key (ItemId)) COLLATE='utf8_general_ci' ENGINE=InnoDB")

cursor.execute("commit")
con.close()

root=Tk()
root.geometry("600x300")
root.title("Grocery Store Manager")

id=Label(root,text='Enter ID',font=('bold',10))
id.place(x=20,y=30)

name=Label(root,text='Enter Name',font=('bold',10))
name.place(x=20,y=60)

price=Label(root,text='Enter Price',font=('bold',10))
price.place(x=20,y=90)

cat=Label(root,text='Enter Category',font=('bold',10))
cat.place(x=20,y=120)

life=Label(root,text='Enter Shelf Life',font=('bold',10))
life.place(x=20,y=150)

image=Label(root,text='Upload Image',font=('bold',10))
image.place(x=20,y=180)

vendorid=Label(root,text='Enter vendorid',font=('bold',10))
vendorid.place(x=20,y=210)

e_id=Entry()
e_id.place(x=150,y=30)

e_name=Entry()
e_name.place(x=150,y=60)

e_price=Entry()
e_price.place(x=150,y=90)

e_cat=Entry()
e_cat.place(x=150,y=120)

e_life=Entry()
e_life.place(x=150,y=150)

#need to change later to upload image
e_image=Entry()
e_image.place(x=150,y=180)

e_vendorid=Entry()
e_vendorid.place(x=150,y=210)

insert=Button(root,text="Insert",font=("italic",10),bg="white",command=insert)
insert.place(x=20,y=240)

update=Button(root,text="Update",font=("italic",10),bg="white",command=update)
update.place(x=130,y=240)

delete=Button(root,text="Delete",font=("italic",10),bg="white",command=delete)
delete.place(x=70,y=240)


get=Button(root,text="Get",font=("italic",10),bg="white",command=get)
get.place(x=190,y=240)

root.mainloop()
