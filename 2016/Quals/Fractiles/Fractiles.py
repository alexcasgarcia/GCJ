def generateTileBase(n):
    tileBases=[]
    if n==1:
        return [[1],[0]]
    p1=generateTileBase(n-1)
    p2=generateTileBase(n-1)
    for x in p1:
        x.append(1)
    for x in p2:
        x.append(0)
    return p1+p2

def generateTileBase2(n,memo):
    tileBases=[]
    if n==1:
        return [[1],[0]]
    if n-1 in memo:
        p1=[[y for y in x] for x in memo[n-1]]
        p2=[[y for y in x] for x in memo[n-1]]
    else:
        p1=generateTileBase2(n-1,memo)
        p2=[[y for y in x] for x in p1]
        memo[n-1]=p2

    for x in p1:
        x.append(1)
    for x in p2:
        x.append(0)
    return p1+p2
print generateTileBase2(80,{})

def generateTilePattern(base,complexity):
    if complexity==1:
        return base
    pattern=[x for x in base]
    ones=[1 for x in xrange(len(base))]
    for i in xrange(complexity-1):
        finalPattern=[]
        for j in pattern:
            if j==0:
                finalPattern+=[x for x in base]
            if j==1:
                finalPattern+=[x for x in ones]
        pattern=[x for x in finalPattern]
    return finalPattern

def generateTiles(baseSize,complexity):
    bases=generateTileBase(baseSize)
    patterns=[]
    for x in bases:
        patterns.append(generateTilePattern(x,complexity))
    return patterns

def transpose(patterns):
    rows=len(patterns)
    columns=len(patterns[0])
    transposed=[[0 for x in xrange(rows)] for y in xrange(columns)]
    j=0
    while j < columns:
        i=0
        while i < rows:
            transposed[j][i]=patterns[i][j]
            i+=1
        j+=1

    return transposed

def numOnes(transposedPatterns):
    numOnes=[]
    for x in transposedPatterns:
        numOnes.append((sum(x),len(x)))
    return numOnes

def findIndex(numOnes,startIndex,difference):
    if startIndex>=len(numOnes):
        return "ERROR"
    i=startIndex
    while i < len(numOnes):
        if numOnes[i][1]-numOnes[i][0]==difference:
            return i
        i+=1
    return -1

def superposition(patterns):
    superposition=[]
    rows=len(patterns)
    columns=len(patterns[0])
    j=0
    while j < columns:
        i=0
        didAppend=False
        while i < rows:
            if patterns[i][j]==1 and not didAppend:
                superposition.append(1)
                didAppend=True
            i+=1
        if not didAppend:
            superposition.append(0)
        j+=1
    return superposition

def getCombinations(length,startIndex,students):
    if students==1:
        return [[startIndex]]
    i=startIndex
    allCombos=[]
    while i < length - students + 1:
        allCombos+=[[startIndex] + x for x in getCombinations(length,i+1,students-1)]
        i+=1
    return allCombos

def getFullCombinations(length,students):
    fullCombos=[]
    i=0
    while i < length - students + 1:
        fullCombos+=getCombinations(length,i,students)
        i+=1
    return fullCombos

def getSuperpositions(tPatterns,students):
    indices=[]
    p=[]
    i=0
    while i < len(tPatterns):
        if sum(tPatterns[i])==len(tPatterns[i])-students:
            indices.append(i)
            p.append(tPatterns[i])
        i+=1
    allCombos=getFullCombinations(len(indices),students)
    for x in allCombos:
        superPatterns=[]
        superPatternsIndices=[]
        for y in x:
            superPatterns.append(p[y])
            superPatternsIndices.append(indices[y])
        superPattern=superposition(superPatterns)
        if sum(superPattern)==len(superPattern)-1:
            return superPatternsIndices
    return [-1]
    
def numCleanTiles(base,complexity,students,case):
    print "Generating tiles"
    patterns=generateTiles(base,complexity)
    print "Transposing"
    tPatterns=transpose(patterns)
    i=1
    superposition=[]
    while i<=students:
        print "Getting superpositions"
        superposition=getSuperpositions(tPatterns,i)
        if -1 not in superposition:
            return "Case #"+str(case)+": "+' '.join([str(s) for s in superposition])+"\n"
        i+=1
    return "Case #"+str(case)+": IMPOSSIBLE\n"


def readTestFile(fileName):
    r = open('fractiles.out', 'w')
    with open(fileName) as f:
        i=0
        for line in f:
            if i==0:
                NumberOfRecords=int(line)
            else:
                textInput=line.strip('\n')
                print textInput
                integerInput=[int(x) for x in textInput.split()]
                r.write(numCleanTiles(integerInput[0],integerInput[1],integerInput[2],i))
            i+=1  
    r.close()
           
            
#readTestFile('fractiles.in')
