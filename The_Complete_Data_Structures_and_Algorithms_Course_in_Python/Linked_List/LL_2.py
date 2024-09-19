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

    def search(self, value):
        curr = self.head
        flag = False
        while curr:
            if curr.value == value:
                flag = True
            curr = curr.next
        print(flag)

    def get(self, index):

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index < -1 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == -1 or index == self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node


new_linked_list = LinkedList()
new_linked_list.append(1)
new_linked_list.append(2)
new_linked_list.append(3)
new_linked_list.append(4)
new_linked_list.append(5)
new_linked_list.prepend(70)
new_linked_list.insert(90, 2)
new_linked_list.traverse()
new_linked_list.search(4)
print(new_linked_list.get(4))

# print(f"The length of the Linked List is now -----> {new_linked_list.length}")
print(new_linked_list)
