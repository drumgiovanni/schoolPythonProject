from tkinter import Frame, Button, StringVar, LEFT, BOTTOM, Label
import time
class Timer(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("キッチンタイマー")
        self.timedisp = StringVar()
        Label(self, textvariable=self.timedisp, font=("Times", 40)).pack()
        frame = Frame(self)
        frame.pack()
        frameb = Frame(self)
        frameb.pack(side=BOTTOM)
        Button(frame, text="Start", command=self.start).pack(side=LEFT)
        Button(frameb, text="Reset", command=self.reset).pack(side=LEFT)
        Button(frameb, text="Quit", command=self.quit).pack(side=LEFT)
        Button(frame, text="Stop", command=self.stop).pack(side=LEFT)
        self.timedisp.set(10)
        self.cdtime = 10
        self.sign = "go"
    def start(self):
        if self.cdtime > 0 and self.sign == "go":
            self.cdtime -= 1
            self.timedisp.set(self.cdtime)
            self.after(1000, self.start)

    def reset(self):
        self.timedisp.set(10)
        self.cdtime = 10
    def stop(self):
        self.sign = "stop"
        self.after(1000, self.go)
    def go(self):
        self.sign = "go"
Timer().mainloop()