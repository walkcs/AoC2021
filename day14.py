import pandas as pd
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt


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
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''
realInput = 'day14.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()


def day14p1(textInput, steps):
    spInput = list(filter(None, textInput.split('\n')))
    insertionDict = {}
    for item in spInput:
        if '->' not in item:
            startInstruction = item
        else:
            spLine = item.split(' -> ')
            insertionDict[spLine[0]] = spLine[1]
    for s in range(steps):
        i = 0
        newLine = ''
        if s==0:
            oldLine = startInstruction
        while i < len(oldLine)-1:
            pair = oldLine[i]+oldLine[i+1]
            if i==len(oldLine)-2:
                newTrio = oldLine[i]+insertionDict[pair]+oldLine[i+1]
            else:
                newTrio = oldLine[i]+insertionDict[pair]
            newLine = newLine + newTrio
            i += 1
        oldLine = newLine

    maxCount = max(list(Counter(newLine).values()))
    minCount = min(list(Counter(newLine).values()))
    return maxCount - minCount



print(day14p1(sampleTextInput,10))

real14p1 = day14p1(fileContents, 10)
print(real14p1)

def day14p2(textInput, steps):
    spInput = list(filter(None, textInput.split('\n')))
    insertionDict = {}
    for item in spInput:
        if '->' not in item:
            startInstruction = item
        else:
            spLine = item.split(' -> ')
            insertionDict[spLine[0]] = spLine[1]
    pairs = Counter(map(str.__add__,startInstruction, startInstruction[1:]))
    chars = Counter(startInstruction)    
    for s in range(steps):
        for (a,b), c in pairs.copy().items():
            x = insertionDict[a+b]
            pairs[a+b] -= c
            pairs[a+x] += c
            pairs[x+b] += c
            chars[x] += c
    return max(chars.values())-min(chars.values())

    #maxCount = max(list(Counter(newLine).values()))
    #minCount = min(list(Counter(newLine).values()))
    #return maxCount - minCount


print(day14p2(sampleTextInput, 40))

real14 = day14p2(fileContents, 40)

print(real14)


