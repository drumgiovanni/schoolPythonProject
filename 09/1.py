from tkinter import Frame, Label, Button, StringVar, TOP, Entry, END


class Timer(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("Countdown Timer")

        frame = Frame(self)
        frame.pack(side=TOP)

        self.ent = Entry(frame, font=("Times", 20))
        self.ent.pack()

        Button(frame, text="set", command=self.settime).pack(side=TOP)


        # 表示部分
        self.counterlabel = StringVar()
        Label(self, width=5,
            textvariable=self.counterlabel, font=("Helvetica", 36)).pack()
        # Startボタン
        Button(self, text="Start", command=self.start).pack()
    def settime(self):
        string = self.ent.get()
        self.timeleft = int(string)
        self.ent.delete(0, END)
    def start(self):
        self.counterlabel.set(self.timeleft)
        self.after(1000, self.countdown)

    def countdown(self):
        if self.timeleft > 0:
            self.timeleft -= 1
            self.counterlabel.set(self.timeleft)
            self.after(1000, self.countdown)

Timer().mainloop()