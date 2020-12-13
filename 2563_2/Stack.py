class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.item == []
    def push(self,item):
        self.item.append(item)
    def pop(self):
        return self.tiems.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)