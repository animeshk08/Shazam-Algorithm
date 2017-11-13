from scipy.fftpack import fft
from scipy.io import wavfile
from math import log
from database import *
import os, sys, time



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
                if dtest == dartist and dtest != 0 and dartist != 0:
                    results += 1
        print(results)
        if results >= 100:
            print("it's a match with an artist!")
        else:
            print("Cannot find match!")
    print("sorry no matches, try recording again!")


### MAIN CODE ###

bins = [[40, 80], [80, 120], [120, 180], [180, 300]]
db = library("sample library", bins, 1024)

sample_rate, data = wavfile.read('test.wav')
name = "test.wav"
left_channel, right_channel = data[:,0], data[:,1]
db.addtrack(name, left_channel)

sample_rate, data = wavfile.read('other.wav')
name = "other.wav"
left_channel, right_channel = data[:,0], data[:,1]
db.addtrack(name, left_channel)

while True:
     inp = raw_input('Type "record" to start recording: ')
     print(inp)
     if inp == "record":
          os.system("python record.py")
          test_rate, test_data = wavfile.read("record.wav")
          lc, rc = test_data[:,0], test_data[:,0]
          check(lc, db.db, bins)





