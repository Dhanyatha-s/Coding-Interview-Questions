# Coding-Interview-Questions-

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

