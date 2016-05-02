def getDigits(string):
    print string
    ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letterMap={}
    for letter in ALPHABET:
        letterMap[letter]=0
    
    for letter in string:
        letterMap[letter]+=1

    phoneNumber=[]
    letterToNumberMap={'Z':0,'W':2,'U':4,'X':6,'G':8,'ONE':1,'THREE':3,'SEVEN':7,'NINE':9,'TEN':10,'FIVE':5}
    letterRemovalMap={'Z':'ZERO','W':'TWO','U':'FOUR','X':'SIX','G':'EIGHT'}
    
    for index in letterToNumberMap:
        if len(index)==1:
            for x in xrange(letterMap[index]):
                phoneNumber.append(letterToNumberMap[index])
                letterRemovalList=letterRemovalMap[index]
                print letterMap
                for letter in letterRemovalList:
                    letterMap[letter]-=1
                    print letterMap
        elif len(index)>100:
            indices=[x for x in index]
            num=min(letterMap[index1],letterMap[index2])
            for x in xrange(num):
                phoneNumber.append(letterToNumberMap[index])

    phoneNumber.sort()
    print phoneNumber


getDigits('ZWUXGZWONVFTNINVNHR')
    
