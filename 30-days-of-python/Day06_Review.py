import sys

inList = []

for each in sys.stdin:
    inList.append(each.replace("\n", ""))

T = int(inList[0])

for ind in range(1, len(inList)):
    evenList = []
    oddList = []
    string = inList[ind]
    for i in range(0,len(string)):
        if i % 2 == 0:
            evenList.append(string[i])
        else:
            oddList.append(string[i])
    
    evenStr = "".join(evenList)
    oddStr = "".join(oddList)
    print(evenStr + " "+ oddStr)
