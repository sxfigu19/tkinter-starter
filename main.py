# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window
window.title("Welcome to Class!")

# Add a label with the text "Hello"
lbl = Label(window, text="Hello", font=("Courier",50))
lbl.grid(column=0, row=0)
txt = Label(window, text="Hope you're ready to begin", font=("Courier",20))
txt.grid(column=0, row=10)


box = Label(window, text="Start")
box.grid(column=0, row=20)
def clicked():
    box.configure(text="Button was clicked!!")
btn = Button(window, text="Click Me!", command=clicked)
btn.grid(column=0, row=30)
btn = Button(window, text="Click Me!", command=clicked)
btn.grid(column=0, row=40)

from tkinter import*
from tkinter import Menu
window.title("Welcome to the Menu")
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
window.mainloop()

from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
window = Tk()
window.title("Your Progress")
window.geometry('350x200')
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 70
bar.grid(column=0, row=0)
window.mainloop()
