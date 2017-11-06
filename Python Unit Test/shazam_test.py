import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile


sample_rate, data = wavfile.read('sample.wav')
name = "sample.wav"
left_channel, right_channel = data[:,0], data[:,1]
#print(len(left_channel))
#frame_size = len(left_channel) / 4
frame_size = 500
iterations = len(left_channel)//frame_size + 1
print(frame_size)
print(iterations)
database = {}

for i in range(iterations):
    if int((i+1)*frame_size) > len(left_channel):
        chunk = fft(left_channel[int((i)*frame_size) : len(left_channel)])
    else:
        chunk = fft(left_channel[int((i)*frame_size) : int((i+1)*frame_size)])
    #print(chunk)
    print(max(chunk, key=abs))
    #print(i)
    tag = hash(max(chunk, key=abs))
    #print(tag)
    database[tag] = [i, name]

print("done")



def check(inp, length, library):
    size = 500
    matches = {}
    for i in range(length):
        if int((i+1)* size) > len(inp):
            bit = fft(inp[int(i*size) : len(inp)])
        else:
            bit = fft(inp[int(i*size) : int((i+1)*size)])
        #print(bit)
        print(max(bit, key=abs))
        #print(i)
        tag = hash(max(bit, key=abs))
        #print(tag)
        if tag in library:
            time, name = library[tag]
            if name not in matches:
                matches[name] = [[i, time]]
            else:
                matches[name].append([i, time])
    for artist in matches:
        mat_lst = matches[artist]
        results = 0
        for x in range(len(mat_lst)):
            for y in range(len(mat_lst)):
                start_test, start_artist = mat_lst[x]
                end_test, end_artist = mat_lst[y]
                if end_artist-start_artist == end_test-start_test:
                    results += 1
        print(str((results/len(mat_lst)**2)*100) + "% match with artist" + artist)

### UNIT TEST ###

# Indentical File
test_rate, test_data = wavfile.read("test.wav")
lc, rc = test_data[:,0], test_data[:,0]
#check(lc, len(lc)//500 + 1, database)

# Cut File
test_rate, test_data = wavfile.read("test1.wav")
lc, rc = test_data[:,0], test_data[:,0]
#check(lc, len(lc)//500 + 1, database)

test_rate, test_data = wavfile.read("test2.wav")
lc, rc = test_data[:,0], test_data[:,0]
check(lc, len(lc)//500 + 1, database)

### Need to add, for whatever song, get sample rate and apply it to duration for testing






