import time
import math
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.end = time.time()
        self.time_taken = self.end - self.start


def find_primes(min,max):
    primes=[]
    for x in range(min,max):
        if is_prime(x):
            primes.append(x)
    return primes

def is_prime(n):
    if n<2:
        return False
    for x in range(2,int(math.sqrt(n))+1):
        if n%x==0:
            return False
    return True

with Timer() as t:
    prime = find_primes(2,500000)
    print(f'Total Primes are - {len(prime)}')

print(f'Total Time Taken - {t.time_taken}')