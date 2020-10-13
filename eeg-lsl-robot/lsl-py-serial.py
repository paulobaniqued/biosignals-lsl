import serial
import time

ser = serial.Serial('COM4', 9600)
time.sleep(2)

thresh = 0.5

from pylsl import StreamInlet, resolve_stream

# first resolve an EEG stream on the lab network
print("looking for a control EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample, timestamp = inlet.pull_sample()
    state = sample[0]
    #print(state)

    if state >= thresh:
        print("close")
        ser.write(b'H')
    
    elif state < thresh:
        print("open")
        ser.write(b'L')
    else:
        print("There is something wrong...")
