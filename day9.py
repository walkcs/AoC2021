from numpy.lib.function_base import delete
import pandas as pd
import numpy as np
import statistics as stat

from pandas.core.reshape.concat import concat

from collections import Counter


sampleTextInput = '''
2199943210
3987894921
9856789892
8767896789
9899965678
'''
realInput = 'day9.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()


def day9p1(textInput):
    spInput = list(filter(None, textInput.split()))
    mask = np.full((len(spInput), len(spInput[0])), False)
    totalRL = 0
    for r, n in enumerate(spInput):
        for c, ch in enumerate(n):
            if c!=0 and c!=len(n)-1 and r!=0 and r!=len(spInput)-1:
                clist = [n[c-1], n[c+1], spInput[r-1][c], spInput[r+1][c]]
            elif c==0 and r==0:
                clist = [n[c+1], spInput[r+1][c]]
            elif c==len(n)-1 and r==len(spInput)-1:
                clist = [n[c-1], spInput[r-1][c]]          
            elif c==len(n)-1:
                clist = [n[c-1], spInput[r-1][c], spInput[r+1][c]]
            elif r==len(spInput)-1:
                clist = [n[c-1], n[c+1], spInput[r-1][c]]  
            elif c==0:
                clist = [n[c+1], spInput[r-1][c], spInput[r+1][c]] 
            elif r==0:
                clist = [n[c-1], n[c+1], spInput[r+1][c]] 
            if all(int(x) > int(ch) for x in clist):
                mask[r,c] = True
                totalRL += int(ch)+1


    
    return totalRL


print(day9p1(sampleTextInput))

real9p1 = day9p1(fileContents)
print(real9p1)

def day9p2(textInput):
    spInput = list(filter(None, textInput.split()))
    mask = np.full((len(spInput), len(spInput[0])), False)
    
    for r, n in enumerate(spInput):
        for c, ch in enumerate(n):
            if int(ch)==9:
                mask[r,c] = True

    rList = []
    for r, k in enumerate(mask):
        subList = []
        for c, i in enumerate(k):
            rc = str(r)+'.'+str(c)
            if i==False and c==len(k)-1:
                subList.append(rc)
                rList.append(subList)
            elif i==False:
                subList.append(rc)
            elif c==len(k)-1 and len(subList)>0:
                rList.append(subList)
            elif len(subList)>0:
                rList.append(subList)
                subList = []


    cList = []
    for c in range(len(mask[0])):
        col = mask[:,c]
        subList = []
        for r, i in enumerate(col):
            rc = str(r)+'.'+str(c)
            if i==False and r==len(col)-1:
                subList.append(rc)
                cList.append(subList)
            elif i==False:
                subList.append(rc)
            elif r==len(col)-1 and len(subList)>0:
                cList.append(subList)
            elif len(subList)>0:
                cList.append(subList)
                subList = []
    cs = []

    for r in rList:
        for c in cList:
            overlapList = [value for value in r if value in c]
            
            if len(overlapList)>0:
                combinedList = r + c
                combinedSet = list(set(combinedList))
                cs.append(combinedSet)
    
    pooled = [set(subList) for subList in cs]
    merging = True
    while merging:
        merging=False
        for i,group in enumerate(pooled):
            merged = next((g for g in pooled[i+1:] if g.intersection(group)),None)
            if not merged: continue
            group.update(merged)
            pooled.remove(merged)
            merging = True
    s = []
    for item in pooled:
        s.append(len(item))

    return np.prod(sorted(s)[-3:])



print(day9p2(sampleTextInput))

real9 = day9p2(fileContents)
print(real9)


