from math import sin, cos , pi , radians , atan2 ,floor
from Tkinter import Canvas;

def eventToDegre (event):
    #print (event.x, event.y);
    a = atan2(  event.y - 100 , event.x - 100);
    l = a;
    if( a < 0 ): l = 6 + a;
    return l/6.00;

class RangeButton (Canvas):
    def __init__(self,master, callBack, level , steps = 12):
        Canvas.__init__(self,master,width=200, height=200)
        self.configure(
            background = "#444",
            borderwidth = 0
        )
        self.steps = steps;
        self.callBack = callBack;
        self.isMoving = False;
        self.bind('<Motion>',self.motion);
        self.bind("<Button>",self.startMoving);
        self.bind("<ButtonRelease>",self.endMoving);
        self.startPosition = 0;
        self.endLevel = 0;
        self.level = level;
        self.drawLines(level);

    def startMoving(self,event):
        print(event);
        self.startPosition = eventToDegre(event);
        self.isMoving = True;
        self.startLevel = 0;
        self.endLevel = 0;
    def endMoving(self,event):
        print(event);
        self.isMoving = False;   
    def motion(self, event):
        if(self.isMoving):
            self.degree(event);
    def degree(self,event):
        l = eventToDegre(event) - self.startPosition;
        self.changeLavel(l);

    def changeLavel(self, level ):
        if( level < 100):
            self.level = level;
        self.delete("all");
        self.drawLines(100 * self.level);
        self.callBack(100 * level);

    def drawLines( self, level ):
        center = 100;
        radius1 = 80;
        radius2 = 100;
        steps = self.steps;
        stepSize= 360.0/steps;
        r = 10;
        self.create_arc( 
            0+r, 
            0+r, 
            200 - r, 
            200 - r, 
            extent= -level * 3.5999 , 
            start=0 ,
            style = "arc",
            width = 5,
            outline = "red"
        );
        for i in range(0, steps):
            grad = radians(i * stepSize)                                                                                                    
            sinGrad = sin(grad)
            cosGrad = cos(grad)
            self.create_line( 
                center+sinGrad*radius1 , 
                center+cosGrad*radius1,
                center+sinGrad*radius2 , 
                center+cosGrad*radius2,
                fill="red",
                width=1
            )