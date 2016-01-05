#!/usr/bin/python
import time

def adjacentLetters(filename):
    with open(filename, "r") as inputFile:
        adjMat = [[0.0]*26 for i in range(26)]
        divisor = [0.0]*26
        for line in inputFile:
            for word in line.upper().split(' '):
                for i in range(len(word)-1):
                    cur = ord(word[i])-65
                    nex = ord(word[i+1])-65
                    if (cur < 26 and nex < 26 and cur > -1 and nex > -1):
                        divisor[cur] += 1
                        adjMat[cur][nex] += 1
        for i in range(26):
            for j in range(26):
                if divisor[i] != 0:
                    adjMat[i][j] = adjMat[i][j] / divisor[i]
    return adjMat

adjMat = adjacentLetters("TheOdyssey.txt")

def generateScore(adjMat):
    lineScore = 0;
    with open("poetry.txt", "r") as inputFile:
        for lines in inputFile:
            lineChars = list(lines.upper())
            for i in range(len(lineChars)-2):
                if(ord(lineChars[i]) and ord(lineChars[i+1]) >= 65):
                    print ord(lineChars[i+1])-65
                    lineScore = lineScore + adjMat[ord(lineChars[i])-65][ord(lineChars[i+1])-65]
adjMat = adjacentLetters("TheOdyssey.txt")
print generateScore(adjMat)