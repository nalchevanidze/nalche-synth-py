import math
import pyaudio
import array
from wave_looper import WaveLooper
from audio_config import SAMPLE_RATE

LOOPSIZE = int(SAMPLE_RATE/100)

def sine(sounds):
    c = []
    for i in range(0, LOOPSIZE):
        value = 0

        for sound in sounds:
            value += math.sin(sound.next()) * 0.25

        c.append(value)

    return c

sound = WaveLooper();
soundList = [sound]
soundSet = set([])

soundList = [None] * 49

active = set([])
addInNextEvent = set([])
removeInNextEvent = set([])

class AudioProcessor:

    def __init__(self, cont):



        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=pyaudio.paFloat32,         
            channels=1, 
            rate=SAMPLE_RATE, 
            output=1   
        )

        self.cont = cont
        cont.setN = self.setNote
        cont.unsetN = self.unsetNote

    def setNote(self, note):

        if(soundList[note] == None):
            soundEvent = WaveLooper(note)
            addInNextEvent.add(soundEvent)
            soundList[note] = soundEvent

    def unsetNote(self, note):

        soundEvent = soundList[note]

        if(soundEvent != None):
            removeInNextEvent.add(soundEvent)
            soundList[note] = None

    def run(self,cont):

        if(cont.notes != -1):
            self.tone()

    def tone(self):

        event = active.union(addInNextEvent).difference(removeInNextEvent)
        result = array.array('f', sine(event)).tostring()
        self.stream.write(result)

    def start(self):
        while self.cont.live:
            self.run(self.cont)

    def end(self):
            self.stream.close()
            self.p.terminate()