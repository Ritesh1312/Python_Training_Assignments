n = int(input("Enter the number of values : "))
largest = float('-inf')
for i in range(n):
    num = int(input(f"Enter Numbers {i+1} : "))
    
    if largest == float('-inf') or num > largest:
        largest  = num
print("The Largest no is : ", largest)