def check(num):
    if num <= 1:
        return False
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

min_num = int(input("Enter the minimum number: "))
max_num = int(input("Enter the maximum number: "))

print(f"Prime numbers between {min_num} and {max_num}:")
for number in range(min_num, max_num + 1):
    if check(number):
        print(number)