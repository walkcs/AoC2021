import pandas as pd
import numpy as np
import statistics as stat

from pandas.core.reshape.concat import concat

def day3p1(input):
    insplit = input.split()
    newList = []
    for num in insplit:
        splitNum = list(num)
        newList.append(splitNum)
    inNP = pd.DataFrame(newList)
    modeDF = inNP.mode()
    modeList = modeDF.values.tolist()
    modeNum = ''.join(modeList[0])
    decMN = int(modeNum,2)
    oppMN = []
    for num in modeNum:
        if num=='0':
            oppMN.append('1')
        else:
            oppMN.append('0')
    OMN = ''.join(oppMN)
    decOMN = int(OMN,2)
    mult = decMN*decOMN
    return mult


samplein = '''
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''
print(day3p1(samplein))

realInput = 'day3.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()
real3 = day3p1(fileContents)
print(real3)

def day3p2(input):
    insplit = input.split()
    newList = []
    for num in insplit:
        splitNum = list(num)
        newList.append(splitNum)
    startNP = pd.DataFrame(newList)
    inNP = pd.DataFrame(newList)
    k = 0
    while k < inNP.shape[1]:
        colMode = inNP[k].mode()
        if len(colMode)==1:
            inNP = inNP.loc[(inNP[k]==colMode[0])]
        else:
            inNP = inNP.loc[(inNP[k]=='1')]
        k += 1

    modeList = inNP.values.tolist()
    modeNum = ''.join(modeList[0])
    OGR = int(modeNum,2)


    in2NP = pd.DataFrame(newList)
    k = 0
    while k < in2NP.shape[1]:
        colMode = in2NP[k].mode()

        if len(colMode)==1:
            if colMode[0]=='1':
                colMode2 = '0'
            else:
                colMode2 = '1'
            in2NP = in2NP.loc[(in2NP[k]==colMode2)]
        else:
            in2NP = in2NP.loc[(in2NP[k]=='0')]
        if in2NP.shape[0]==1:
            k = in2NP.shape[1]
        else:
            k += 1

    modeList = in2NP.values.tolist()
    modeNum = ''.join(modeList[0])
    CO2R = int(modeNum,2)
 

    LSR = OGR * CO2R
    return LSR



samplein = '''
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''
print(day3p2(samplein))

realInput = 'day3.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()
real3 = day3p2(fileContents)
print(real3)