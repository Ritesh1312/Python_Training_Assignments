from Linked_list import LinkedList

def main():
    list = LinkedList()
    list.append(10)
    list.append(1)
    list.append(21)
    list.append(11)
    list.append(3)
    list.append(78)

    print(f'Value of element present at index {3}: {list.get_value(3)}')

    print("Inserting at specific indexes")

    list.insert_at_position(700, 1)
    list.info()
    list.insert_at_position(38, 4)
    list.insert_at_position(457, 0)

    list.info()
    
    print()

    print('Removing elements from list at particular indexes')
    list.remove_at_index(0)
    list.remove_at_index(3)
    list.size()
    

    list.info()

    list.clear()
    list.info()

if(__name__=='__main__'):
    main()

