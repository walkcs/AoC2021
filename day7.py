import pandas as pd
import numpy as np
import statistics as stat

from pandas.core.reshape.concat import concat


def day7p1(textInput):
    inList = list(map(int, textInput.split(',')))
    i = min(inList)
    while i <= max(inList):
        diffList = [abs(number - i) for number in inList]
        if i==min(inList):
            minSum = sum(diffList)
        elif sum(diffList) < minSum:
            minSum = sum(diffList)
        i += 1

    return minSum

sampleIn = '16,1,2,0,4,2,7,1,2,14'
print(day7p1(sampleIn))


realInput = 'day7.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()
real7 = day7p1(fileContents)
print(real7)

def triangularNumber(inNumber):
    for i in range(inNumber):
        inNumber += i
    return inNumber

def day7p2(textInput):
    inList = list(map(int, textInput.split(',')))
    i = min(inList)
    while i <= max(inList):
        diffList = [triangularNumber(abs(number - i)) for number in inList]
        if i==min(inList):
            minSum = sum(diffList)
        elif sum(diffList) < minSum:
            minSum = sum(diffList)
        i += 1

    return minSum

sampleIn = '16,1,2,0,4,2,7,1,2,14'
print(day7p2(sampleIn))


realInput = 'day7.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()
real7 = day7p2(fileContents)
print(real7)