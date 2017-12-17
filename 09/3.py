from tkinter import Frame, Button, StringVar, LEFT, BOTTOM, Label
import random
class JApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("じゃんけん")
        frame = Frame(self)
        frameb = Frame(self)
        frameb.pack()
        frame.pack(side=BOTTOM)
        for i in range(3):
            button = JButton(frame, i, self.notify)
            button.pack(side=LEFT)
        Button(self, text="Quit", command=self.quit).pack(side=BOTTOM)
        self.disp = StringVar()
        Label(frameb, textvariable=self.disp, font=("Sans-Serif", 25)).pack()

    def notify(self, id):
        if id =="d":
            self.disp.set("あいこ")
        elif id =="w":
            self.disp.set("勝ち")
        else:
            self.disp.set("負け")


class JButton(Button):
    def __init__(self, master, status, notify):
        self.text = StringVar()
        super().__init__(master, textvariable=self.text, font=("Sans-Serif", 20), command=self.judge)
        self.status = status
        if self.status == 0:
            self.hand = "✊"
        elif self.status == 1:
            self.hand = "✌️"
        else:
            self.hand = "✋"
        self.show()
        self.notify = notify
    def show(self):
        self.text.set(self.hand)
    def judge(self):
        rnm = int(random.randrange(3))
        if self.status == rnm:
            self.draw()
        elif self.status - rnm == -1 or self.status - rnm == 2:
            self.win()
        else:
            self.loose()
    def draw(self):
        self.notify("d")
    def win(self):
        self.notify("w")
    def loose(self):
        self.notify("l")
JApp().mainloop()