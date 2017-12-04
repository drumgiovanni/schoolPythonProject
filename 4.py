from tkinter import Frame, Button, LEFT, RIGHT, StringVar, Label, TOP, BOTTOM


class UpDownCounter(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("UpDownCounter")
        Button(self, text="UP", command=self.up, font=("Times", 16)).pack(side=LEFT)
        Button(self, text="Down", command=self.down, font=("Times", 16)).pack(side=LEFT)
        Button(self, text="Quit", command=self.dismiss, font=("Helvetica", 10), bg="black", fg="red").pack(side=BOTTOM)

        self.meter = StringVar()
        Label(self, textvariable=self.result, font=("Times", 18), width=10).pack(side=TOP)
    def up(self):
