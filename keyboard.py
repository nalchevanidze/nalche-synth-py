from math import sin, cos , pi , radians , atan2 ,floor
from Tkinter import Canvas;

def positionToNoteIndex (event):
    #print (event.x, event.y);
    a = event.x;
    return a;

def keyEventToIndex(event):
    return ord(event.char) - 96;


class Keyboard (Canvas):
    def __init__(self,master, audioSystem ):
        self.keyWidth = 20;
        self.keyHeigth =100;
        self.keyCount = 36;
        self.tools = audioSystem;

        Canvas.__init__(
            self,
            master,
            width=self.keyWidth*self.keyCount, 
            height=self.keyHeigth
        )

        self.configure(
            background = "#EEE",
            borderwidth = 0
        )
        
        self.state = -1;
        self.bind("<Button>",self.onMouseDown);
        self.bind("<ButtonRelease>",self.onMouseUp);
        master.bind_all("<KeyPress>", self.KeyPress);
        master.bind_all("<KeyRelease>", self.KeyRelease);
        self.drawScene();
    
    def KeyPress(self,event):
        note = keyEventToIndex(event);
        self.tools.setNote(note);
        self.updateState();
    
    def KeyRelease(self,event):
        note = keyEventToIndex(event);
        self.tools.unsetNote(note);
        self.updateState();

    def noteFromEvent(self,event):
        return int(positionToNoteIndex(event) / self.keyWidth);

    def onMouseDown(self,event):
        self.tools.setNote(self.noteFromEvent(event));
        self.updateState();

    def onMouseUp(self,event):
        self.tools.unsetNote(self.noteFromEvent(event));
        self.updateState();

    def updateState(self):
        self.drawScene();
        
    def drawScene( self ):
        self.delete("all");
        for i in range(0, self.keyCount):
            startX = i*self.keyWidth;
            heigth = self.keyHeigth;

            if(i in self.tools.notes):
                heigth -= 10;

            color = "white";
            noteID = i%12;

            if(
                noteID == 1 or noteID == 3 
                or noteID == 6 or noteID == 8
                or noteID == 10 
            ):
                color = "black";
        
            self.create_rectangle(
                startX,
                0, 
                startX+self.keyWidth,
                heigth,
                fill=color,
            );