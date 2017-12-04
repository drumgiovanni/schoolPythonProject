from tkinter import Frame, Label, Button, StringVar, BOTTOM, TOP
import random
class LotoButton(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("おみくじだよ〜〜")

        Button(self, text="占う", command=self.start, font=("Sans-serif", 20)).pack(side=TOP)
        self.result = StringVar()
        Label(self, textvariable=self.result, font=("Sans-serif", 54), width=10).pack(side=BOTTOM)

    def start(self):
        rnd = random.randrange(1, 101)
        if rnd >= 1 and rnd <= 5:
            self.result.set("大吉")
        elif rnd >= 6 and rnd <= 15:
            self.result.set("吉")
        elif rnd >= 16 and rnd <= 30:
            self.result.set("中吉")
        elif rnd >= 31 and rnd <= 60:
            self.result.set("小吉")
        elif rnd >= 61 and rnd <= 94:
            self.result.set("末吉")
        else:
            self.result.set("凶")
LotoButton().mainloop()

