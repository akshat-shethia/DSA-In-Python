class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        

new_linked_list = LinkedList()
new_linked_list.append(1)
new_linked_list.append(2)
new_linked_list.append(3)
new_linked_list.append(4)
new_linked_list.append(5)

print(f"The length of the Linked List is now -----> {new_linked_list.length}")
        