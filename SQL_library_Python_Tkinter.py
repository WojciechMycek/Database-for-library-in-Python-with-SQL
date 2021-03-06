from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("SQL Library Python")
root.geometry("1200x400")


#create a database

conn = sqlite3.connect('Library_app.db')


#create cursor
c = conn.cursor()

#c.execute('''CREATE TABLE books(
#   books_id INT PRIMARY KEY,
#   tittle text,
#   author text,
#   who_get_it text,
#   publishing_house text,
#   date integer
#)''')


#c.execute('''CREATE TABLE users(
#    borrowed_book INT PRIMARY KEY,
#    vorname text,
#    name text,
#    user_id integer,
#    adress text,
#    FOREIGN KEY(borrowed_book) REFERENCES books(books_id) ON DELETE SET NULL
#)''')


def add():
    conn = sqlite3.connect('Library_app.db')
    #create cursor
    c = conn.cursor()

    #Insert into Table
    c.execute("INSERT INTO books VALUES (:tittle, :author,:who_get_it,:publishing_house,:date,:books_id)",
        {
            'tittle':tittle.get(),
            'author':author.get(),
            'who_get_it':who_get_it.get(),
            'publishing_house':publishing_house.get(),
            'date':date.get(),
            'books_id':book_id.get()
        }
    )

    

    #commit Changes
    conn.commit()   

    #Close Connection
    conn.close()

    tittle.delete(0,END)
    author.delete(0,END)
    who_get_it.delete(0,END)
    publishing_house.delete(0,END)
    date.delete(0,END)

def add_users():
    conn = sqlite3.connect('Library_app.db')
    #create cursor
    c = conn.cursor()

    #Insert into Table
    c.execute("INSERT INTO users VALUES (:vorname, :name,:address,:user_id)",
        {
            'vorname':vorname.get(),
            'name':name.get(),
            'address':adress.get(),
            'user_id':user_id.get(),
            
        }
    )

    

    #commit Changes
    conn.commit()   

    #Close Connection
    conn.close()

    tittle.delete(0,END)
    author.delete(0,END)
    who_get_it.delete(0,END)
    publishing_house.delete(0,END)
    date.delete(0,END)

def show():
    conn = sqlite3.connect('Library_app.db')
    #create cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM books")
    records=c.fetchall()#fetch all records
    print(records)

    #Loop thru Results
    print_records=""
    for record in records:
        print_records += str(record) + "\n"
    
    query_label = Label(root,text=print_records)
    query_label.grid(row=9,column=0,columnspan=2)

    #commit Changes
    conn.commit()   

    #Close Connection
    conn.close()

def show_users():
    conn = sqlite3.connect('Library_app.db')
    #create cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM users")
    records=c.fetchall()#fetch all records
    print(records)

    #Loop thru Results
    print_records=""
    for record in records:
        print_records += str(record) + "\n"
    
    query_label = Label(root,text=print_records)
    query_label.grid(row=7,column=2,columnspan=2)

    #commit Changes
    conn.commit()   

    #Close Connection
    conn.close()

#date of books
tittle = Entry(root, width=35)
tittle.grid(row=0,column=1, padx=30,pady=(10,0))

author = Entry(root, width=35)
author.grid(row=1,column=1, padx=20)

who_get_it = Entry(root, width=35)
who_get_it.grid(row=2,column=1, padx=20)

publishing_house = Entry(root, width=35)
publishing_house.grid(row=3,column=1, padx=20)

date = Entry(root, width=35)
date.grid(row=4,column=1, padx=20)

book_id = Entry(root,width=35)
book_id.grid(row=5,column=1,padx=20)

#print names of priting data

tittle_label = Label(root,text="Tittle'Books")
tittle_label.grid(row=0,column=0,pady=(10,0))

author_label = Label(root,text="Author's Book")
author_label.grid(row=1,column=0)

who_get_it_label = Label(root,text="Who get it")
who_get_it_label.grid(row=2,column=0)


publishing_label = Label(root,text="Published by")
publishing_label.grid(row=3,column=0)

date_label = Label(root,text="Date")
date_label.grid(row=4,column=0)

book_id_label = Label(root,text="Book_id")
book_id_label.grid(row=5,column=0)

# Create Add Button
submit_btn = Button(root, text="Add book", command=add)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=134)

#Create a Query Button
query_btn = Button(root,text="Show records",command=show)
query_btn.grid(row=7, column=0,columnspan=2,pady=10,padx=10,ipadx=125)

#-----------------------------------------------------------------------

#date of users
vorname = Entry(root, width=35)
vorname.grid(row=0,column=3, padx=30,pady=(10,0))

name = Entry(root, width=35)
name.grid(row=1,column=3, padx=20)

adress = Entry(root, width=35)
adress.grid(row=2,column=3, padx=20)

user_id = Entry(root, width=35)
user_id.grid(row=3,column=3, padx=20)

#print names of priting data
vorname_label= Label(root,text="Vorname")
vorname_label.grid(row=0,column=2,pady=(10,0))

name_label = Label(root,text="Name")
name_label.grid(row=1,column=2)

address_label = Label(root,text="Address")
address_label.grid(row=2,column=2)


user_id_label = Label(root,text="User id: ")
user_id_label.grid(row=3,column=2)

# Create Add User Button
submit_btn = Button(root, text="Add user", command=add_users)
submit_btn.grid(row=5,column=2,columnspan=2,pady=10,padx=10,ipadx=134)

#Create a show users Button
query_btn = Button(root,text="Show users",command=show_users)
query_btn.grid(row=6, column=2,columnspan=2,pady=10,padx=10,ipadx=125)

#---------------------------------------------------------------------
#looking for users or books
user_id_look_for = Entry(root, width=35)
user_id_look_for.grid(row=0,column=5, padx=20)

user_id_look_for = Label(root,text="Lk for user id")
user_id_look_for.grid(row=0,column=4,pady=(10,0))

look_for_book = Entry(root, width=35)
look_for_book.grid(row=1,column=5, padx=20)

look_for_book = Label(root,text="Lk for book")
look_for_book.grid(row=1,column=4,pady=(10,0))

# Create Add User Button
show_users_by_id = Button(root, text="Show users")
show_users_by_id.grid(row=2,column=4,columnspan=2,pady=10,padx=10,ipadx=129)

#Create a show users Button
show_books_by_id = Button(root,text="Show books")
show_books_by_id.grid(row=3, column=4,columnspan=2,pady=10,padx=10,ipadx=125)

#try

#commit Changes
conn.commit()   

#Close Connection
conn.close()

root.mainloop()