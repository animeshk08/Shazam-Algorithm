import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
from math import log



sample_rate, data = wavfile.read('sample.wav')
name = "sample.wav"
left_channel, right_channel = data[:,0], data[:,1]
#print(len(left_channel))
frame_size = 1024
iterations = len(left_channel)//frame_size
#print(frame_size)
#print(iterations)
database = {}


def getIndex(value, lst):
    for j in range(len(lst)):
        if lst[j][0] <= value and lst[j][1] >= value:
            return j

def get4points(sample, lst):
    results = [0,0,0,0]
    for freq in sample:
        index = getIndex(freq, lst)
        value = log(abs(freq) + 1)
        if index is not None and results[index] < value:
             results[index] = round(value, 0)
    return results
   
def createHash(inp, fuz):
    return (inp[3]-(inp[3]%fuz))* 100000000 + (inp[2]-(inp[2]%fuz))* 100000 + (inp[1]-(inp[1]%fuz))* 100 + (inp[0]-(inp[0]%fuz))

bins = [[40, 80], [80, 120], [120, 180], [180, 300]]



for i in range(iterations):
    if int((i+1)*frame_size) > len(left_channel):
        chunk = fft(left_channel[int((i)*frame_size) : len(left_channel)])
        chunk = chunk[0:len(chunk)//2]
    else:
        chunk = fft(left_channel[int((i)*frame_size) : int((i+1)*frame_size)])
        chunk = chunk[0:len(chunk)//2]

    tf = get4points(chunk, bins)
    #print(tf)
    #tag = createHash(tf, 2)
    tag = hash(sum(tf))
    #print(tag)
    database[tag] = [i, name]

print("done")



def check(inp, library, lst):
    size = 1024
    iterations = len(inp)//size
    matches = {}
    for i in range(iterations):
        if int((i+1)* size) > len(inp):
            bit = fft(inp[int(i*size) : len(inp)])
            bit = bit[0:len(bit)//2]
        else:
            bit = fft(inp[int(i*size) : int((i+1)*size)])
            bit = bit[0:len(bit)//2]

        #tag = createHash(get4points(bit, lst), 2)
        tag = hash(sum(get4points(bit, lst)))

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
                dtest = end_test-start_test
                dartist = end_artist-start_artist
                #print(dtest)
                #print(dartist)
                if dtest == dartist:
                    results += 1
                    #print(dtest)
                    #print(dartist)
        #print(mat_lst)
        #print(str((results/len(mat_lst)**2)*100) + "% match with artist" + artist)
        if results >= 30:
            print("it's a match with an artist!")
        else:
            print("Cannot find match!")

### UNIT TEST ###

# Indentical File
test_rate, test_data = wavfile.read("test.wav")
lc, rc = test_data[:,0], test_data[:,0]
check(lc, database, bins)

# Cut File
test_rate, test_data = wavfile.read("test1.wav")
lc, rc = test_data[:,0], test_data[:,0]
check(lc, database, bins)

test_rate, test_data = wavfile.read("test2.wav")
lc, rc = test_data[:,0], test_data[:,0]
check(lc, database, bins)

### Need to add, for whatever song, get sample rate and apply it to duration for testing






