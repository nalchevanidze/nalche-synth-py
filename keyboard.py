from tkinter import Canvas

keymap = (
    "y",
    "s",
    "x",
    "d",
    "c",
    "v",
    "g",
    "b",
    "h",
    "n",
    "j",
    "m",
    "q",
    "2",
    "w",
    "3",
    "e",
    "r",
    "5",
    "t",
    "6",
    "z",
    "7",
    "u"
)


def  key_to_note(event):
    return keymap.index(event.char)

def positionToNoteIndex (event):
    #print (event.x, event.y);
    a = event.x
    return a

def keyEventToIndex(event):
    return ord(event.char) - 96


class Keyboard (Canvas):

    def __init__(self, master, audio_system):
        self.keyWidth = 20
        self.keyHeigth =100
        self.keyCount = 36
        self.tools = audio_system

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
        
        self.bind("<Button>",self.onMouseDown)
        self.bind("<ButtonRelease>",self.onMouseUp)
        master.bind_all("<KeyPress>", self.KeyPress)
        master.bind_all("<KeyRelease>", self.KeyRelease)
        self.drawScene()

    def KeyPress(self,event):
        if event.char in keymap:
            note = key_to_note(event)
            self.tools.setNote(note)
            self.updateState()
    
    def KeyRelease(self,event):
        if event.char in keymap:
            note = key_to_note(event)
            self.tools.unsetNote(note)
            self.updateState()

    def noteFromEvent(self,event):
        return int(positionToNoteIndex(event) / self.keyWidth)

    def onMouseDown(self,event):
        self.tools.setNote(self.noteFromEvent(event))
        self.updateState()

    def onMouseUp(self,event):
        self.tools.unsetNote(self.noteFromEvent(event))
        self.updateState()

    def updateState(self):
        self.drawScene()

    def drawScene(self):
        self.delete("all")
        for i in range(0, self.keyCount):
            startX = i*self.keyWidth
            heigth = self.keyHeigth

            if(i in self.tools.notes):
                heigth -= 10

            color = "white"
            noteID = i % 12

            if(
                noteID == 1 or noteID == 3 
                or noteID == 6 or noteID == 8
                or noteID == 10 
            ):
                color = "black"
        
            self.create_rectangle(
                startX,
                0, 
                startX+self.keyWidth,
                heigth,
                fill=color,
            )
