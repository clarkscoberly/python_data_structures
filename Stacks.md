# Stacks

### Introduction

A **stack** is a data structure that takes data and returns back to the user the last item that was put into it. Effectively creating a last in first out or LIFO. This is used for various effects and a wide range of problems implemented in python using a list.

Consider the way that you eat icecream for example. The first pieces of icecream that you actually eat when you pull out that first scoop was the last drop of icecream put in during it's production. As the carton is filled from bottom to top. Code inside of this data structure is much the same. You store the first *bits* of code at the bottom of the stack and pile other pieces on top of it.

What is the purpose of the data structure?

What is the performance of the data structure (you will need to talk about big O notation)?

What kind of problems can be solved using the data structure?

How would the data structure be used in Python (in some cases you will need to discuss recursion)?

What kind of errors are common when using the data structure?



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
```
**Output of previous example:**

2

Vanilla
Chocolate

1

Vanilla


### Problem to Solve

