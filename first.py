from tkinter import *

# creating a class ==> a blank window. root is MAIN window
root = Tk()

# creating a simple text and putting it in a window-root with 'text'
label = Label(root, text='This is too easy')

# this line of code means - just pack whatever u see and pack
# displaying our label in window
label.pack()

"""
    Mainloop puts window in a loop that never ends and whereas our window will continuously display.
    Or else our PC will show the window in thousand of milliseconds
"""
root.mainloop()