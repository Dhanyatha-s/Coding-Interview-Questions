# Coding-Interview-Questions-
| Questions | Asked in |
|------------|-----------|
|Flip binary Numbers| IBM|
|In-Order-Traverse| none |
| Revese list in group of given size | Sigmoid |

### Question 1 Asked in IBM Software Developer Assessment 

> A password string, PWT, consists of binary characters 0s and 1s. A cybersecurity expert is trying to determine the minimum number of changes required to make the password secure. To do so, it must be divided into substrings of non-overlapping, even length strings. Each substring can only contain 1s or 0s, not a mix. This helps to ensure that the password is strong and less vulnerable to hacking attacks. Find the minimum number of characters that must be flipped in the password string, i.e., changed from 0s to 1s or 1s to 0s, to allow the string to be divided as described.
```
class PasswordSecurity:
    def __init__(self, PWT):
        self.PWT = PWT

    def min_flips_to_secure(self):
        flips = 0

        # Process the string in pairs
        for i in range(0, len(self.PWT) - 1, 2):
            if self.PWT[i] != self.PWT[i + 1]:
                flips += 1

        return flips

# Example usage:
password = "011001"
security = PasswordSecurity(password)
print(security.min_flips_to_secure())  # Output: 3

```

### Question 2
>Perform an in-order traversal of a binary tree on given list   
>[1,2,3,4,5] to [4 -> 2-> 5 -> 1 -> 3]    
      1  
     / \  
    2   3  
   / \  
  4   5  
```
class TreeNode:
    def __init__(self, val=0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order_traversal(root):
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
    traverse(root)
    return result
    

#construct root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

output = in_order_traversal(root)
print("In-Order Traversal:", output)

```
### Question 3
> Reverse a linked list in group of given size  
>input 1 -> 2 -> 3 -> 4-> 5-> 6 -> 7 -> 8 -> 9  
> k = 3  
> output  3 -> 2 -> 1 -> 6-> 5-> 4 -> 9 -> 8 -> 7  
``` class Node:
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

```





