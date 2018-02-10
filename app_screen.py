from buttons import RangeButton
from keyboard import Keyboard
from tkinter import Tk, Frame, TOP, BOTTOM

class AppScreen:

    def __init__(self, cont):
        master = Tk()
        frame = Frame(master)
        master.configure(background='#444')
        master.protocol("WM_DELETE_WINDOW", self.close)
        self.root = master
        frame.pack()
        self.frame = frame
        self.cont = cont
        self.pitcher = RangeButton(frame, self.setPitch, 10)
        self.pitcher.pack(side=TOP)
        self.keys = Keyboard(frame, cont)
        self.keys.pack(side=BOTTOM)

    def close(self):
        self.cont.stop()
        self.frame.quit()
        self.root.destroy()

    def setPitch(self, level):
        self.cont.up(level)

    def start(self):
        self.root.mainloop()