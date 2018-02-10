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

black_keys = (1, 3, 6, 8, 10)


def key_to_note(event):
    return keymap.index(event.char)


def positionToNoteIndex (event):
    a = event.x
    return a


class Keyboard (Canvas):

    def __init__(self, master, audio_system):
        self.key_width = 20
        self.key_height = 100
        self.key_count = 36
        self.tools = audio_system


        Canvas.__init__(
            self,
            master,
            width=self.key_width * self.key_count,
            height=self.key_height
        )

        self.configure(
            background="#777",
            borderwidth=0
        )
        
        self.bind("<Button>",self.onMouseDown)
        self.bind("<ButtonRelease>",self.onMouseUp)
        master.bind_all("<KeyPress>", self.KeyPress)
        master.bind_all("<KeyRelease>", self.KeyRelease)
        self.drawScene()

    def KeyPress(self, event):
        if event.char in keymap:
            note = key_to_note(event)
            self.tools.setNote(note)
            self.updateState()
    
    def KeyRelease(self, event):
        if event.char in keymap:
            note = key_to_note(event)
            self.tools.unsetNote(note)
            self.updateState()

    def noteFromEvent(self,event):
        return int(positionToNoteIndex(event) / self.key_width)

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
        for i in range(0, self.key_count):
            start_x = i*self.key_width
            height = self.key_height

            if i in self.tools.notes:
                height -= 10

            color = "white"
            note_id = i % 12

            if note_id in black_keys:
                color = "black"
        
            self.create_rectangle(
                start_x,
                0, 
                start_x+self.key_width,
                height,
                fill=color,
            )
