from math import sin, cos , pi , radians , atan2 ,floor
from Tkinter import *
import audioProcessing
import multiprocessing
import thread;
from buttons import RangeButton

class AppScreen:
    def __init__(self,cont):
        master = Tk();
        frame = Frame(master);
        master.configure(background='#444');
        self.root = master;
        frame.pack();
        self.frame = frame;
        self.cont = cont;
        self.canvas = RangeButton(frame,self.setPitch,10);
        self.canvas.pack(
            side=LEFT
        );
        self.level = 10;
        self.button = Button(
            frame, 
            text="QUIT", 
            fg="red",
            command= self.close
        )
        self.button.pack(side=LEFT);
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
    def stop(self):
        self.live = False;
    def up(self,level):
        print(level);
        self.frequency = floor(level * 440/100);

controller = Controller();


def audioLoop(cont,m):
    audio = audioProcessing.AudioProcessor();
    while(cont.live):
        audio.tone(cont.frequency);
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