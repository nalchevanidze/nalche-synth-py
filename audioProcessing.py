import math
import pyaudio
import array
from wave_looper import WaveLooper;
from audio_config import SAMPLE_RATE;

LOOPSIZE = int(SAMPLE_RATE/100);

def sine(sound):
    c = [];
    for i in range(0, LOOPSIZE):
        c.append( math.sin( sound.next() )   )
    return c;

sound = WaveLooper(); 

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
        sound.state = 0;
        sound.set(note * 64 + 240);
    def run (self,cont):
        if(cont.notes != -1):
            self.tone();
    def tone(self):
        result = array.array('f',
            sine(sound)
        ).tostring();

        self.stream.write(result);

    def start(self):
        while(True):
            self.tone()

    def end(self):
            self.stream.close();
            self.p.terminate();