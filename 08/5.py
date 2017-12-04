from tkinter import Frame, Label, StringVar, Button, LEFT, BOTTOM, TOP
import random
class LuckChallenger(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("LuckChallenger")

        frame = Frame(self)
        frame.pack(side=BOTTOM)
        Button(frame, text="A", command=self.choose).pack(side=LEFT)
        Button(frame, text="B", command=self.choose).pack(side=LEFT)
        Button(frame, text="RESET", command=self.reset).pack(side=BOTTOM)
        Button(frame, text="QUIT", command=self.dismiss).pack(side=LEFT)
        self.disp = StringVar()
        Label(self, textvariable=self.disp, font=("Sans-serif", 48)).pack(side=TOP)
    def choose(self):
        rnd = random.randrange(4)
        if rnd == 1:
            self.disp.set("あたり")
        else:
            self.disp.set("はずれ")
    def reset(self):
        self.disp.set("")
    def dismiss(self):
        self.master.destroy()
LuckChallenger().mainloop()