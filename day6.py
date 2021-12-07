import pandas as pd
import numpy as np
import statistics as stat

from pandas.core.reshape.concat import concat


def day6p1(textInput,ndays):
    inList = list(map(int, textInput.split(',')))
    fish = [inList.count(i) for i in range(9)]
    for i in range(ndays):
        num = fish.pop(0)
        fish[6] += num
        fish.append(num)
    return sum(fish)

sampleIn = '3,4,3,1,2'
print(day6p1(sampleIn,256))


realInput = 'day6.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()
real6 = day6p1(fileContents, 256)
print(real6)