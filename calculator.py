import tkinter as tk

class calc:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('600x600')
        self.equation = ''
        self.window.resizable(False,False)

        self.var = tk.StringVar()
        self.display = tk.Label(self.window,textvariable=self.var,font=('Arial',25))
        self.display.pack(pady=20)



        self.frame = tk.Frame(self.window)
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1,weight=1)
        self.frame.columnconfigure(2,weight=1)
        self.frame.columnconfigure(3,weight=1)
        self.frame.place(x=1,y=100)

        self.btn1 = tk.Button(self.frame,text='1',width=27,height=4,command=self.val1)
        self.btn1.grid(row=0,column=0,sticky=tk.W+tk.E)

        self.btn2 = tk.Button(self.frame,text='2',width=27,height=4,command=self.val2)
        self.btn2.grid(row=0,column=1,sticky=tk.W+tk.E)

        self.btn3 = tk.Button(self.frame,text='3',width=27,height=4,command=self.val3)
        self.btn3.grid(row=0,column=2,sticky=tk.W+tk.E)

        self.btn4 = tk.Button(self.frame,text='4',width=27,height=4,command=self.val4)
        self.btn4.grid(row=1,column=0,sticky=tk.W+tk.E)

        self.btn5 = tk.Button(self.frame,text='5',width=27,height=4,command=self.val5)
        self.btn5.grid(row=1,column=1,sticky=tk.W+tk.E)

        self.btn6 = tk.Button(self.frame,text='6',width=27,height=4,command=self.val6)
        self.btn6.grid(row=1,column=2,sticky=tk.W+tk.E)

        self.btn7 = tk.Button(self.frame,text='7',width=27,height=4,command=self.val7)
        self.btn7.grid(row=2,column=0,sticky=tk.W+tk.E)

        self.btn8 = tk.Button(self.frame,text='8',width=27,height=4,command=self.val8)
        self.btn8.grid(row=2,column=1,sticky=tk.W+tk.E)

        self.btn9 = tk.Button(self.frame,text='9',width=27,height=4,command=self.val9)
        self.btn9.grid(row=2,column=2,sticky=tk.W+tk.E)

        self.btn0 = tk.Button(self.frame,text='0',width=27,height=4,command=self.val0)
        self.btn0.grid(row=3,column=1,sticky=tk.W+tk.E)

        self.btnp = tk.Button(self.frame,text='+',width=27,height=4,command=self.valp)
        self.btnp.grid(row=4,column=0,sticky=tk.W+tk.E)

        self.btns = tk.Button(self.frame,text='-',width=27,height=4,command=self.vals)
        self.btns.grid(row=4,column=2,sticky=tk.W+tk.E)

        self.btnm = tk.Button(self.frame,text='x',width=27,height=4,command=self.valm)
        self.btnm.grid(row=3,column=2,sticky=tk.W+tk.E)

        self.btnd = tk.Button(self.frame,text='÷',width=27,height=4,command=self.vald)
        self.btnd.grid(row=3,column=0,sticky=tk.W+tk.E)

        self.btne = tk.Button(self.window,text='=',width=83,height=4,command=self.vale)
        self.btne.place(x=5,y=455)

        self.btnce = tk.Button(self.frame,text='CE',width=27,height=4,command=self.valce)
        self.btnce.grid(row=4,column=1,sticky=tk.W+tk.E)



        self.window.mainloop()

    def val1(self):
        self.equation += '1'
        self.var.set(self.equation)

    def val2(self):
        self.equation += '2'
        self.var.set(self.equation)
    
    def val3(self):
        self.equation += '3'
        self.var.set(self.equation)

    def val4(self):
        self.equation += '4'
        self.var.set(self.equation)

    def val5(self):
        self.equation += '5'
        self.var.set(self.equation)

    def val6(self):
        self.equation += '6'
        self.var.set(self.equation)

    def val7(self):
        self.equation += '7'
        self.var.set(self.equation)

    def val8(self):
        self.equation += '8'
        self.var.set(self.equation)

    def val9(self):
        self.equation += '9'
        self.var.set(self.equation)

    def val0(self):
        self.equation += '0'
        self.var.set(self.equation)

    def valp(self):
        self.equation += '+'
        self.var.set(self.equation)

    def vals(self):
        self.equation += '-'
        self.var.set(self.equation)

    def valm(self):
        self.equation += '*'
        self.var.set(self.equation)

    def vald(self):
        self.equation += '/'
        self.var.set(self.equation)

    def vale(self):
        self.equation = eval(self.equation)
        self.var.set(self.equation)
        self.equation = str(self.equation)
    
    def valce(self):
        self.equation = ''
        self.var.set(self.equation)

calc()