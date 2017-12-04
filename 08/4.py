from tkinter import Frame, Button, LEFT, StringVar, Label, TOP, BOTTOM
class UpDownCounter(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("UpDownCounter")

        frame = Frame(self)
        frame.pack(side=BOTTOM)
        Button(frame, text="UP", command=self.up, font=("Times", 16)).pack(side=LEFT)
        Button(frame, text="Down", command=self.down, font=("Times", 16)).pack(side=LEFT)
        Button(frame, text="Quit", command=self.dismiss, font=("Helvetica", 10)).pack(side=BOTTOM)
        self.result = StringVar()
        Label(self, textvariable=self.result, font=("Times", 18), width=10).pack(side=TOP)
        self.default()
    def default(self):
        self.a = 0
        self.result.set(self.a)
    def up(self):
        self.a += 1
        self.result.set(self.a)
    def down(self):
        if self.a > 0:
            self.a -= 1
            self.result.set(self.a)
    def dismiss(self):
        self.master.destroy()
UpDownCounter().mainloop()
