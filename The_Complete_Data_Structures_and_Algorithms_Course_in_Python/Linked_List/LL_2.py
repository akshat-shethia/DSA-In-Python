class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self) -> str:
        temp = self.head
        result = ""
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += " -> "
            temp = temp.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        
    def insert(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(position-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1
        
    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


new_linked_list = LinkedList()
new_linked_list.append(1)
new_linked_list.append(2)
new_linked_list.append(3)
new_linked_list.append(4)
new_linked_list.append(5)
new_linked_list.prepend(70)
new_linked_list.insert(90, 2)
new_linked_list.traverse()

# print(f"The length of the Linked List is now -----> {new_linked_list.length}")
print(new_linked_list)
