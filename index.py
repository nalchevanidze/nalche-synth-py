from tkinter import *
from audioProcessing import AudioProcessor
from buttons import RangeButton
from keyboard import Keyboard
from synth_system import AudioSystem
from threading import Thread


class AppScreen:

    def __init__(self, cont):
        master = Tk()
        frame = Frame(master)
        master.configure(background='#444')
        master.protocol("WM_DELETE_WINDOW", self.close )
        self.root = master
        frame.pack()
        self.frame = frame
        self.cont = cont
        self.pitcher = RangeButton(frame,self.setPitch,10)
        self.pitcher.pack(side=TOP)
        self.keys = Keyboard(frame,cont)
        self.keys.pack(side=BOTTOM)
        master.mainloop()

    def close(self):
        self.cont.stop() 
        self.frame.quit()
        self.root.destroy()
        
    def setPitch(self, level ):
        self.cont.up(level)


audio_system = AudioSystem()


class AudioThread(Thread):

    def __init__(self, cont ):
        Thread.__init__(self)
        self.cont = cont

    def run(self):
        audio = AudioProcessor(self.cont)
        audio.start()


class GUIThread(Thread):

    def __init__(self, cont):
        Thread.__init__(self)
        self.cont = cont

    def run(self):
        AppScreen(self.cont)


audio_thread = AudioThread(audio_system)
gui_thread = GUIThread(audio_system)
audio_thread.start()
gui_thread.start()

audio_thread.join()
gui_thread.join()
