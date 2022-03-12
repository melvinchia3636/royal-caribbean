from tkinter import *
from tkinter.font import Font
class quantum_class():
    def __init__(self):
        self.quantumclass = ['QUANTUM OF THE SEAS', 'ANTHEM OF THE SEAS', 'OVATION OF THE SEAS']
        self.ultraquantumclass = ['SPECTURM OF THE SEAS', 'ODYSSEY OF THE SEAS']
        self.btnframe = [Frame(root, bg='black') for i in range(9)]
        self.btn = [Button(root, text=i, borderwidth=0, font=Font(size=20, family='Bahnschrift SemiLight'), bg='white', activebackground='black', activeforeground='white') for i in self.quantumclass]
        [self.btn.append(Button(root, text=i, borderwidth=0, font=Font(size=20, family='Bahnschrift SemiLight'), bg='white', activebackground='black', activeforeground='white'))  for i in self.ultraquantumclass]
        self.quantum_title = Label(root, text='Quantum Class', font=Font(size=25, family='Bahnschrift SemiBold'), bg='white')
        self.u_quantum_title = Label(root, text='Ultra Quantum Class', font=Font(size=25, family='Bahnschrift SemiBold'), bg='white')
        self.backbtn = Button(root, text='BACK', font=Font(size=20, family='Bahnschrift SemiLight'), bg='white', borderwidth=0, activebackground='white', activeforeground='black')
        self.y, self.y2 = 370, 720
    def back_to_menu(self):
        [i.place_forget() for i in self.btnframe]
        [i.place_forget() for i in self.btn]
        self.backbtn.place_forget()
        self.quantum_title.place_forget()
        self.u_quantum_title.place_forget()
        menu.widget()
    def widget(self):
        root.title('Royal Caribbean Ship Archive | Quantum Class')
        menu.clear('QUANTUM CLASS')
        def btn_enter(e):
            if e.widget in self.btn:
                e.widget.config(bg='black', fg='white')
            if e.widget == self.backbtn:
                self.btnframe[8].place(x=400, y=940, anchor='center', height=50, width=150)
        def btn_leave(e):
            if e.widget in self.btn:
                e.widget.config(bg='white', fg='black')
            if e.widget == self.backbtn:
                self.btnframe[8].place_forget()
        root.bind('<Enter>', btn_enter)
        root.bind('<Leave>', btn_leave)
        self.quantum_title.place(x=400, y=300, anchor='center')
        self.u_quantum_title.place(x=400, y=650, anchor='center')
        for i in range(len(self.quantumclass)):
            self.btnframe[i].place(x=400, y=self.y, anchor='center', width=320, height=58)
            self.btn[i].place(x=400, y=self.y, anchor='center', width=316)
            self.y+=90 
        for i in range(3, len(self.ultraquantumclass)+3):
            self.btnframe[i].place(x=400, y=self.y2, anchor='center', width=320, height=58)
            self.btn[i].place(x=400, y=self.y2, anchor='center', width=316)
            self.y2+=90
        self.backbtn.place(x=400, y=940, anchor='center', height=46, width=146)
        self.backbtn.config(command=self.back_to_menu)

class oasis_class():
    def __init__(self):
        self.oasisclass = ['OASIS OF THE SEAS', 'ALLURE OF THE SEAS', 'HARMONY OF THE SEAS', 'SYMPHONY OF THE SEAS']
        self.btnframe = [Frame(root, bg='black') for i in range(5)]
        self.btn = [Button(root, text=i, borderwidth=0, font=Font(size=20, family='Bahnschrift SemiLight'), bg='white', activebackground='black', activeforeground='white') for i in self.oasisclass]
        self.backbtn = Button(root, text='BACK', font=Font(size=20, family='Bahnschrift SemiLight'), bg='white', borderwidth=0, activebackground='white', activeforeground='black')
        self.y = 370
    def back_to_menu(self):
        [i.place_forget() for i in self.btnframe]
        [i.place_forget() for i in self.btn]
        self.backbtn.place_forget()
        menu.widget()
    def widget(self):
        root.title('Royal Caribbean Ship Archive | Oasis Class')
        menu.clear('OASIS CLASS')
        def btn_enter(e):
            if e.widget in self.btn:
                e.widget.config(bg='black', fg='white')
            if e.widget == self.backbtn:
                self.btnframe[4].place(x=400, y=940, anchor='center', height=50, width=150)
        def btn_leave(e):
            if e.widget in self.btn:
                e.widget.config(bg='white', fg='black')
            if e.widget == self.backbtn:
                self.btnframe[4].place_forget()
        root.bind('<Enter>', btn_enter)
        root.bind('<Leave>', btn_leave)
        for i in range(len(self.oasisclass)):
            self.btnframe[i].place(x=400, y=self.y, anchor='center', width=320, height=58)
            self.btn[i].place(x=400, y=self.y, anchor='center', width=316)
            self.y+=90 
        self.backbtn.place(x=400, y=940, anchor='center', height=46, width=146)
        self.backbtn.config(command=self.back_to_menu)

class main_menu():
    global title
    def __init__(self):
        self.quantumclass = quantum_class()
        self.oasisclass = oasis_class()
        root.title('Royal Caribbean Ship Archive')
        self.main_logo = PhotoImage(file='main logo.png').subsample(4, 4)
        self.btnframe = [Frame(root, bg='black') for i in range(8)]
        self.classname = ['QUANTUM CLASS', 'OASIS CLASS', 'FREEDOM CLASS', 'VOYAGER CLASS', 'RADIANCE CLASS', 'VISION CLASS', 'SOVEREIGN CLASS', 'EMPRESS CLASS']
        self.btn = [Button(root, text=i, borderwidth=0, font=Font(size=20, family='Bahnschrift SemiLight'), bg='white', activebackground='black', activeforeground='white') for i in self.classname]
        self.logolabel = Label(root, image=self.main_logo, bg='white')
        self.y=320
        self.logolabel.place(x=400, y=100, anchor='center')
    def clear(self, titlechange):
        title.config(text=titlechange)
        [self.btn[i].place_forget() for i in range(len(self.btn))]
        [self.btnframe[i].place_forget() for i in range(len(self.btn))]
    def widget(self):
        self.__init__()
        self.btn[0].config(command=self.quantumclass.widget)
        self.btn[1].config(command=self.oasisclass.widget)
        self.clear('ROYAL CARIBBEAN CRUISE SHIP ARCHIVE')
        def btn_enter(e):
            if e.widget in self.btn:
                e.widget.config(bg='black', fg='white')
        def btn_leave(e):
            if e.widget in self.btn:
                e.widget.config(bg='white', fg='black')
        for i in range(len(self.btn)):
            self.btn[i].place(x=400, y=self.y, anchor='center', width=296)
            self.btnframe[i].place(x=400, y=self.y, anchor='center', width=300, height=58)
            self.y+=90
        root.bind('<Enter>', btn_enter)
        root.bind('<Leave>', btn_leave)

root = Tk()
root.geometry('800x1000+560+20')
root.config(bg='white')
root.iconbitmap('icon.ico')
title = Label(root, text='ROYAL CARIBBEAN SHIP ARCHIVE', font=Font(size=30, family='Bahnschrift Bold'), bg='white')
title.place(x=400, y=200, anchor='center')
menu = main_menu()
menu.widget()
root.mainloop()
