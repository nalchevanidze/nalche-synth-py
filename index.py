from math import sin, cos , pi , radians , atan2 ,floor
from Tkinter import *
import audioProcessing
import multiprocessing
import thread;
from buttons import RangeButton
from keyboard import Keyboard

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
        self.keys = Keyboard(frame,cont.setNote);
        self.keys.pack(side=BOTTOM);
        master.mainloop();

    def close(self):
        self.cont.stop() 
        self.frame.quit()
        self.root.destroy()
        
    def setPitch(self, level ):
        self.cont.up(level);

class Controller:
    def __init__(self):
        self.frequency = 441;
        self.live = True;
        self.notes = -1;
    def stop(self):
        self.live = False;
    def setNote(self,note):
        self.notes =  note;
        self.play(note);
    def up(self,level):
        print(level);
        self.frequency = floor(level * 440/100);

controller = Controller();

def audioLoop(cont,m):
    audio = audioProcessing.AudioProcessor();
    cont.play = audio.setNote;
    
    while(cont.live):
        audio.run(cont);

    print("end of sound")
    
      
def panel(cont,m):
    app = AppScreen(cont);
    print("close");
    

try:
    thread.start_new_thread( audioLoop, (controller,0) );
    thread.start_new_thread( panel , (controller,0) );
except:
   print("Error: unable to start thread")


while controller.live:
    pass;