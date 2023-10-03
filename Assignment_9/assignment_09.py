
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.next != None:
                temp_node = temp_node.next
            temp_node.next = new_node
        
    def clear(self):
        temp = self.head
        while temp!= None:
            self.remove_at_index(0)
            temp = temp.next


    def insert_at_position(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0

        if position == index:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return
            else:
                new_node.next = self.head
                self.head = new_node

        else:

            while( current_node != None and position+1 != index):
                position +=1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print(" Index Not Available ")

    def remove_at_index(self, index):
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            if(self.head == None):
                return
            self.head = self.head.next
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    def get_value(self, index):
        new_node = self.get(index)
        if(new_node):
            return new_node.data

    def get(self, index):
        temp_node = self.head
        count = 0
        while temp_node != None:
            if(count==index):
                return temp_node
            count+=1
            temp_node = temp_node.next
        return Node(None)

    def set_value(self, data, index):
        new_node = self.get(index)
        if(isinstance(new_node, Node)):
            new_node.data = data

    def size(self):
        temp_node = self.head
        count = 0

        while temp_node != None:
            temp_node = temp_node.next
            count+=1
        print( f" Size = {count}" ) 
    
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def info(self):
        print('List elements : ', end='')
        self.print_list()
        print(f'\nSize {self.size()}')

    def clear(self):
        self.head=None

    def check_prime(self,num):
        if num <= 1:
            return False
        for i in range(2, num//2):
            if num % i == 0:
                return False
        return True

    def find_primes(self):
        temp = self.head
        while temp != None:
            if self.check_prime(temp.data):
                print(temp.data)
            temp = temp.next

    def find_evens(self):
        temp = self.head
        while temp != None:
            if temp.data % 2 == 0:
                print(temp.data)
            temp = temp.next

    



