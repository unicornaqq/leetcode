# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# If multiple answers are possible, just return any of them.

# Example 1:

# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:

# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:

# Input: numerator = 2, denominator = 3
# Output: "0.(6)"

# The tricky part is that, the repeating part in the fractional part is not necessarily be single number.
# it could be some thing like 0.102102102102, or an even ugly case, such as 0.7102102102...
# So, the problem goes to find the logest repeating number
# for the case: 1/6, the result is 0.1(6)

class Solution:
    # def findLongestRepeating(self, string: str) -> str:
        
        
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        mapping = dict()
        repeating = ''
        result = ''
        signal = -1 if ((numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0)) else 1
        # print(signal)
        numerator = abs(numerator)
        denominator = abs(denominator)
        inte = numerator // denominator
        remain = numerator % denominator
        # print(inte, remain)
        if remain == 0:
            return '-' + str(inte) if signal == -1 else str(inte)
        while remain > 0:
            if result == '':
                if inte == 0:
                    result += '0.'
                else:
                    result += str(inte) + '.'

            if remain < denominator:
                remain *= 10
            
            inte = remain // denominator
            remain = remain % denominator
            result += str(inte)
            print(inte, remain, result)
            if (temp:= mapping.get((inte, remain))) != None:
                if temp != True:
                    mapping[(inte, remain)] = True
                    repeating += str(inte)
                else:
                    break
                    # print("repeating {}".format(repeating))
            else:
                mapping[(inte, remain)] = False
        if repeating != '':        
            # print('repeat part is {}'.format(repeating))
            [intePart, fraction] = result.split('.')
            repeatStart = fraction.find(repeating)
            result = intePart + '.' + fraction[0:repeatStart] + '(' + repeating + ')'        
        return '-'+result if signal == -1 else result
        

sol = Solution()
print(sol.fractionToDecimal(7, -12))
print(sol.fractionToDecimal(2, 1))
print(sol.fractionToDecimal(1, 2))
print(sol.fractionToDecimal(1, 6))
print(sol.fractionToDecimal(4, 333))
print(sol.fractionToDecimal(1, 90))
print(sol.fractionToDecimal(100, 90))



#%%
50//8

# %%
-50//8

# %%
2/1

# %%
