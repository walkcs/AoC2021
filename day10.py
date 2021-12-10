from numpy.lib.function_base import delete
import pandas as pd
import numpy as np
import statistics as stat
import re

from pandas.core.reshape.concat import concat

from collections import Counter


sampleTextInput = '''
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''
realInput = 'day10.txt'
with open(realInput, 'r') as inFile:
    fileContents = inFile.read()


def day10p1(textInput):
    def EOLcheckString(textIn):
        open_list = ["[","{","(", "<"]
        close_list = ["]","}",")", ">"]
        open_count = [0,0,0,0]
        close_count = [0,0,0,0]
        r = 'Balanced'
        for i in textIn:
            if i in open_list:
                pos = open_list.index(i)
                open_count[pos] += 1
            else:
                pos = close_list.index(i)
                close_count[pos] += 1
                if close_count[pos] > open_count[pos]:
                    r = 'Unbalanced'
        if open_count!=close_count:
            r = 'Unbalanced'
        return r
    def check(textIn):
        unbalancedRowChars = []
        figMatches = {')':'(', ']': '[', '}':'{','>':'<'}
        i = 0
        u = 0
        textList = list(textIn)
        while i < len(textList) and u==0:
            ch = textList[i]
            if i==0 and ch in figMatches.keys():
                u = 1
            elif ch in figMatches.keys():
                    searchFor = figMatches[ch]
                    k = i - 1
                    z = 0
                    while u==0 and z == 0:
                        if k==-1:
                            unbalancedRowChars = ch
                            u = 1
                            z = 1                        
                        elif textList[k]==searchFor:
                            testString = textList[k:i+1]
                            check = EOLcheckString(testString)
                            if check=='Unbalanced':
                                unbalancedRowChars = ch
                                u = 1
                                z = 1
                            else:                       
                                del textList[k:i+1]
                                i = k 
                                z = 1

                        else:
                            k += -1
            else:
                i += 1
        return unbalancedRowChars
    spInput = textInput.split()
    unBCh = []
    for line in spInput:
        if len(check(line))>0:
            unBCh.append(check(line))
    scoreDict = {')':3, ']':57, '}':1197, '>':25137}
    totalScore = 0
    for item in unBCh:
        score = scoreDict[item]
        totalScore += score
    return totalScore
    


print(day10p1(sampleTextInput))


real10p1 = day10p1(fileContents)
print(real10p1)

def day10p2(textInput):
    def EOLcheckString(textIn):
        open_list = ["[","{","(", "<"]
        close_list = ["]","}",")", ">"]
        open_count = [0,0,0,0]
        close_count = [0,0,0,0]
        r = 'Balanced'
        for i in textIn:
            if i in open_list:
                pos = open_list.index(i)
                open_count[pos] += 1
            else:
                pos = close_list.index(i)
                close_count[pos] += 1
                if close_count[pos] > open_count[pos]:
                    r = 'Unbalanced'
        if open_count!=close_count:
            r = 'Unbalanced'
        return r
    def check(textIn):
        unbalancedRowChars = []
        figMatches = {')':'(', ']': '[', '}':'{','>':'<'}
        i = 0
        u = 0
        textList = list(textIn)
        while i < len(textList) and u==0:
            ch = textList[i]
            if i==0 and ch in figMatches.keys():
                u = 1
            elif ch in figMatches.keys():
                    searchFor = figMatches[ch]
                    k = i - 1
                    z = 0
                    while u==0 and z == 0:
                        if k==-1:
                            unbalancedRowChars = ch
                            u = 1
                            z = 1                        
                        elif textList[k]==searchFor:
                            testString = textList[k:i+1]
                            check = EOLcheckString(testString)
                            if check=='Unbalanced':
                                unbalancedRowChars = ch
                                u = 1
                                z = 1
                            else:                       
                                del textList[k:i+1]
                                i = k 
                                z = 1

                        else:
                            k += -1
            else:
                i += 1
        return unbalancedRowChars

    spInput = textInput.split()
    cleanLines = []
    for line in spInput:
        if len(check(line))==0:
            cleanLines.append(line)
    def check2(textIn):
        unbalancedRowChars = []
        figMatches = {')':'(', ']': '[', '}':'{','>':'<'}
        i = 0
        u = 0
        textList = list(textIn)
        while i < len(textList) and u==0:
            ch = textList[i]
            if i==0 and ch in figMatches.keys():
                u = 1
            elif ch in figMatches.keys():
                    searchFor = figMatches[ch]
                    k = i - 1
                    z = 0
                    while u==0 and z == 0:
                        if k==-1:
                            unbalancedRowChars = ch
                            u = 1
                            z = 1                        
                        elif textList[k]==searchFor:
                            testString = textList[k:i+1]
                            check = EOLcheckString(testString)
                            if check=='Unbalanced':
                                unbalancedRowChars = ch
                                u = 1
                                z = 1
                            else:                       
                                del textList[k:i+1]
                                i = k 
                                z = 1

                        else:
                            k += -1
            else:
                i += 1
        return textList
    figMatches = {'(':')', '[': ']', '{':'}','<':'>'}
    figScore = {')':1, ']': 2, '}':3,'>':4}
    scoreList = []
    for item in cleanLines:
        startLines = check2(item)
        newEnd = []
        for s in startLines:
            newChar = figMatches[s]
            newEnd.append(newChar)
        newEnd.reverse()
        s = 0
        for j in newEnd:
            s *= 5
            s += figScore[j]
        scoreList.append(s)
    return np.median(scoreList)   

print(day10p2(sampleTextInput))

real10 = day10p2(fileContents)
print(real10)


