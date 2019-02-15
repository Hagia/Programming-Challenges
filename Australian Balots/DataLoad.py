def dataload():
    data = open("Data.txt", "r")  
    candidateSet = {}
    dataSet = {}
    cases = int(data.readline())
    i = 0
    while(i < cases):
        candidates = int(data.readline())
        j = 0
        while(j < candidates):
            candidateSet[j] = data.readline()
            dataSet[j] = list()
            j +=1
        j = 0
        balot = data.readline()
        while(balot != '-'):
            while(j < candidates):
                dataSet[j].append(balot.split()[j])
                j+=1
            j = 0
            balot = data.readline()
        i +=1 
    print(candidateSet)
    print(dataSet)

dataload()