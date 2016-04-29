import pdb
#5 (milkshake flavors)
#4 (customers)
#2 1 0 2 0 or 0 0 None None None 
#2 1 1 2 1 or 1 1 None None None
#2 1 0 2 1 or 1 0 None None None

#0 0
#1 1
#1 0
#0 1

#find 

# for a set of customers with the same # of preferences, figure out which the set of milkshakes that will satisfy them
# for each customer
## for each flavor
### compare flavor preference with all other customer's preference for that flavor
#### if match, set = None

#who is the pickiest customer?
##find min first number
def milkshakeMatch(milkshakeFlavorCount,customers,caseNumber):
    print milkshakeFlavorCount
    print customers
    print caseNumber
    # find the set of pickiest customers
    # if customer picks 1 milkshake
    ## compare his milkshake preference with all other customers
    ###if it conflicts with someone elses preference, remove the other persons preference, if they only have one preference, mark as impossible
    ###remove that customer from the list of customers to compare to
    # if customer can pick multiple milkshakes
    ## compare customer with customers with the same number of preferences 
    

    #method to remove a milkshake flavor from a customer

def readTestFile(fileName):
    r = open('milkshakes.out', 'w')
    with open(fileName) as f:
        pdb.set_trace()
        i=0
        customerNumber=0
        caseNumber=1
        customers=[]
        for line in f:
            line=[int(x) for x in line.strip('\n').split()]
            if i==0:
                testCaseCount=line[0]
            elif i==1:
                milkshakeFlavorCount=line[0]
            elif i==2:
                customerCount=line[0]
            else:
                customers.append(line)
                customerNumber+=1
                if customerCount==customerNumber:
                    milkshakeMatch(milkshakeFlavorCount,customers,caseNumber)
                    customerNumber=0
                    customers=[]
                    caseNumber+=1
                    i=0
            i+=1
    r.close()

readTestFile('milkshakes.in')




    

