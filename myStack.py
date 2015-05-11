"""
Stack
Programmer: Taylor Scafe
2/23/2014
"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        item = self.items.pop()
        return item

    def peek(self):
        item = self.items[-1]
        return item

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
        
