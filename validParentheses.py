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

def match(left, right):
    return (left == '(' and right == ')') or (left == '[' and right == ']') or (left == '{' and right == '}')

class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        for parenthesis in s:
            if parenthesis in ['(', '[', '{']:
                ele = StackElement(parenthesis)
                stack.push(ele)
            elif parenthesis in [')', ']', '}']:
                if stack.empty():
                    return False
                left_part = stack.pop()
                if not match(left_part.val, parenthesis):
                    return False
        if stack.empty():
            return True
        else:
            return False

sol = Solution()    
s = "("
print(sol.isValid(s))