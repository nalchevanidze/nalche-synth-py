from math import sin, cos , pi , radians , atan2 ,floor
from Tkinter import Canvas;

def positionToNoteIndex (event):
    print (event.x, event.y);
    a = event.x;
    return a;

class Keyboard (Canvas):
    def __init__(self,master, callBack):
        self.keyWidth = 20;
        self.keyHeigth =100;
        self.keyCount = 36;

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
        self.callBack = callBack;
        self.bind("<Button>",self.onMouseDown);
        self.bind("<ButtonRelease>",self.onMouseUp);
        self.drawScene();

    def onMouseDown(self,event):
        self.state = int(positionToNoteIndex(event) / self.keyWidth);
        self.updateState();

    def onMouseUp(self,event):
        self.state = -1;
        self.updateState();

    def updateState(self):
        self.callBack(self.state);
        self.drawScene();
        
    def drawScene( self ):
        self.delete("all");
        for i in range(0, self.keyCount):
            startX = i*self.keyWidth;
            heigth = self.keyHeigth;
            if(i == self.state):
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