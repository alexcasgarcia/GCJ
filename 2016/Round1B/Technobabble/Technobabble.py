def createMap(strings):
    leftMap={}
    rightMap={}
    for string in strings:
        stringList=string.split()
        if leftMap.get(stringList[0]) is None:
            leftMap[stringList[0]]=[stringList[1]]
        else:
            leftMap[stringList[0]].append(stringList[1])

        if rightMap.get(stringList[1]) is None:
            rightMap[stringList[1]]=[stringList[0]]
        else:
            rightMap[stringList[1]].append(stringList[0])
    print (leftMap,rightMap)

def missingLinks(maps):
    for key in maps[0]:
        for value in maps[0][key]:
            



strings=['HYDROCARBON COMBUSTION', 'QUAIL BEHAVIOR', 'QUAIL COMBUSTION']
createMap(strings)
