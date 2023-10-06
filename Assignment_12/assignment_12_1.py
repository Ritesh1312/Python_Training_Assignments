import time

def cached(func):
    factorial_cache = {}
    def inner(*args, **kwargs):
        if args not in factorial_cache:
            result = func(*args, **kwargs)
            factorial_cache[args] = result
            return result
        else:
            print("Result returned from Cache")
            return factorial_cache[args]
    return inner

def performance_log(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(0.1)
        returned_value = func(*args, **kwargs)
        end = time.time()
        print(f'Time taken to execute = {end - start}')
        return returned_value
     
    return inner


@cached
@performance_log
def factorial(num):
    fn = 1
    for x in range(1, num+1):
        fn *= x
    return fn

f1 = factorial(5)
print(f1)
f1 = factorial(18)
print(f1)
f1 = factorial(5)
print(f1)
f1 = factorial(18)
print(f1)
f1 = factorial(24)
print(f1)
