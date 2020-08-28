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
    
级联的case
（）（） 2
（（）） 1
（（（）（））） 2 1 1
）（）（））
（（）））））（（（）（）（）（）））））（（（
遇到（就push
遇到）
	stack 非空，就pop，当前长度=2，如果和前面的级联，就计算新的长度，并更新最长， update prev 的index
	stack空，prev_index == 0, 继续扫描


 """
from stack import Stack
from stack import StackElement

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        temp_stack = Stack()
        prev_index = 0
        current_len = 0
        max_len = 0
        max_index = 0
        prev_len = 0
        for (index, bracket) in enumerate(s):
            if bracket == '(':
                ele = StackElement('(')
                temp_stack.push(ele)
            else:
                if not temp_stack.empty():
                    temp_stack.pop()
                    current_len = 2
                    if (index - prev_index) < 3:
                        current_len += prev_len
                    prev_index = index
                    prev_len = current_len
                    if current_len > max_len:
                        max_len = current_len
                        max_index = index
                else:
                    prev_index = 0
                    prev_len = 0
        print(s[(max_index-max_len+1):(max_index+1)])
        return max_len
    
sol = Solution()
s = ")()())"
s = "()"
s = ""
s = ")"
s = "("
# s = "(()"
# s = "()(((((()"
# s = "()(((((())"
s = "((())))()(()())()()()()(((())))))(()()()()()()((((((())))"
s = "()(()())"
print(sol.longestValidParentheses(s))

# the current solution can't handle the case as : ()(()())
# create a special element (position_of_( and prev_index) and push it into the stack
# once we pop the (, we can use this special element to check if we need to add the prev_len into the current len