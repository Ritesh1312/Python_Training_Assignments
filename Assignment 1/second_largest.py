n = int(input("Enter the number of values : "))
largest = float('-inf')
second_largest = float('-inf')
for i in range(n):

    num = int(input(f"Enter Numbers {i+1} : "))
    
    if (num > largest):
        second_largest = largest
        largest = num
        
    elif num > second_largest and num!=largest:
        second_largest = num
        

print("The 2nd Largest no is : ", second_largest)