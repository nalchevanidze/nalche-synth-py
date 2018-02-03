import math
import pyaudio
import array

RATE = 44100;
LOOPSIZE = RATE/100;

def sine(sound):
    c = [];
    for i in range(0, LOOPSIZE):
        c.append( math.sin( sound.next() )   )
    return c;

class WaveLooper:
    def __init__(self):
        self.state = 0;
        self.frequency = 440;
        self.stepSize = 0;
        self.waveSize =(math.pi * 2);

    def set(self, frequency = 440 ):
        self.frequency = frequency;
        self.stepSize = float(frequency) / (RATE);

    def next(self):
        self.state  = (self.state + self.stepSize) % self.waveSize;
        return self.state;

sound = WaveLooper(); 

class AudioProcessor:
    def __init__(self):
        self.p = pyaudio.PyAudio();
        self.stream = self.p.open(
            format=pyaudio.paFloat32,         
            channels=1, 
            rate=RATE, 
            output=1   
        );
    def tone(self, freq = 440):
        sound.set(freq * 16);

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