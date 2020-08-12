class Solution:
    def temp_solution(self, digits, result, mapping):
        if len(digits) == 1:
            return mapping.get(digits[0])
        
        print(digits)
        return [c+e for e in self.temp_solution(digits[1:], result, mapping) for c in mapping.get(digits[0])] 
    
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []
        mapping = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        return self.temp_solution(digits, [], mapping)
           
    
solution = Solution()
digits = "2398739"
print(solution.letterCombinations(digits))
    