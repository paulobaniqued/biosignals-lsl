""" EMG-LSL Simulator: This script simulates a continuous stream of EMG data
at 250 Hz then sends it to labstreaminglayer to be received by Python via pylsl
or in Unity by LSL4Unity."""

import numpy as np
import matplotlib.pyplot as plt
import time 

from pylsl import StreamInfo, StreamOutlet

# Create stream info for LSL
info = StreamInfo('emg_stream', 'EMG', 1, 250, 'float32', 'myuidemgemg')

# next make an outlet
outlet = StreamOutlet(info)

# simulate EMG signal
flex1 = np.random.uniform(-1, 1, size=1000) + 0.08
flex2 = np.random.uniform(-1.25, 1.25, size=1200) + 0.08
relax = np.random.uniform(-0.05, 0.05, size=2000) + 0.08
emg_sim = np.concatenate([relax, relax, flex1, relax, flex2, flex1, relax])
emg_sim = np.concatenate([emg_sim, emg_sim])
t = np.array([i/1000 for i in range(0, len(emg_sim)-99, 1)])
np.array(emg_sim, dtype='float32')

# Root mean square
def window_rms(emg_sim, window_size):
  emg_sqd = np.power(emg_sim,2)
  window = np.ones(window_size)/float(window_size)
  return np.sqrt(np.convolve(emg_sqd, window, 'valid'))
emg_rms = window_rms(emg_sim, 100)

# Stream simulated EMG signal to LSL
print("now sending data...")
while True:
    # push sample to outlet

    for sample in emg_rms:
        print(sample)
        outlet.push_sample([sample])
        time.sleep(0.004)
