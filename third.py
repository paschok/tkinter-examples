from tkinter import *

root = Tk()

# bg - background of a text, fg - color of text
one = Label(root, text='ONE', bg='red', fg='white')
one.pack()

two = Label(root, text='TWO', bg='green', fg='black')
# label two will be as big, as X value of a parent - it's gonna grow
two.pack(fill=X)

three = Label(root, text='THREE', bg='blue', fg='white')
# label two will be as big, as y value of a parent - it's gonna grow
three.pack(side=LEFT, fill=Y)

root.mainloop()
