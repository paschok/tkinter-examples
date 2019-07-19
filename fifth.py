from tkinter import *

root = Tk()


def printName():
    print('hello, my name is Paul!')


# command means - whenever I click this run a certain function
button1 = Button(root, text='Know my name the first method', command=printName)
button1.pack()


def printName2(event):
    """
        another way of binding command to a function
    :return:None
    """
    print('heeeeello, my name is Paul!')


button2 = Button(root, text='Know my name the second method')
# bind(): what event r we waiting for and whar function must be run
# <Button-1> : means left button
button2.bind('<Button-1>', printName2)
button2.pack()

root.mainloop()
