def firstNumberIndex(string):
    firstNumberIndex=0
    for i in xrange(len(string)):
        if string[i]!='?':
            return i

    return 0

def stripTrailingZeros(str1,str2):
    index=min(firstNumberIndex(str1),firstNumberIndex(str2))
    return (str1[index:],str2[index:],index)

def minimizeScore(str1,str2,pad,case):
    output=([],[])
    for x in xrange(pad):
        output[0].append(0)
        output[1].append(0)
        
    strLen=len(str1)
    str1str2Comparison='UNKNOWN'
    for x in xrange(strLen):
        d1=str1[x:x+1]
        d2=str2[x:x+1]
        if d1!='?' and d2!='?':
            if str1str2Comparison=='UNKNOWN':
                if int(d1)>int(d2):
                    str1str2Comparison='GREATER'
                    output[0].append(int(d1))
                    output[1].append(int(d2))
                elif int(d1)<int(d2):
                    str1str2Comparison='LESS'
                    output[0].append(int(d1))
                    output[1].append(int(d2))
        elif d1=='?' and d2!='?':
            output[1].append(int(d2))
            if str1str2Comparison=='UNKNOWN':
                output[0].append(int(d2))
            elif str1str2Comparison=='GREATER':
                output[0].append(0)
            elif str1str2Comparison=='LESS':
                output[0].append(9)
        elif d1!='?' and d2=='?':
            output[0].append(int(d1))
            if str1str2Comparison=='UNKNOWN':
                output[1].append(int(d1))
            elif str1str2Comparison=='GREATER':
                output[1].append(9)
            elif str1str2Comparison=='LESS':
                output[1].append(0)
        elif d1=='?' and d2=='?':
            if str1str2Comparison=='UNKNOWN':
                output[0].append(0)
                output[1].append(0)
            elif str1str2Comparison=='GREATER':
                output[0].append(0)
                output[1].append(9)
            elif str1str2Comparison=='LESS':
                output[0].append(9)
                output[1].append(0)
        else:
            print 'UNEXPECTED'

    return (case,''.join(map(str,output[0])),''.join(map(str,output[1])))

def main(str1,str2,case):
    stripped=stripTrailingZeros(str1,str2)
    answerTuple=minimizeScore(stripped[0],stripped[1],stripped[2],case)
    print "Case #%s: %s %s" % answerTuple

def readFile(fileName):
    f=open(fileName)
    i=0
    for line in f:
        strings=line.split()
        if i>0:
            main(strings[0],strings[1],i)
        i+=1
        
readFile('B-small-attempt0.in')            
                
                


    
