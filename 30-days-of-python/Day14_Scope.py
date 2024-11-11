class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = self.computeDifference()
    
    def computeDifference(self):
        diff = []
        sortedArray = sorted(a)
        maxDiff = abs(sortedArray[0] - sortedArray[len(a)-1])
        return maxDiff
        
        
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
