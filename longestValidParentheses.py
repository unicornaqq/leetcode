""" Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"


How about this "()(((((()", the tricky part is how do we know the last contribute to a long list?
hit ( 
    push it
hit ) 
    if the stack is empty, refresh the longest, the longest string has been broken, cumulative = 0, and document the current value as max_len
    else, pop it, and update the length +=2
        if the stack is empty, remember the length as previous, and update the max_len, cumulative = 0
        else, update the max_len

write down some cascade case, and figure out the pattern, so helps me to get the logic:

                    if (index - prev_index) < 2: # for local case
                        current_len += prev_len

And we need to take into the consideration the case that we need to connect the local longest string with a remote long string
when poping out the (, this helps to connect to remote long string.

 """
 
 
 
import line_profiler
import atexit

profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)

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

class Solution:
    @profile
    def longestValidParentheses(self, s: str) -> int:
        temp_stack = Stack()
        prev_index = 0
        current_len = 0
        max_len = 0
        max_index = 0
        prev_len = 0
        push_prev_len = False
        for (index, bracket) in enumerate(s):
            if bracket == '(':
                if push_prev_len == True:
                    ele = StackElement(prev_len)
                    push_prev_len = False
                else:
                    ele = StackElement(0)
                temp_stack.push(ele)
            else:
                if not temp_stack.empty():
                    ele = temp_stack.pop()
                    current_len = 2
                    if (index - prev_index) < 2: # for local case
                        current_len += prev_len
                    current_len += ele.val # for the case that need to connect with 
                    prev_index = index
                    prev_len = current_len
                    if current_len > max_len:
                        max_len = current_len
                        max_index = index
                    push_prev_len = True
                else:
                    prev_index = 0
                    prev_len = 0
        # print(s[(max_index-max_len+1):(max_index+1)])
        return max_len
    
sol = Solution()
s = ")()())"
# s = "()"
# s = ""
# s = ")"
# s = "("
# s = "(()"
# s = "()(((((()"
# s = "()(((((())"
# s = "((())))()(()())()()()()(((())))))(()()()()()()((((((())))"
# s = "()(()())"
s = "((((((())))(((((())))))(())((((())))()((((((((()()()(((())()()(((((()))))()()())())))))((((()()()))((((((()))())(((((((())()))))))(()))()()(((((((())))))))))(((((()))))))(((((((((((((((((()))))))))))))))))))))))))))))))))))((()))())())())()))))))))))))))"
print(sol.longestValidParentheses(s))
