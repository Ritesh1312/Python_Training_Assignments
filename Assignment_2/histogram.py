def frequency_distribution(sequence):
    frequency = {}

    for value in sequence:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    return frequency

def print_histogram(result):
    result = frequency_distribution(lst)
    for key,value in result.items():
        print(f' {key} | ', end = '')
        i = 0
        while i < value:
            print(f'==',end='')
            i += 1
        print(' ',value)

lst = [2,2,9,1,2,2,1,4,2,2,3,1]
result = frequency_distribution(lst)
print_histogram(result) 