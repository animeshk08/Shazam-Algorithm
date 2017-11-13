import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
from math import log


class library(object):


     def __init__(self, name, freqs, size):
         self.name = name
         self.freqs = freqs
         self.winsize = size
         self.db = {}

     def getIndex(self, value, lst):
         for j in range(len(lst)):
            if lst[j][0] <= value and lst[j][1] >= value:
                 return j

     def get4points(self, sample, lst):
         results = [0,0,0,0]
         for freq in sample:
             index = getIndex(freq, lst)
             value = log(abs(freq) + 1)
             if index is not None and results[index] < value:
                  results[index] = round(value, 0)
         return results
     
     def addtrack(self, track, name):
         iterations = len(track)//self.winsize
         for i in range(iterations):
             if int((i+1)*self.winsize) > len(track):
                 chunk = fft(track[int((i)*self.winsize) : len(track)])
                 chunk = chunk[0:len(chunk)//2]
             else:
                 chunk = fft(track[int((i)*self.winsize) : int((i+1)*self.winsize)])
                 chunk = chunk[0:len(chunk)//2]

             tf = get4points(chunk, self.freqs)
             tag = hash(sum(tf))
             self.db[tag] = [i, name]
         print("done")








