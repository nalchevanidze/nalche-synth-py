from sets import Set;

class AudioSystem:
    def __init__(self):

        self.frequency = 441;
        self.live = True;
        self.notes = Set();

    def stop(self):
        self.live = False;

    def setNote(self,note):
        note = int(note);
        if(note not in self.notes):
            self.notes.add(note);
            self.setN(note);
        
    def unsetNote(self,note):
        if(note in self.notes):
            self.notes.remove(note);
            self.unsetN(note);
        
    def up(self,level):
        print(level);
        self.frequency = floor(level * 440/100);