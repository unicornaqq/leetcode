class StackElement:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    def push(self, item:StackElement):
        if self.top == None:
            self.top = item
        else:
            item.next = self.top
            self.top = item
    def pop(self):
        if self.top == None:
            return self.top
        else:
            temp = self.top
            self.top = temp.next
            return temp
    def empty(self):
        return self.top == None