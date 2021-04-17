from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("SQL Library Python")
root.geometry("1100x400")


#create a database

conn = sqlite3.connect('Library_app.db')


#create cursor
c = conn.cursor()

#c.execute('''CREATE TABLE books(
#   tittle text,
#   author text,
#   who_get_it text,
#   publishing_house text,
#   date integer
#)''')

def add():
    conn = sqlite3.connect('Library_app.db')
    #create cursor
    c = conn.cursor()

    #Insert into Table
    c.execute("INSERT INTO books VALUES (:tittle, :author,:who_get_it,:publishing_house,:date)",
        {
            'tittle':tittle.get(),
            'author':author.get(),
            'who_get_it':who_get_it.get(),
            'publishing_house':publishing_house.get(),
            'date':date.get()
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
    conn = sqlite3.connect('Library_users.db')
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
    query_label.grid(row=7,column=0,columnspan=2)

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

#print names of priting data
date = Entry(root, width=35)
date.grid(row=4,column=1, padx=20)

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

# Create Add Button
submit_btn = Button(root, text="Add record to Database", command=add)
submit_btn.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#Create a Query Button
query_btn = Button(root,text="Show records",command=show)
query_btn.grid(row=6, column=0,columnspan=2,pady=10,padx=10,ipadx=125)

#commit Changes
conn.commit()   

#Close Connection
conn.close()

root.mainloop()