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
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''
realInput = 'day8.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()


def day8p1(textInput):
    inList = multiDelim(textInput, '\n', '|')
    numDict = {2:1,4:4,3:7,7:8}
    totalSum = 0
    for item in inList:
        letterDict = {}
        firstSide = item[0].split()
        lastSide = item[1].split()

        for num in lastSide:
            nl = len(num)
            if nl in numDict.keys():
                totalSum += 1

    return totalSum
print(day8p1(sampleTextInput))

real8p1 = day8p1(fileContents)
print(real8p1)

def day8p2(textInput):
    inList = multiDelim(textInput, '\n', '|')
    numDict = {2:1,4:4,3:7,7:8}
    totalSum = 0
    for item in inList:
        letterDict = {}
        firstSide = item[0].split()
        lastSide = item[1].split()
        len5list = [item2 for item2 in firstSide if len(item2)==5]
        totalLen5 = ''.join(len5list)
        len5dict = dict(Counter(totalLen5))
        c5_3 = list({k:v for (k,v) in len5dict.items() if v == 3}.keys())
        c5_2 = list({k:v for (k,v) in len5dict.items() if v == 2}.keys())
        c5_1 = list({k:v for (k,v) in len5dict.items() if v == 1}.keys())

        
        len6list = [item2 for item2 in firstSide if len(item2)==6]
        for s in len6list:
            z = 0
            sx = 0
            for letter in s:
                if letter in c5_3:
                    z += 1
                elif letter in c5_2:
                    sx += 1
                else:
                    continue
            if z!=3:
                u = "".join(sorted(s))
                letterDict[u] = 0
            elif sx!=2:
                u = "".join(sorted(s))
                letterDict[u] = 6
            else:
                u = "".join(sorted(s))
                letterDict[u] = 9
                for letter in 'abcdefg':
                    if letter not in s:
                        e = letter
        for h in len5list:
            if e in h:
                u = "".join(sorted(h))
                letterDict[u] = 2
            else:
                for letter in h:
                    if letter in c5_1:
                        u = "".join(sorted(h))
                        letterDict[u] = 5
        for h in len5list:
            u = "".join(sorted(h))
            if u not in letterDict.keys():
                letterDict[u] = 3
        for num in firstSide:
            nl = len(num)
            if nl in numDict.keys():
                u = "".join(sorted(num))
                letterDict[u] = numDict[nl]
        combinedNum = []

        for e in lastSide:
            sn = "".join(sorted(e))
            dcNum = letterDict[sn]
            combinedNum.append(str(dcNum))
        intNum = int(''.join(combinedNum))
        totalSum += intNum
    return totalSum


print(day8p2(sampleTextInput))

real8 = day8p2(fileContents)
print(real8)


