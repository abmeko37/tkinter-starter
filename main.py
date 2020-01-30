# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
from tkinter.ttk import *
from tkinter import Menu
from tkinter.ttk import Progressbar
from tkinter import ttk
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
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='yellow')
bar = Progressbar(window, length=100, style='black.Horizontal.TProgressbar')
bar.grid(column=0, row=0)
spin = Spinbox(window, from_=-100, to=100, width=10)
spin.grid(column=3,row=0)
progress = Progressbar(window, orient = HORIZONTAL, 
              length = 100, mode = 'determinate') 
def bar(): 
    import time 
    progress['value'] = 20
    window.update_idletasks() 
    time.sleep(1) 

    progress['value'] = 30
    window.update_idletasks() 
    time.sleep(1) 
    progress['value'] = 60
    window.update_idletasks() 
    time.sleep(1) 
    progress['value'] = 80
    window.update_idletasks() 
    time.sleep(1) 
    progress['value'] = 100

progress.pack(pady=10)
Button(window, text="Click Me" command=bar).pack(pady=10)
window.mainloop()     # Keep the window open
