"""Taken from https://uva.onlinejudge.org/"""
import sys
from Candidate import Candidate
#Method for reading input
def dataload():
    #Plain data file
    data = open("Data.txt", "r")
    
    #Used data structures
    candidateSet = {}
    balotSet = {}
    
    cases = int(data.readline())
    i = 0
    while(i < cases):
        candidates = int(data.readline())
        j = 0
        
        #Fill candidates set
        while(j < candidates):
            candidateSet[j+1] = Candidate(data.readline())
            balotSet[j] = list()
            j +=1
        j = 0
        balot = data.readline()
        
        #Fill balots set
        while(balot != '-'):
            while(j < candidates):
                balotSet[j].append(balot.split(" ")[j])
                j+=1
            j = 0
            balot = data.readline()
        i +=1 
        
        #Balots set to balot queue
        balotsQueue = list()
        for x in range(0,candidates):
            balotsQueue = balotSet[x] + balotsQueue
    return candidateSet, balotsQueue

def countVotes():
    candidateSet, balotsQueue = dataload()
    votesAmount = len(balotsQueue)/len(candidateSet)
    winner = None
    while(len(balotsQueue) != 0):
        print("-------------------")
        for j in range(0,votesAmount):
            candidate = int(balotsQueue.pop())
            candidateSet[candidate].increaseCount()
        winner = findWinner(votesAmount, candidateSet)
        if(winner.getName() != ""):
           break

def findWinner(votesAmount, candidateSet):
    c = Candidate("")
    candidateAmount = len(candidateSet)
    maxVotes = 0
    minVotes = 2000000
    for i in range(0,candidateAmount):
        currentCandidate = candidateSet[i+1]
        candidateVotes = currentCandidate.getCount()
        if(candidateVotes/votesAmount > 0.5):
            c = currentCandidate
            break
        if(candidateVotes < minVotes):
            minVotes = candidateVotes
        if(candidateVotes > maxVotes):
            maxVotes = candidateVotes
    print(minVotes)
    print(maxVotes)
    if(minVotes != maxVotes):
            cleanSet(minVotes, candidateSet)
    return c

def cleanSet(minVotes, candidateSet):
    size = len(candidateSet)
    for i in range(0,size):
        currentCandidate = candidateSet[i+1]
        if(currentCandidate.getCount() == minVotes):
            candidateSet.pop(i+1)
countVotes()
