```Python
"""
Add an item to a stack

undo n number of items from the stack

check length of stack

print reverse order of the stack

have a redo option for n number of removed items back onto the stack

"""

class Stack:

    # Add a stack array and redo stack array
    def __init__(self):
        self.stack = []
        self.redo_stack = []

    # Implement adding an item to the stack
    def add(self, item):
        self.stack.append(item)

    # Implement removing n number of items from the stack
    def undo(self, removals=1):
        for num in range(removals):
            removed_item = self.stack.pop()
            print("Removed:", removed_item)
            self.redo_stack.append(removed_item)

    def check_items(self):
        for item in self.stack:
            print(item, end=" ")
        print()
            
    # Implement checking the length of items on the stack
    def length(self):
        print(len(self.stack))

    # Implement printing each of the items on the stack in reverse
    def reverse(self):
        for i in range(len(self.stack) -1, -1, -1):
            print(self.stack[i], end=" ")
        print()

    # Implement "redo" functionality putting back onto the stack the last thing that was taken off the stack
    def redo(self):
        self.add(self.redo_stack.pop())

stack = Stack()

#----------------------------------------------------
#         TASK 1 - Add and Undo/Remove Items
#----------------------------------------------------
print("Task 1")
stack.add("1")
stack.add("2")
stack.add("3")
stack.add("4")
stack.check_items()
stack.undo(2)
stack.check_items()

# Expected Output
# 1, 2, 3, 4
# 1, 2

#----------------------------------------------------
#      TASK 2 - Check length and Print Reversed
#----------------------------------------------------
print("\n\n\nTask 2")
stack.add("3")
stack.length()
stack.reverse()
stack.undo()
stack.length()


# Expected Output
# 3
# 3 2 1 
# Removed: 3
# 2

#----------------------------------------------------
#                    TASK 3 - Redo 
#----------------------------------------------------

print("\n\n\nTask 3")
stack.check_items()
stack.redo()
stack.check_items()
stack.redo()
stack.check_items()
stack.add("Flibbity Gibbit")
stack.undo()
stack.check_items()
stack.redo()
stack.check_items()
stack.length()

# Expected Output:
# 1 2 
# 1 2 3 
# 1 2 3 3 
# Removed: Flibbity Gibbit
# 1 2 3 3 
# 1 2 3 3 Flibbity Gibbit 
# 5```
