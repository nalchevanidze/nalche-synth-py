class AudioSystem:
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