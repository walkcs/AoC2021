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
start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''

realInput = 'day12.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()


def day12p1(textInput):
    pathList = multiDelim(textInput, '\n', '-')
    x = np.array(pathList)

    startArrays = [x for x in pathList if 'start' in x]
    for p, item in enumerate(startArrays):
        if item[-1]=='start':
            startArrays[p] = [item[-1], item[0]]



    nonStartArrays = [x for x in pathList if 'start' not in x]
    for p, item in enumerate(nonStartArrays):
        if item[0]=='end':
            nonStartArrays[p] = [item[-1], item[0]]


    def addSteps(sa,nsa,ea):
        newList = []
        endList = ea
        for item in sa:
            sv = item[-1]
            if sv!='end':
                newOptions = [x for x in nsa if sv in x]
                
                for i in newOptions:
                    line = []
                    for k in item:
                        line.append(k)
                    for ch in i:
                        if ch!=sv:
                            if ch.islower() and ch in item:
                                line = []
                            else:
                                line.append(ch)
                    if i[-1]=='end':
                        endList.append(line)
                    else:
                        newList.append(line)
        newList = list(filter(None, newList))
        return newList, endList
    
    steps,endSteps = addSteps(startArrays, nonStartArrays,[])

    i = 0
    while len(steps) > 0:
        steps,endSteps = addSteps(steps, nonStartArrays, endSteps)
        i += 1

    return len(endSteps)


print(day12p1(sampleTextInput))

real12p1 = day12p1(fileContents)
print(real12p1)

def day12p2(textInput):
    pathList = multiDelim(textInput, '\n', '-')
    x = np.array(pathList)

    startArrays = [x for x in pathList if 'start' in x]
    for p, item in enumerate(startArrays):
        if item[-1]=='start':
            startArrays[p] = [item[-1], item[0]]



    nonStartArrays = [x for x in pathList if 'start' not in x]
    for p, item in enumerate(nonStartArrays):
        if item[0]=='end':
            nonStartArrays[p] = [item[-1], item[0]]


    def addSteps(sa,nsa,ea):
        newList = []
        endList = ea
        for item in sa:
            sv = item[-1]
            if sv!='end':
                newOptions = [x for x in nsa if sv in x]
                
                for i in newOptions:
                    line = []
                    for k in item:
                        line.append(k)
                    for ch in i:
                        if ch!=sv:
                            nonStartEnd = [x for x in item if x!='start']
                            nonStartEnd = [x for x in nonStartEnd if x!='end']

                            if len(nonStartEnd)>0:
                                listLower = list(Counter([x for x in nonStartEnd if x.islower()]).values())
                                if len(listLower)==0:
                                    maxNoLower = 0
                                else:
                                    maxNoLower = max(listLower)
                            else:
                                maxNoLower = 0
                            if ch.islower() and ch!='end' and maxNoLower==2 and ch in item:
                                line = []
                            else:
                                line.append(ch)
                    if i[-1]=='end' and len(line)!=0:
                        endList.append(line)
                    elif len(line)!=0:
                        newList.append(line)
        newList = list(filter(None, newList))
        return newList, endList
    
    steps,endSteps = addSteps(startArrays, nonStartArrays,[])

    i = 0
    while len(steps) > 0:
        steps,endSteps = addSteps(steps, nonStartArrays, endSteps)
        i += 1


    return len(endSteps)


print(day12p2(sampleTextInput))

real12 = day12p2(fileContents)
print(real12)


