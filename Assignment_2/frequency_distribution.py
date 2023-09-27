def frequency_distribution(sequence):
    frequency = {}

    for value in sequence:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    return frequency

lst = [2,2,9,1,2,2,1,4,2,2,3,1]
result = frequency_distribution(lst)
print(result)


# lst = []
# n = int(input("total numbers ? "))
# for i in range (n):
#     lst[i] = int(input(f'enter number #{i+1} '))

# seq = [1,1,1,1,1,-1,0,-2,-1]
# dict={}
# i = 0
# count = 0
# while i < len(seq):
#     if(seq[i] in dict):
#         count += 1
#         dict.update({seq[i]:count})
#     else:
#         dict[seq[i]] = 1
#         count = 1
#     i+=1
# print(dict)