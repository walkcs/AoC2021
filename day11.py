from os import urandom
import numpy as np

s1 = '''
11111
19991
19191
19991
11111'''

sampleIn = '''
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''

realIn = '''
4438624262
6263251864
2618812434
2134264565
1815131247
2612457325
8585767584
7217134556
2825456563
8248473584'''

def day11p1(textIn, steps):
    l = textIn.split()
    b = []
    for item in l:
        b.append([int(char) for char in item])
    a = np.array(b)

    flashCount = 0
    for s in range(steps):
        if s==0:
            newA = np.copy(a) + 1
        else:
            newA = np.copy(newA) + 1

        newAc = np.copy(newA)
        countNines = np.count_nonzero(newA > 9)
        flashedYet = newA==True
        oppFY = flashedYet==False
        nineMask = newA > 9
        comboMask = nineMask[oppFY]
        countNines = np.count_nonzero(comboMask)

        while countNines>0:
            for r,row in enumerate(b):
                for c,col in enumerate(row):
                    if flashedYet[r,c] == False and newA[r,c]>9:
                        flashCount += 1
                        index = [r,c]
                        left = max(0,index[0]-1)
                        right = max(0,index[0]+1+1)

                        bottom = max(0,index[1]-1)
                        top = max(0,index[1]+1+1)
                        newAc[left:right,bottom:top] += 1
                        flashedYet[r,c] = True

            newA = np.copy(newAc)
            oppFY = flashedYet==False
            nineMask = newA > 9
            comboMask = nineMask[oppFY]
            countNines = np.count_nonzero(comboMask)

        
        newA = np.where(newA > 9, 0, newA)


    return flashCount

print(day11p1(sampleIn, 100))
print(day11p1(realIn, 100))

def day11p2(textIn):
    l = textIn.split()
    b = []
    for item in l:
        b.append([int(char) for char in item])
    a = np.array(b)
    x,y = a.shape

    q = 0
    s = 0
    flashCount = 0
    while q==0:
        if s==0:
            newA = np.copy(a) + 1
        else:
            newA = np.copy(newA) + 1

        newAc = np.copy(newA)
        countNines = np.count_nonzero(newA > 9)
        flashedYet = newA==True
        oppFY = flashedYet==False
        nineMask = newA > 9
        comboMask = nineMask[oppFY]
        countNines = np.count_nonzero(comboMask)

        while countNines>0:
            for r,row in enumerate(b):
                for c,col in enumerate(row):
                    if flashedYet[r,c] == False and newA[r,c]>9:
                        flashCount += 1
                        index = [r,c]
                        left = max(0,index[0]-1)
                        right = max(0,index[0]+1+1)

                        bottom = max(0,index[1]-1)
                        top = max(0,index[1]+1+1)
                        newAc[left:right,bottom:top] += 1
                        flashedYet[r,c] = True

            newA = np.copy(newAc)
            oppFY = flashedYet==False
            nineMask = newA > 9
            comboMask = nineMask[oppFY]
            countNines = np.count_nonzero(comboMask)

        if np.count_nonzero(newA > 9)==x*y:
            w = s + 1
            q = 1
        else:
            newA = np.where(newA > 9, 0, newA)
            s += 1


    return w

print(day11p2(sampleIn))
print(day11p2(realIn))