#n by n grid
#each cell a certain height
#within every row, strictly increasing left to right
#within every column, strictly increasing top to bottom
#no two soldiers within the same row or column may share the same height

def readFile(inputFile):
    f=open(inputFile)
    testCases=int(f.readline().strip('\n'))
    for i in xrange(testCases):
        numberRows=int(f.readline().strip('\n'))
        inputArray=[]
        for j in xrange(numberRows*2-1):
            inputArray.append(map(int,f.readline().strip('\n').split()))
        findMissingRow(inputArray)
        print

def findMissingRow(inputArray):
    print inputArray
    n=len(inputArray[0])
    i=0
    while i<2*n-1:
        j=0
        while j<2*n-1:
            if j!=i:
                print intersection(inputArray[i],inputArray[j])
            i+=1

def intersection(a1,a2):
    sideLength=len(a1)
    i=0
    foundMatch=False
    while i<sideLength:
        j=0
        while j<sideLength:
            if a1[i]==a2[j]:
                foundMatch=True
                break
            j+=1
        if foundMatch:
            break
        i+=1
    if foundMatch!=True:
        return -1
    else:
        outputArray=[]
        for y in xrange(sideLength):
            outputRow=[]
            for x in xrange(sideLength):
                if y==j:
                    outputRow.append(a1[x])
                elif x==i:
                    outputRow.append(a2[y])
                else:
                    outputRow.append('')
            outputArray.append(outputRow)
        return outputArray

def completeMatrix(matrix,array):
    sideLength=len(array)
    for i in xrange(sideLength):
        for j in xrange(sideLength):
            if matrix[i][j]=='':
                    
                
                
                
       

print "--Running Test--"
readFile('input.txt')
    
            
