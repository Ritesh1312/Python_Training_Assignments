
from math import sqrt
def check_prime(num):
    if(num==1):
        return False
    for x in range(2,int(sqrt(num))+1):
        if(num%x==0):
            return False
    return True

class Prime_number_Iterator:
    def __init__(self, start, end=None):
        if end == None:
            self.x = 1
            self.y = start
        else:
            self.x = start
            self.y = end

    def __iter__(self):
        self.n = self.x -1
        return self

    def __next__(self):
        if self.n <= self.y:
            self.n += 1
            while not check_prime(self.n):
                self.n += 1
                if self.n > self.y:
                        raise StopIteration
            else:
                return self.n
        else:
            raise StopIteration

a = iter(Prime_number_Iterator(1000,100000))

for x in a:
    print(x)