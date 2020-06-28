class Solution:
    def reverse(self, x: int) -> int:
        minus = False
        if x < 0:
            minus = True
            x = (-1)*x
        reversed_string = ""
        remaining = x // 10
        reversed_string += str(x % 10)
        while remaining != 0:
            reversed_string+= str(remaining % 10)
            remaining = remaining // 10
        if minus == True:
            result = -1 * int(reversed_string)
        else:
            result = int(reversed_string)
            
        neg_limit= -0x80000000
        pos_limit= 0x7fffffff

        if(result<0):
            val = result & neg_limit
            if(val == neg_limit): 
                #hex:0x80000000, bin:10000000... if the number is within the range, it will be all and out by 0 
                return result
            else:
                return 0
        elif(result == 0):
            return result
        else:
            val = result & pos_limit
            if(val == result):
                return result
            else:
                return 0

x = 1563847412
solution = Solution()
print(solution.reverse(x))
