import pandas as pd
import numpy as np
import statistics as stat

from pandas.core.reshape.concat import concat

def multiDelim(inString, d1, d2):
    l1 = inString.split(d1)
    l2 = []
    for item in l1:
        spItem = item.split(d2)
        l2.append(spItem)
    return l2

def day5p1(textFile):
    inList = multiDelim(textFile, '\n', ' -> ')
    SLlist = []
    coveredPoints = []
    for item in inList:
        p1 = item[0].split(',')
        x1 = int(p1[0])
        y1 = int(p1[1])
        p2 = item[1].split(',')
        x2 = int(p2[0])
        y2 = int(p2[1])
        if x1==x2:
            if y1>y2:
                newys = list(range(y2, y1+1))
                for y in newys:
                    newString = str(x2)+','+str(y)
                    coveredPoints.append(newString)
            else:
                newys = list(range(y1, y2+1))
                for y in newys:
                    newString = str(x2)+','+str(y)
                    coveredPoints.append(newString)            
        elif y1==y2:
            if x1>x2:
                newxs = list(range(x2, x1+1))
                for x in newxs:
                    newString = str(x)+','+str(y2)
                    coveredPoints.append(newString)
            else:
                newxs = list(range(x1, x2+1))
                for x in newxs:
                    newString = str(x)+','+str(y2)
                    coveredPoints.append(newString)           
    pointCounts = [[x,coveredPoints.count(x)] for x in set(coveredPoints)]
    totalCount = 0
    for item in pointCounts:
        if int(item[1])>1:
            totalCount += 1
    return totalCount

sampleIn = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''
print(day5p1(sampleIn))

realInput = 'day5.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()
real5 = day5p1(fileContents)
print(real5)

def day5p2(textFile):
    inList = multiDelim(textFile, '\n', ' -> ')
    SLlist = []
    coveredPoints = []
    for item in inList:
        p1 = item[0].split(',')
        x1 = int(p1[0])
        y1 = int(p1[1])
        p2 = item[1].split(',')
        x2 = int(p2[0])
        y2 = int(p2[1])
        if x1==x2:
            if y1>y2:
                newys = list(range(y2, y1+1))
                for y in newys:
                    newString = str(x2)+','+str(y)
                    coveredPoints.append(newString)
            else:
                newys = list(range(y1, y2+1))
                for y in newys:
                    newString = str(x2)+','+str(y)
                    coveredPoints.append(newString)            
        elif y1==y2:
            if x1>x2:
                newxs = list(range(x2, x1+1))
                for x in newxs:
                    newString = str(x)+','+str(y2)
                    coveredPoints.append(newString)
            else:
                newxs = list(range(x1, x2+1))
                for x in newxs:
                    newString = str(x)+','+str(y2)
                    coveredPoints.append(newString)    
        elif x2 > x1 and y2 > y1:
            xa = list(range(x1, x2+1))
            ya = list(range(y1, y2+1))
            for l, x in enumerate(xa):
                newString = str(x)+','+str(ya[l])
                coveredPoints.append(newString)  
        elif x2 < x1 and y2 < y1:
            xa = list(range(x1, x2-1,-1))
            ya = list(range(y1, y2-1, -1))
            for l, x in enumerate(xa):
                newString = str(x)+','+str(ya[l])
                coveredPoints.append(newString)  
        elif x2 > x1 and y2 < y1:
            xa = list(range(x1, x2+1))
            ya = list(range(y1, y2-1, -1))
            for l, x in enumerate(xa):
                newString = str(x)+','+str(ya[l])
                coveredPoints.append(newString)  
        elif x2 < x1 and y2 > y1: 
            xa = list(range(x1, x2-1, -1))
            ya = list(range(y1, y2+1))
            for l, x in enumerate(xa):
                newString = str(x)+','+str(ya[l])
                coveredPoints.append(newString)  
    pointCounts = [[x,coveredPoints.count(x)] for x in set(coveredPoints)]
    totalCount = 0
    for item in pointCounts:
        if int(item[1])>1:
            totalCount += 1
    return totalCount

sampleIn = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''
print(day5p2(sampleIn))

realInput = 'day5.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()
real5 = day5p2(fileContents)
print(real5)