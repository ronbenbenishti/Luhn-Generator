#! /usr/bin/python

from Tkinter import *

chkbox = True
w = None
def init(top, gui):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def vp_start_gui():
    global val, w, root
    root = Tk()
    top = NumCheck (root)
    init(root, top)
    root.mainloop()

def UpdateCheck():
    global chkbox
    if chkbox == True:
        chkbox = False
    else:
        chkbox = True

class NumCheck:
    def __init__(self, top=None):

        top.geometry('175x220+650+150')
        top.title("Luhn Generator")
        top.bind('<Escape>', lambda x: quit())
        top.resizable(width=False, height=False)
        top.iconbitmap(default='luhn.ico')

        def Submit():
            global chkbox

            if chkbox == True:
                luhn = Check(Valid(self.Entry1.get()))
            else:
                luhn = Check(self.Entry1.get())
            self.Entry2.configure(state='normal')
            self.Entry2.delete(0, END)
            self.Entry2.insert(END, luhn)
            self.Entry2.configure(state='disabled')

        def Valid(id):
            while len(id) > 8:
                id = list(id)
                del id[-1]
                id = "".join(id)
                self.Entry1.delete(0, END)
                self.Entry1.insert(INSERT , id)

            while len(id) < 8:
                    id = "0" + id
                    self.Entry1.insert(-1,'0')
            return id

        def Check(x):
            c = 1
            IDstr = ""
            for i in x:
                try:
                    IDstr += str(int(i) * c)
                    if c == 1:
                        c += 1
                    else:
                        c = 1
                    self.Statusbar.configure(state='normal')
                    self.Statusbar.delete('1.0', END)
                    self.Statusbar.insert(INSERT, 'Running...')
                    self.Statusbar.configure(state='disabled')
                except:
                    self.Statusbar.configure(state='normal')
                    self.Statusbar.delete('1.0', END)
                    self.Statusbar.tag_configure('color-red', foreground='red')
                    self.Statusbar.insert(INSERT, "Error: Cannot Convert str to int", 'color-red')
                    self.Statusbar.configure(state='disabled')

            IDsum = 0
            for i in range(0, len(IDstr)):
                IDsum += int(IDstr[i])

            table = [10, 20, 30, 40, 50, 60, 70, 80, 90]
            for i in table:
                if IDsum < i:
                    checkdig = str(i - IDsum)
                    break
                else:
                    pass
            if len(checkdig) > 1:
                self.Statusbar.configure(state='normal')
                self.Statusbar.delete('1.0', END)
                self.Statusbar.tag_configure('color-red', foreground='red')
                self.Statusbar.insert(INSERT, "Error: Invalid number", 'color-red')
                self.Statusbar.configure(state='disabled')
                return checkdig
            else:
                return checkdig

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.06, rely=0.05, relheight=0.9, relwidth=0.89)

        self.Title = Label(self.Frame1)
        self.Title.place(relx=0.06, rely=0.01, height=31, width=134)
        self.Title.configure(text='Luhn Number Generator')

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.06, rely=0.23, height=21, width=104)
        self.Label1.configure(justify=LEFT)
        self.Label1.configure(text='Enter ID number:')

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.06, rely=0.4,height=30, relwidth=0.67)
        self.Entry1.configure(font='TkFixedFont')

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.77, rely=0.4,height=30, relwidth=0.15)
        self.Entry2.configure(font='TkFixedFont')
        self.Entry2.configure(state='disabled')

        self.Checkbutton1 = Checkbutton(self.Frame1)
        self.Checkbutton1.place(relx=0.06, rely=0.57, relheight=0.14, relwidth=0.78)
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='8 digits validation')
        self.Checkbutton1.configure(onvalue=True, offvalue=False, command= lambda: UpdateCheck())
        self.Checkbutton1.select()

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.06, rely=0.74, height=34, width=137)
        self.Button1.configure(text='Submit', command=lambda: Submit())

        self.Statusbar = Text(top)
        self.Statusbar.place(relx=0.04, rely= 0.91, relheight= 0.07, relwidth=0.91)
        self.Statusbar.configure(font=("TkFixedFont", 8), background='#f0f0f0', borderwidth='0')
        self.Statusbar.insert(INSERT, 'Running..')
        self.Statusbar.configure(state='disabled')

if __name__ == '__main__':
    vp_start_gui()



