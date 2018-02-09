from math import sin, cos, pi, radians, atan2
from tkinter import Canvas


def percent_from_degree(angle):
    degree = 180 * angle / pi
    if degree < 0:
        degree = 180 + degree
    else:
        degree += 180
    return degree

class RangeButton(Canvas):

    def __init__(self, master, callback, level, steps=12):
        size = 200
        Canvas.__init__(self, master, width=size, height=size)
        self.configure(
            background="#444",
            borderwidth=0
        )
        self.steps = steps
        self.callBack = callback
        self.isMoving = False
        self.bind('<Motion>', self.motion)
        self.bind("<Button>", self.startMoving)
        self.bind("<ButtonRelease>", self.endMoving)
        self.startPosition = 0
        self.startLevel = 0
        self.endLevel = 0
        self.level = level
        self.drawLines(level)
        self.center = size/2

    def event_to_degre(self, event):
        radian = atan2(self.center - event.y, self.center - event.x)
        degree = percent_from_degree(radian)
        return degree

    def startMoving(self, event):
        self.startPosition = self.event_to_degre(event)
        self.isMoving = True

    def degree(self, event):
        return max(0, min(self.event_to_degre(event) - self.startPosition + self.level, 360))

    def endMoving(self, event):
        self.isMoving = False
        self.level = self.degree(event)
        self.startPosition = 0
        self.delete("all")
        self.drawLines(self.level)

    def motion(self, event):
        if self.isMoving:
            self.changeLevel(event)

    def changeLevel(self, event):
        degree = self.degree(event)
        self.delete("all")
        self.drawLines(degree)
        self.callBack(degree/360)

    def drawLines(self, degree):
        center = 100
        radius1 = 80
        radius2 = 100
        steps = self.steps
        step_size = 360.0 / steps
        r = 10
        self.create_arc(
            0 + r,
            0 + r,
            200 - r,
            200 - r,
            extent=1-degree,
            start=0,
            style="arc",
            width=5,
            outline="red"
        )
        for i in range(0, steps):
            grad = radians(i * step_size)
            sin_grad = sin(grad)
            cos_grad = cos(grad)
            self.create_line(
                center + sin_grad * radius1,
                center + cos_grad * radius1,
                center + sin_grad * radius2,
                center + cos_grad * radius2,
                fill="red",
                width=1
            )
