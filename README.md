# Coding-Interview-Questions-
| Questions | Asked in |
|------------|-----------|
|Flip binary Numbers| IBM|
|In-Order-Traverse| none |
| Revese list in group of given size | Sigmoid |
| String Compressor| IBM|
|Count the Absolute Difference| Accenture|

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

### Bonus #1
> Perform Curd Operation in python or create a TO-DO List
```
user_input = 'List'
data = []

def show_menu():
    print('1. Add Item')
    print('2. Mark as Done')
    print('3. View to do List')
    print('4. Exit')



while user_input != '4':

    show_menu()
    user_input = input("Enter  your Choice: ")

    if user_input == '1':
        item = input('What is to be done?: ')
        data.append(item)
        print("Added Item")
    elif user_input == '2':

        item = input("What is to be marked as done: ")
        if item in data:
            data.remove(item)
            print("Item Removed", item)
        else:
            print('Item is not in the list')

    elif user_input == '3':
        for item in data:
            print(item)
            
    elif user_input == '4':
        print("Goodbye")
    else:
        print("Please enter 1, 2, 3 or 4")
```
### Question 4
>Consider a string S that is a series of characters, each followed by its frequency as an integer. The string is not compressed correctly, so there may be multiple occurrences of the same character. A properly compressed string will consist of one instance of each character in alphabetical order, followed by the total count of the characters within the string.  
>input s = 'a2b3a1c2n1c4'  
>output  = 'a3b3c6n1'


```
class stringCompressor:
    def __init__(self, s):
        self.s = s

    def compres(self):
        
        from collections import defaultdict

        chat_count = defaultdict(int)
        
        # instace of char
        i = 0

        # Total len of string
        n= len(self.s)

        while i<n:
            char = self.s[i]
            i +=1
            freq_start = i

            while i < n and self.s[i].isdigit():
                i+=1
                freq = int(self.s[freq_start: i])
                chat_count[char] += freq

        return ''.join(f"{char}{chat_count[char]}" for char in sorted(chat_count))

s = 'a2b3a1c2n1c4'
compressor = stringCompressor(s)
result = compressor.compres()
print(result)
````
### Question 5
>> ### find the Absolute diffrence from the array of integer, has num of array and difference,  if empty array return -1 and if absolute diffrence when num is <= difference
#### input :  12, 3, 14 ,56, 77, 13
#### num : 13
#### diff : 2
#### Output : 3
```
>> 
def find_count():
    arr = [12, 3, 14 ,56, 77, 13]
    num = 13
    diff = 2
    count = 0

    
    if len(arr) == 0:
            return -1
    
    for i in arr:
        abs_diff = abs(i - num)
        if abs_diff <= diff:
            count +=1
            # print(count)
    return count

result = find_count()
print(f'the count of absolute difference are {result}')
```

