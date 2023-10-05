import time
import math


def decorator(func):
    def inner(*args, **kwargs):
        start = time.time()
        returned_value = func(*args, **kwargs)
        end = time.time()
        print(f'Time taken to execute = {end - start}')
        return returned_value
     
    return inner
    
@decorator
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


x=find_primes(1,100000)

print(len(x))   
