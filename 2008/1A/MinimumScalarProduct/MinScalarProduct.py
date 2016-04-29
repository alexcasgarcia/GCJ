def MinScalarProduct(vector1,vector2,case):
    vector1.sort(reverse=False)
    vector2.sort(reverse=True)
    scalarProduct=0
    i=0
    while i<len(vector1):
        scalarProduct+=vector1[i]*vector2[i]
        i+=1
    return "Case #"+str(case)+": "+str(scalarProduct)+"\n"

def readTestFile(inputFile,outputFile):
    r = open(outputFile, 'w')
    with open(inputFile) as f:
        i=0
        n=1
        vector1=[]
        vector2=[]
        for line in f:
            if i==0:
                NumberOfRecords=int(line)
            else:
                if (i+2)%3==0:
                    vectorLength=int(line.strip('\n'))
                else:
                    textInput=line.strip('\n')
                    stringList=textInput.split()
                    integerList=[int(x) for x in stringList]
                    if (i+1)%3==0:
                        vector1=integerList
                    else:
                        vector2=integerList
                        r.write(MinScalarProduct(vector1,vector2,i/3))
                n+=1
            i+=1  

readTestFile('in/minscalarproduct.in','out/minscalarproduct.out')
