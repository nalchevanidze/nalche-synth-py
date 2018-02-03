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
        self.func = lambda (level): cont.up(level);
        self.canvas = RangeButton(frame,self.add_more,60);
        self.canvas.pack(
            side=LEFT
        );
        self.level = 10;
        self.canvas.drawLines(self.level);

        self.button = Button(
            frame, 
            text="QUIT", 
            fg="red",
            command= self.end
        )
        self.button.pack(side=LEFT);

        master.mainloop();

    def end(self):
        self.cont.stop() 
        self.frame.quit()
        self.root.destroy()
     
    def add_more(self, level ):
        if( level < 100):
            self.level = level;
        self.canvas.delete("all");
        self.canvas.drawLines(self.level);
        self.func(level);



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