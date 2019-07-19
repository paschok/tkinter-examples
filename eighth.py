from tkinter import *

def doNothing():
    print('do nothing')


root = Tk()

# ***** Main Menu ******
menu = Menu(root)
# saying that we r configuring the menu
root.config(menu=menu)

# creating a submenu that goes INSIDE the Menu
submenu = Menu(menu)
# dropdown functionality: submenu is our menu to be dropped down
menu.add_cascade(label='File', menu=submenu)
# command: what function to cal when we click
submenu.add_command(label='New Project ..', command=doNothing)
submenu.add_command(label='New..', command=doNothing)
# creates a line to separate one group from another
submenu.add_separator()
submenu.add_command(label='Exit', command=doNothing)

editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Undo..', command=doNothing)

# ***** Toolbar ******
toolbar = Frame(root, bg='blue')
insert_butt = Button(toolbar, text='Insert Image', command=doNothing)
# padx: 2px of padding
insert_butt.pack(side=LEFT, padx=2, pady=2)
print_butt = Button(toolbar, text='Print', command=doNothing)
print_butt.pack(side=LEFT, padx=3, pady=1)
toolbar.pack(side=TOP, fill=X)

# ***** Status Bar ******
# bd: border; relief=sunken: just a cool visual
status_bar = Label(root, text='Statusing', bd=1, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, fill=X)

root.mainloop()