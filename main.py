# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
from tkinter import Menu
window = Tk()         # Create the application window

# Add a label with the text "Hello"
lbl = Label(window, text="How is it going", font=("Arial Bold",50))
# Place the label in the window at 0, 0
lbl.grid(column=1, row=2)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=1, row=3)
btn = Button(window, text="Click Me")
btn.grid(column=0, row=2)
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
window.mainloop()     # Keep the window open
