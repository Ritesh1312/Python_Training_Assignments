from assignment_09 import LinkedList

def main():
    list = LinkedList()

    list.append(10)
    list.append(1)
    list.append(21)
    list.append(11)
    list.append(3)
    list.append(78)
    list.append(13)
    list.append(3)
    list.append(79)
    
    list.find_primes()
    print()
    list.find_evens()
    print()
    list.clear()
    print()
    list.info()

if(__name__=='__main__'):
    main()
