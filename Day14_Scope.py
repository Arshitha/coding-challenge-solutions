class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = self.computeDifference()
    
    def computeDifference(self):
        diff = []
        for i in range(0, len(a)-1):
            for j in range(i+1,len(a)):
                diff.append(abs(a[i]-a[j]))
        diff = sorted(diff)
        return diff[len(diff)-1]
        
        
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
