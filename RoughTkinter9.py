from tkinter import *

root = Tk()
root.title("Learn to Code at Codemy.com")

# r = StringVar()
# r.set("Pepperoni")

MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]
pizza = StringVar()
pizza.set("Pepperoni")
for text,mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W) 
       
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()  
# Radiobutton(root, text="Option 1", variable=r, value=1).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2).pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()
root.mainloop()