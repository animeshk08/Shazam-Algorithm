import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile


sample_rate, data = wavfile.read('sample.wav') # load the data
name = "sample.wav"
left_channel, right_channel = data[:,0], data[:,1]
print(left_channel)
print(right_channel)

freq_domain = fft(left_channel)
print(freq_domain)

### Time Domain
plt.plot(range(len(left_channel)), left_channel)
#plt.show()

### Frequency Domain
plt.plot(range(len(freq_domain)), freq_domain)
#plt.show()


#print(left_channel.shape)
frame_size = len(left_channel) / 10
#print(frame_size)

database = {}

for i in range(10):
    chunk = fft(left_channel[int(i*frame_size):int((i+1)*frame_size)])
    database[hash(max(chunk, key=abs))] = [i, name]
    




