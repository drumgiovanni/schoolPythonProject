from tkinter import Frame, Label, LEFT
class GuiApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        Label(self, text="赤", fg="red", font=("Sans-serif", 36)).pack(side=LEFT)
        Label(self, text="黄", fg="yellow", font=("Sans-serif", 36)).pack(side=LEFT)
        Label(self, text="緑", fg="green", font=("Sans-serif", 36)).pack(side=LEFT)


GuiApp().mainloop()