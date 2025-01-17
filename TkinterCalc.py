from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=4, padx=10,pady=10)

def button_undo():
    r = e.get()
    e.delete(0, END)
    str = r[:len(r)-1]
    e.insert(0, str)

def button_clear():
    e.delete(0,END)
def button_equal():
    second_num = e.get()
    e.delete(0,END)
    if (math=="addition"):
        e.insert(0,f_num+int(second_num))
    elif (math=="subtraction"):
        e.insert(0,f_num-int(second_num))
    elif (math=="divison" and second_num!=0):
        e.insert(0,f_num/int(second_num))
    elif (math=="multiplication"):
        e.insert(0,f_num*int(second_num))
    elif (math=="power"):
        e.insert(0, f_num**int(second_num))
    elif (math=="modulo"):
        e.insert(0, f_num%int(second_num))
def button_pow():
    first_number = e.get()
    global f_num
    global math
    math = "power"
    f_num = int(first_number)
    e.delete(0, END)
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)
def button_click(number):
    # e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)
def button_mod():
    first_number = e.get()
    global f_num
    global math
    math = "modulo"
    f_num = int(first_number)
    e.delete(0, END)
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divison"
    f_num = int(first_number)
    e.delete(0,END)


# Define buttons
Button_1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
Button_2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
Button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
Button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
Button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
Button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
Button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
Button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
Button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
Button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
Button_back = Button(root, text="del", padx=40, pady=20, command=lambda:button_undo())
Button_pow = Button(root, text="x^y", padx=40, pady=20, command=lambda: button_pow())
Button_add = Button(root, text="+",padx=39,pady=20,command=lambda: button_add())
Button_equal = Button(root,text="=",padx=89,pady=20,command=lambda: button_equal())
Button_clear = Button(root,text="Clear",padx=79,pady=20,command=lambda: button_clear())
Button_divide = Button(root,text="/",padx=41,pady=20,command= lambda: button_divide())
Button_subtract = Button(root,text="-",padx=40,pady=20,command= lambda: button_subtract())
Button_multiply = Button(root,text="*",padx=40,pady=20,command= lambda: button_multiply())
Button_mod = Button(root, text="%", padx=40, pady=20, command=lambda: button_mod())

# Put buttons on screen
Button_1.grid(row=3,column=0)
Button_2.grid(row=3,column=1)
Button_3.grid(row=3,column=2)

Button_4.grid(row=2,column=0)
Button_5.grid(row=2,column=1)
Button_6.grid(row=2,column=2)

Button_7.grid(row=1,column=0)
Button_8.grid(row=1,column=1)
Button_9.grid(row=1,column=2)

Button_0.grid(row=4,column=0)

Button_clear.grid(row=4,column=1,columnspan=2)
Button_add.grid(row=5,column=0)
Button_equal.grid(row=5,column=1,columnspan=2)
Button_subtract.grid(row=6,column=0)
Button_divide.grid(row=6,column=1)
Button_multiply.grid(row=6,column=2)
Button_back.grid(row=1, column=3)
Button_pow.grid(row=2, column=3)
Button_mod.grid(row=3, column=3)
root.mainloop()


