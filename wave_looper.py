import math;
from audio_config import SAMPLE_RATE;

class WaveLooper:
    def __init__(self):
        self.state = 0;
        self.frequency = 440;
        self.stepSize = 0;
        self.waveSize =(math.pi * 2);

    def set(self, frequency = 440 ):
        self.frequency = frequency;
        self.stepSize = float(frequency) / (SAMPLE_RATE);

    def next(self):
        self.state  = (self.state + self.stepSize) % self.waveSize;
        return self.state;