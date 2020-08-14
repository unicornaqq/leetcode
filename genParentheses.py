""" Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
] """


class Solution:
    def find(self, n):
      result = set()
      if n == 1:
        return ["()"]
      for i in range(1, n):
        # print("value in the middle is {}".format(self.find(i)+ self.find(n-i)))
        # print([elem1 + elem2 for elem1 in self.find(i) for elem2 in self.find(n-i)])
        [result.add(elem) for elem in [elem1 + elem2 for elem1 in self.find(i) for elem2 in self.find(n-i)]]
      [result.add(elem) for elem in ["("+e+")" for e in self.find(n-1)]] 

      return [ele for ele in result]
      
        
        
  
    def generateParenthesis(self, n: int):
      return self.find(n)
    

# how to handle this case: (())(())
# find(2) = find(1)find(1) + (find(1)) => ()(), (())
# find(3) = find(1)find(2) + find(2)find(1) + (find(2))
# find(4) = find(1)find(3) + find(2)find(2) + find(3)find(1) + (find(3))  

sol = Solution()
n = 4
print("final result is {}".format(sol.generateParenthesis(n)))


# %%
