import math;
from audio_config import SAMPLE_RATE;

def note_to_frequency(index):
    power_value = (index - 49) / 12
    return (2 ** power_value) * 440


class WaveLooper:
    def __init__(self, note=1):
        self.state = 0
        self.waveSize =(math.pi * 2)
        self.set(note)

    def set(self, note=1):
        frequency = note_to_frequency(note + 36)
        self.frequency = frequency
        self.step_size = float(frequency) / SAMPLE_RATE

    def next(self):
        self.state = (self.state + self.step_size) % self.waveSize
        return self.state
