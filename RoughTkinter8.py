from tkinter import *

root = Tk()
root.title("Learn to Code at Codemy.com")
frame = LabelFrame(root, text="This is my Frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click here")
b2 = Button(frame, text="Exit Program", command=root.quit)
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()