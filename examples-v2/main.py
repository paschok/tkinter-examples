# i'll importing another module soon and names of these two will collide
# that's why we import 'kinter this way, and not like before
import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        # super searches for base class of class Root and returns it
        # then lunches init of this found class
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='red', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='tenor.gif')
        button_open_dialog = tk.Button(toolbar, text='Click my ass', command=self.open_dialog_window,
                                       bg='blue', bd=0, compound=tk.TOP, image=self.add_img)
        button_open_dialog.pack(side=tk.LEFT)

        self.tree =ttk.Treeview(self, columns=('ID', 'description', 'costs', 'total'), height=15,
                                show='headings')
        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('description', width=30, anchor=tk.CENTER)
        self.tree.column('costs', width=30, anchor=tk.CENTER)
        self.tree.column('total', width=30, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('description', text='description')
        self.tree.heading('costs', text='costs')
        self.tree.heading('total', text='total')

        self.tree.pack()

    def open_dialog_window(self):
        Child()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Title 2')
        # 400 and 300: coordinates
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_desc = ttk.Label(self, text='Your description')
        label_desc.place(x=50, y=50)
        label_select = ttk.Label(self, text='Your selection')
        label_select.place(x=50, y=80)
        label_sum = ttk.Label(self, text='Your sum')
        label_sum.place(x=50, y=110)

        self.entry_desc = ttk.Entry(self)
        self.entry_desc.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        self.combobox =ttk.Combobox(self, values=[u'In', u'Out'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        button_cancel = ttk.Button(self, text='Close', command=self.destroy)
        button_cancel.place(x=300, y=170)
        button_add = ttk.Button(self, text='Add')
        button_add.place(x=220, y=170)
        button_add.bind('<Button-1>')

        # firts u'll have to deal with dialog window and only then with the main
        self.grab_set()
        self.focus_set()


# if scripts runs as a main programm, then code will run.
# If script is imported - code will not run
if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Title')
    root.geometry('650x450+300+200')
    root.resizable(False, False) # window shouldn't change width/height
    root.mainloop()
