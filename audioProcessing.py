import math
import pyaudio
import array
from wave_looper import WaveLooper;
from audio_config import SAMPLE_RATE;
from sets import Set;

LOOPSIZE = int(SAMPLE_RATE/4100);

def sine(sounds):
    c = [];
    for i in range(0, LOOPSIZE):
        value = 0;

        for sound in sounds:
            value += math.sin(sound.next());

        c.append(value);

    return c;

sound = WaveLooper(); 
soundList = [sound];
soundSet = Set([]);

soundList = [None] * 49;

active = Set([]);

class AudioProcessor:
    def __init__(self):
        self.p = pyaudio.PyAudio();
        self.stream = self.p.open(
            format=pyaudio.paFloat32,         
            channels=1, 
            rate=SAMPLE_RATE, 
            output=1   
        );
    def setNote(self,note):
        if(soundList[note] == None):
            soundEvent = WaveLooper(note);
            active.add(soundEvent);
            soundList[note] = soundEvent;

    def unsetNote(self,note):

        soundEvent = soundList[note];

        if(soundEvent != None):
            active.remove(soundEvent);
            soundList[note] = None;
            
            
    def run (self,cont):
        if(cont.notes != -1):
            self.tone()
    def tone(self):
        result = array.array('f',
            sine(active)
        ).tostring();

        self.stream.write(result);

    def start(self):
        while(True):
            self.tone()

    def end(self):
            self.stream.close();
            self.p.terminate();