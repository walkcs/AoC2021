import pandas as pd
import numpy as np
import statistics as stat

from pandas.core.reshape.concat import concat

def Day1(input):
    counter = 0
    splitInput = input.split()
    for i, item in enumerate(splitInput):
        k = int(item)
        if i==0:
            continue
        else:
            p = int(splitInput[i-1])
            if k > p:
                counter += 1
    return counter

sampleInput = '''199
200
208
210
200
207
240
269
260
263'''
sample = Day1(sampleInput)
print(sample)

realInput = 'day1.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()
real1 = Day1(fileContents)
print(real1)

def Day1p2(input):
    counter = 0
    splitInput = input.split()
    for i, item in enumerate(splitInput):
        k = int(item)
        if i==0:
            k1 = int(splitInput[i+1])
            k2 = int(splitInput[i+2])
            window = k + k1 + k2
            prevWindow = window
        elif i + 2 < len(splitInput):
            k1 = int(splitInput[i+1])
            k2 = int(splitInput[i+2])
            window = k + k1 + k2
            if window > prevWindow:
                counter += 1
        prevWindow = window           
    return counter

sampleInput = '''199
200
208
210
200
207
240
269
260
263'''
sample = Day1p2(sampleInput)
print(sample)

realInput = 'day1.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()
real1 = Day1p2(fileContents)
print(real1)