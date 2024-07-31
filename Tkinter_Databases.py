from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Tkinter Tutorials")
root.geometry("400x400")
# Databases

# Create a database or connect to one
conn = sqlite3.connect("Address_Book.db")

# Create cursor 
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE Addresses (
          first_name text,
          last_name text,
          address text,
          city text,
          state text,
          zipcode integer,
          )""")
'''
# Create text boxes
first_name = Entry(root,width=30)
first_name.grid(row=0,column=1,padx=20,pady=(10,0))

last_name = Entry(root,width=30)
last_name.grid(row=1,column=1)

address = Entry(root,width=30)
address.grid(row=2,column=1)

city = Entry(root,width=30)
city.grid(row=3,column=1)

state = Entry(root,width=30)
state.grid(row=4,column=1)

zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1)

# Creating submit function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('Address_Book.db')
    # Create cursor
    c = conn.cursor()

    # Insert Into the Table
    c.execute("INSERT INTO addresses VALUES (:first_name,:last_name,:address,:city,:state,:zipcode)",
              {
                  'first_name':first_name.get(),
                  'last_name':last_name.get(),
                  'address':address.get(),
                  'city':city.get(),
                  'state':state.get(),
                  'zipcode':zipcode.get()
              }  
              )
    # Clear the text boxes
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

# Creating query function for the database
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('Address_Book.db')
    # Create cursor
    c = conn.cursor()
    # To query the database
    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0]) +'\n'
    
    query_label = Label(root,text=print_records)
    query_label.grid(row=8,column=0,columnspan=2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

# Create Query Button
query_btn = Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)
# Create Text Boxes Labels
f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0,column=0)
last_name_label = Label(root,text="Last Name")
last_name_label.grid(row=1,column=0)
Address_label = Label(root,text="Address")
Address_label.grid(row=2,column=0)
City_label = Label(root,text="City")
City_label.grid(row=3,column=0)
State_label = Label(root,text="State")
State_label.grid(row=4,column=0)
zipcode_label = Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0)

# Submit button
submit_btn = Button(root,text="Add record to Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()