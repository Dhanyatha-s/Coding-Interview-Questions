class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def reverse(self, head, k):
        if head is None:
            return None
        current = head
        next = None
        prev = None
        count = 0

        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            count +=1

        if next is not None:
            head.next = self.reverse(next, k)
        
        return prev
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end= " ")
            temp = temp.next


# construct linked list

list = linkedList()

list.push(9)
list.push(8)
list.push(7)
list.push(6)
list.push(5)
list.push(4)
list.push(3)
list.push(2)
list.push(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def reverse(self, head, k):
        if head is None:
            return None
        current = head
        next = None
        prev = None
        count = 0

        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reverse(next, k)

        return prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

# construct linked list
list = linkedList()

list.push(9)
list.push(8)
list.push(7)
list.push(6)
list.push(5)
list.push(4)
list.push(3)
list.push(2)
list.push(1)

print("Given list is")
list.printList()
list.head = list.reverse(list.head, 3)

print("\nReversed list")
list.printList()





