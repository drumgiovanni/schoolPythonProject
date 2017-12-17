from tkinter import Frame, Label, Button, StringVar, BOTTOM, Entry, END, LEFT, TOP

class Cal(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("Calculator")
        self.ent1 = Entry(self, font=("Times", 20))
        self.ent1.pack()
        self.ent2 = Entry(self, font=("Times", 20))
        self.ent2.pack()
        frame1 = Frame(self)
        frame1.pack()
        frame2 = Frame(self)
        frame2.pack(side=BOTTOM)
        Button(frame1, text="set", command=self.setnum).pack(side=TOP)
        Button(frame1, text="×", command=self.kakeru).pack(side=LEFT)
        Button(frame1, text="÷", command=self.divide).pack(side=LEFT)
        Button(frame1, text="+", command=self.plus).pack(side=LEFT)
        Button(frame1, text="-", command=self.minus).pack(side=LEFT)
        self.disp = StringVar()
        Label(frame2, textvariable=self.disp, font=("Times", 20)).pack()


    def setnum(self):
        self.num1 = int(self.ent1.get())
        self.num2 = int(self.ent2.get())
        self.ent1.delete(0, END)
        self.ent2.delete(0, END)

    def kakeru(self):
        self.result = self.num1 * self.num2
        self.do = "×"
        self.displayresult()
    def divide(self):
        self.result = self.num1 / self.num2
        self.do = "÷"
        self.displayresult()
    def plus(self):
        self.result = self.num1 + self.num2
        self.do = "+"
        self.displayresult()
    def minus(self):
        self.result = self.num1 - self.num2
        self.do = "-"
        self.displayresult()
    def displayresult(self):
        text = f"{self.num1} {self.do} {self.num2} = {self.result}"
        self.disp.set(text)

Cal().mainloop()