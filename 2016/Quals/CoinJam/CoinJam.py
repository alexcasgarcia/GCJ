def generateJamcoins(J,N):
    jamcoin=[1]+[0 for x in xrange(N-2)]+[1]
    resultSet=[]
    i=0
    while i<N:
        
    print jamcoin

def isJamcoin(jamcoin):
    b=2
    while b<=10:
        b10number=0
        for i in xrange(len(jamcoin)):
            b10number+=jamcoin[i]*(b**i)
        if not isNotPrime(b10number):
            return False
        b+=1
    return True

def isNotPrime(n):
    i=2
    while i<n:
        if n%i==0:
            return True
        i+=1
    return False

print isJamcoin([1,0,0,0,1,1])
generateJamcoins(6,3)
generateJamcoins(6,7)
generateJamcoins(6,4)
