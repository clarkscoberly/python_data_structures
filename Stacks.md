# Stacks

### Introduction

A **stack** is a data structure that takes a piece of data and adds it to a container which you can only pull out the last item that was put into it. Effectively creating a last in first out or *LIFO*. This is used for various effects and a wide range of problems. It is implemented within python using a list/array.

Consider the way that you eat icecream for example. The first bites of icecream that you eat when you pull out those first scoops were the last drops of icecream placed within that container during production. **The carton is filled from bottom to top.** Code inside of a **stack** is much the same. You store the first *bits* of code at the bottom of the **stack** and pile other pieces on top of it.

### Purpose and Characteristics
The Undo, not to be confused with the hairstyle, the updo.

One of the major purposes of the **stack** is an allowance for the user to reverse the order of the data that has been put onto the stack. This functionality is used throughout every day life in the form of the back button on your phone or computer, the undo text or control z and even putting your undone actions onto another stack so that you can redo items that you have undone.

### Performance

Performance of a **Stack** with common operations

Operation | Usage | Python Usage | Performance 
----------|-------|--------------|------------
Add       | my_stack.append(item) | Put data onto the top of the stack | 0(1)
Remove    | my_stack.pop() | Take the last item off the top of the stack | 0(1)
Length    | len(my_stack) | Find the number of items on the stack | 0(1)
Empty     | if len(my_stack) == 0: | Check to see if the stack is empty | 0(1)

### Characteristics



### Example
```python
"""
The following is an example of a simple STACK being
implemented.
"""

class Ice_Cream_Stack:
    
    def __init__(self):
        # The container or "Stack"
        self.container = []
        
    # add a scoop on to the top of the STACK
    def add_scoop(self, type):
        self.container.append(type)

    # Take a scoop off the top of the STACK
    def eat_scoop(self):
        self.container.pop()

    # Check the height of the STACK
    def check_ice_cream(self):
        print(len(self.container))
        for scoop in self.container:
            print(scoop)

ice_cream = Ice_Cream_Stack()

ice_cream.add_scoop("Vanilla")
ice_cream.add_scoop("Chocolate")

ice_cream.check_ice_cream()
ice_cream.eat_scoop()
ice_cream.check_ice_cream()

"""
Output of this example:
2
Vanilla
Chocolate
1
Vanilla
"""
```

### Problem to Solve
```Python
"""
Add an item to a stack

undo/remove n number of items from the stack

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
        pass

    # Implement undoing/removing n number of items from the stack
    def undo(self, removals=1):
        pass

    def check_items(self):
        for item in self.stack:
            print(item, end=" ")
        print()
            
    # Implement checking the length of items on the stack
    def length(self):
        pass

    # Implement printing each of the items on the stack in reverse
    def reverse(self):
        pass

    # Implement "redo" functionality putting back onto the stack the last thing that was taken off the stack
    def redo(self):
        pass

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

[ProblemSolution](https://github.com/clarkscoberly/python_data_structures/blob/main/Stacks_problem_solution.md)
