import pandas as pd
import numpy as np
import statistics as stat

from pandas.core.reshape.concat import concat

def day2p1(input):
    spi = input.split('\n')
    UD = 0
    LR = 0
    for line in spi:
        if len(line)==0:
            continue
        else:
            spl = line.split()
            if spl[0]=='up':
                UD = UD - int(spl[1])
            elif spl[0]=='down':
                UD = UD + int(spl[1])
            elif spl[0]=='forward':
                LR = LR + int(spl[1])
    mult = UD * LR
    return mult

sample = '''
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''
print(day2p1(sample))

realInput = 'day2.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()
real2 = day2p1(fileContents)
print(real2)

def day2p2(input):
    spi = input.split('\n')
    UD = 0
    LR = 0
    aim = 0
    for line in spi:
        if len(line)==0:
            continue
        else:
            spl = line.split()
            if spl[0]=='up':
                aim = aim - int(spl[1])
            elif spl[0]=='down':
                aim = aim + int(spl[1])
            elif spl[0]=='forward':
                LR = LR + int(spl[1])
                UD = UD + aim*int(spl[1])
    mult = UD * LR
    return mult

sample = '''
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''
print(day2p2(sample))

realInput = 'day2.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()
real2 = day2p2(fileContents)
print(real2)