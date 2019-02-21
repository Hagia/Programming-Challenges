"""Taken from https://uva.onlinejudge.org/"""
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
            candidateSet[j] = data.readline()
            balotSet[j] = list()
            j +=1
        j = 0
        balot = data.readline()
        
        #Fill balots set
        while(balot != '-'):
            while(j < candidates):
                balotSet[j].append(balot.split()[j])
                j+=1
            j = 0
            balot = data.readline()
        i +=1 
        
        #Balots set to balot queue
        balotsQueue = list()
        for x in range(0,candidates):
            balotsQueue = balotsQueue + balotSet[x]
    print(candidateSet)
    print(balotSet)

dataload()
