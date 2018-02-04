from math import sin, cos , pi , radians , atan2 ,floor
from Tkinter import *
import audioProcessing
import multiprocessing
import thread;
from buttons import RangeButton;
from keyboard import Keyboard;
from synth_system import AudioSystem;

class AppScreen:
    def __init__(self,cont):
        master = Tk();
        frame = Frame(master);
        master.configure(background='#444');
        master.protocol("WM_DELETE_WINDOW", self.close );
        self.root = master;
        frame.pack();
        self.frame = frame;
        self.cont = cont;
        self.pitcher = RangeButton(frame,self.setPitch,10);
        self.pitcher.pack(side=TOP);
        self.keys = Keyboard(frame,cont);
        self.keys.pack(side=BOTTOM);
        master.mainloop();
    def close(self):
        self.cont.stop() 
        self.frame.quit()
        self.root.destroy()
        
    def setPitch(self, level ):
        self.cont.up(level);

audio_system = AudioSystem();

def audioLoop(cont,m):
    audio = audioProcessing.AudioProcessor();
    cont.setN = audio.setNote;
    cont.unsetN = audio.unsetNote;
    
    while(cont.live):
        audio.run(cont);

    print("end of sound")
    
      
def panelLoop(cont,m):
    app = AppScreen(cont);
    print("close");
    

try:
    thread.start_new_thread( audioLoop, (audio_system,0) );
    thread.start_new_thread( panelLoop , (audio_system,0) );
except:
   print("Error: unable to start thread")


while audio_system.live:
    pass;