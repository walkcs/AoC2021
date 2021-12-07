import pandas as pd
import numpy as np
import statistics as stat

from pandas.core.reshape.concat import concat

def day4p1(input):
    insplit = input.split()
    order = insplit[0].split(',')
    print(order)
    inList = input.split('\n\n')[1:]
    newList = []
    zerosList = []
    for item in inList:
        singleTable = []
        spItem = item.split('\n')
        for si in spItem:
            spSI = si.split()
            singleTable.append(spSI)
        newList.append(singleTable)
    nplist = np.array(newList)
    npTest = nplist=='test'
    

    for num in order:
        newTest = nplist==num
        comboTest = newTest | npTest
        if np.sum(np.count_nonzero(comboTest, axis=1)>=5)>0 or np.sum(np.count_nonzero(comboTest, axis=2)>=5)>0:
            boolTableR = np.sum(np.count_nonzero(comboTest, axis=1)>=5, axis=1)==1
            boolTableC = np.sum(np.count_nonzero(comboTest, axis=2)>=5, axis=1)==1
            boolTable = boolTableR | boolTableC
            winningTable = nplist[boolTable]
            winningMask = comboTest[boolTable]
            maskedWinningArray = np.array(winningTable[np.invert(winningMask)])
            maskedWinningArray = maskedWinningArray.astype(int)
            break
        npTest = comboTest
    return int(num)*np.sum(maskedWinningArray)



samplein = '''
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''
# print(day4p1(samplein))

realInput = 'day4.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()
real4 = day4p1(fileContents)
print(real4)

def day4p2(input):
    insplit = input.split()
    order = insplit[0].split(',')
    inList = input.split('\n\n')[1:]
    newList = []
    zerosList = []
    for item in inList:
        singleTable = []
        spItem = item.split('\n')
        for si in spItem:
            spSI = si.split()
            singleTable.append(spSI)
        newList.append(singleTable)
    nplist = np.array(newList)
    npTest = nplist=='test'
    winningTableScores = []
    npArrayRemaining = nplist
    for num in order:
        
        newTest = npArrayRemaining==num
        comboTest = newTest | npTest

        if np.sum(np.count_nonzero(comboTest, axis=1)>=5)>0 or np.sum(np.count_nonzero(comboTest, axis=2)>=5)>0:
            boolTableR = np.sum(np.count_nonzero(comboTest, axis=1)>=5, axis=1)==1
            boolTableC = np.sum(np.count_nonzero(comboTest, axis=2)>=5, axis=1)==1
            boolTable = boolTableR | boolTableC
            winningTable = npArrayRemaining[boolTable]
            winningMask = comboTest[boolTable]
            maskedWinningArray = np.array(winningTable[np.invert(winningMask)])
            maskedWinningArray = maskedWinningArray.astype(int)
            winningTableScores.append(int(num)*np.sum(maskedWinningArray))
            npArrayRemaining = np.array(npArrayRemaining[np.invert(boolTable)])
            npTest = np.array(comboTest[np.invert(boolTable)])

        else:
            npTest = comboTest
    return winningTableScores



samplein = '''
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''
# print(day4p2(samplein))

realInput = 'day4.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()
real4 = day4p2(fileContents)
print(real4)