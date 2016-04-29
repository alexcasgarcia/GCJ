def readFile(fileName):
    f = open(fileName)
    w = open(fileName.strip('.in')+'.out','w')
    i=0
    for line in f:
        line=line.strip('\n')
        if i==0:
            testCases=int(line)
        else:
            word=findWinningLastWord(line)
            print>>w, "Case #%s: %s" % (i,word)
        i+=1
    f.close()

def findWinningLastWord(word):
    lastWord=''
    for x in word:
        if len(lastWord)==0:
            lastWord+=x
        else:
            prepend=x+lastWord
            append=lastWord+x
            if append>prepend:
                lastWord=append
            else:
                lastWord=prepend
    return lastWord

print findWinningLastWord('HORSE')

print "Solving small file"
readFile('A-small-practice.in')
print "Solving large file"
readFile('A-large-practice.in')
