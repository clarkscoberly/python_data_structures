"""
Now that Carly has picked out a baby name - Bary - she recognizes that someone
has not added her own parents to her tree and decides to do so herself. Add both of her
parents Kary and Harry.
"""

class BST:

    class Node:

        def __init__(self, data):
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):

        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = BST.Node(data)
        else:
            # Start at the root
            self._insert(data, self.root)  

    def _insert(self, data, node):

        if data < node.data:
            if node.left is None:
                # There must be an empty space
                node.left = BST.Node(data)
            else:
                # Keep looking for an empty space
                self._insert(data, node.left)
        else:
            # The data must go on the right side of the node
            if node.right is None:
                # Empty Space found
                node.right = BST.Node(data)
            else:

                self._insert(data, node.right)

         
    def __iter__(self):
        # Start at the root
        yield from self._traverse_forward(self.root)  
        
    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
            
# LEAVE THE FOLLOWING-----------------------
tree = BST()
tree.insert("Bary")
tree.insert("Larry")
tree.insert("Scary")
tree.insert("Jery")
tree.insert("Ferry")
tree.insert("Mary")
tree.insert("Marry")
tree.insert("Harry")
tree.insert("Kary")
# LEAVE THE PREVIOUS------------------------


for x in tree:
    print(x)



"""
Output Expected: 
Bary
Ferry
Harry
Jery
Kary
Larry
Marry
Mary
Scary
"""
