import pandas as pd
import numpy as np
import statistics as stat

from pandas.core.reshape.concat import concat

from collections import Counter

def multiDelim(inString, d1, d2):
    l1 = inString.split(d1)
    l2 = []
    for item in l1:
        if len(item)>0:
            if d2=='all':
                spItem = item.split()
            else:
                spItem = item.split(d2)
                spItem = list(filter(None, spItem))
            l2.append(spItem)
    return l2

sampleTextInput = '''
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
'''
realInput = 'day13.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()


def day13p1(textInput, folds):
    spInput = textInput.split('\n')
    coordList = []
    foldList = []
    for line in spInput:
        if len(line)>0:
            if 'fold' in line:
                spLine = line.split()
                instruc = spLine[2]
                spIns = instruc.split('=')
                direction = spIns[0]
                location = int(spIns[1])
                foldList.append([direction, location])
            else:
                spLine = line.split(',')
                x = int(spLine[0])
                y = int(spLine[1])
                coordList.append([x,y])
    CA = np.array(coordList)
    maxValue = np.amax(CA, axis=0)

    ZA = np.zeros((maxValue[1]+1, maxValue[0]+1), dtype=int)
    for i in CA:
        x = i[0]
        y = i[1]
        ZA[y,x] = 1

    for f in range(folds):
        fold = foldList[f]
        direction = fold[0]
        location = int(fold[1])
        if f==0:
            RA = np.copy(ZA)
        if direction=='y':
            FA = np.copy(RA[0:location, :])
            SA = np.flip(np.copy(RA[location+1:, :]), axis=0)
            RA = np.copy(FA[-(location+1):,:])+np.copy(SA)
        else:
            FA = np.copy(RA[:, 0:location])
            SA = np.flip(np.copy(RA[:, location+1:]), axis=1)
            RA = np.copy(FA[:,-(location+1):])+np.copy(SA)


    return np.count_nonzero(RA > 0) 




print(day13p1(sampleTextInput,1))

real13p1 = day13p1(fileContents, 1)
print(real13p1)

def day13p2(textInput):
    spInput = textInput.split('\n')
    coordList = []
    foldList = []
    for line in spInput:
        if len(line)>0:
            if 'fold' in line:
                spLine = line.split()
                instruc = spLine[2]
                spIns = instruc.split('=')
                direction = spIns[0]
                location = int(spIns[1])
                foldList.append([direction, location])
            else:
                spLine = line.split(',')
                x = int(spLine[0])
                y = int(spLine[1])
                coordList.append([x,y])
    CA = np.array(coordList)
    maxValue = np.amax(CA, axis=0)

    ZA = np.zeros((maxValue[1]+1, maxValue[0]+1), dtype=int)
    for i in CA:
        x = i[0]
        y = i[1]
        ZA[y,x] = 1

    for f,fold in enumerate(foldList):
        direction = fold[0]
        location = int(fold[1])
        if f==0:
            RA = np.copy(ZA)
        if direction=='y':
            FA = np.copy(RA[0:location, :])
            SA = np.flip(np.copy(RA[location+1:, :]), axis=0)
            RA = np.copy(FA[-(location+1):,:])+np.copy(SA)
        else:
            FA = np.copy(RA[:, 0:location])
            SA = np.flip(np.copy(RA[:, location+1:]), axis=1)
            RA = np.copy(FA[:,-(location+1):])+np.copy(SA)

    an_array = np.where(RA > 0, 1, RA)
    return an_array


print(day13p2(sampleTextInput))

real13 = day13p2(fileContents)
print(real13)


