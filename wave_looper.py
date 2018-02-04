import math;
from audio_config import SAMPLE_RATE;

class WaveLooper:
    def __init__(self, note = 0):
        self.state = 0;
        self.waveSize =(math.pi * 2);
        self.set(440 + note * 64 )

    def set(self, frequency = 440 ):
        self.frequency = frequency;
        self.stepSize = float(frequency) / (SAMPLE_RATE);

    def next(self):
        self.state  = (self.state + self.stepSize) % self.waveSize;
        return self.state;