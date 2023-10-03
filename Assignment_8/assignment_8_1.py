class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous

class LinkedList:
    def __init__(self):
        self._first=None

    def append(self, value):
        if self._first==None: # list is empty
            self._first=Node(value)
        else: # add to the end of a non-empty list
            n=self._first
            while n._next:
                n=n._next
            n._next=Node(value, previous=n)

    def info(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
            n=n._next
        str+=")"
        return str

    def size(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c
            
    def get(list,index):
        n=list._first
        for i in range(index):
            n=n._next
            if n==None:
                break
        else:
            return n._value
        
    def insert(list, index, value):
        temp = list._first
        count = 0
        while temp is not None:
            if count == index - 1:
                break
            count += 1
            temp = temp._next
        if index == 0:
            new_node = Node(value)
            if list is None:
                list._first = new_node
            else:
                new_node._next = list._first
                list._first._previous = new_node
                list._first = new_node
        elif temp is None:
            print(f"There are less than {index}-1 elements in the linked list. Cannot insert at {index} position.")
        elif temp._next is None:
            new_node = Node(value)
            temp = list._first
            while temp._next is not None:
                temp = temp._next
            temp._next = new_node
            new_node._previous = temp
        else:
            new_node = Node(value)
            new_node._next = temp._next
            new_node._previous = temp
            temp._next._previous = new_node
            temp._next = new_node

    def remove(list, index):
        if list is None:
            print("Linked List is empty. Cannot delete elements.")
        elif index == 1:
            if list._first is None:
                print("Linked List is empty. Cannot delete elements.")
            elif list._first._next is None:
                list._first = None
            else:
                list._first = list._first._next
                list._first._previous = None
        else:
            temp = list._first
            count = 1
            while temp is not None:
                if count == index:
                    break
                temp = temp._next
            if temp is None:
                print(f"There are less than {index} elements in linked list. Cannot delete element.")
            elif temp._next is None:
                if list is None:
                    print("Linked List is empty. Cannot delete elements.")
                elif list._first._next is None:
                    list._first = None
                else:
                    temp = list._first
                    while temp._next is not None:
                        temp = temp._next
                    temp._previous._next = None
                    temp._previous = None
                temp._previous._next = temp._next
                temp._next._previous = temp._previous
                temp._next = None
                temp._previous = None

    def clear(self):
        temp = self._first
        while temp!= None:
            self.remove(0)
            temp = temp.next

l1 = LinkedList()

print(l1.info())

for value in [2,3,9,2,6]:
    l1.append(value)

print('size', l1.size())

print(l1.info())

l1.insert(2,154)
l1.insert(0,25)

print(l1.info())

l1.remove(0)
print(l1.info())