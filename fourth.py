from tkinter import *

root = Tk()

label_name = Label(root, text='Your name')
label_pass = Label(root, text='Password')
entry_name = Entry(root)
entry_pass = Entry(root)

# a new way to organize stuff - Grid Layout. No need to exclusively specify column
# sticky = align-left/refttop/bottom. E stands for East, W for West, N and S for north and south
label_name.grid(row=0, column=0, sticky=E)
label_pass.grid(row=1, column=0, sticky=E)
entry_name.grid(row=0, column=1)
entry_pass.grid(row=1, column=1)

checkbox = Checkbutton(root, text='keep me signed in')
# to take 2 columns (or cells) instead of just one
checkbox.grid(columnspan=2)

root.mainloop()
