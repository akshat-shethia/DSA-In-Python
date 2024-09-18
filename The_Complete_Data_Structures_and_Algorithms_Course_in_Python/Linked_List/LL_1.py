class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
# new_node = Node(14)
# print(new_node)

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
new_linked_list = LinkedList(14)
print(new_linked_list.head.value) 

