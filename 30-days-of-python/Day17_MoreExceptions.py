#class e(Exception):
#    def __init__(self):
#        Exception.__init__(self, "n and p should be non-negative")

class Calculator():
    def power(self,n,p):
        self.n = n
        self.p = p
        if n<0 or p<0:
            raise Exception ("n and p should be non-negative")
        else:
            return n**p
