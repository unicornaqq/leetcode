class Solution:
    def intToRoman(self, num: int) -> str:

        result = ''
        
        mapping = [[1000, 'M'], 
                [900, 'CM'],
                [500, 'D'],
                [400, 'CD'],
                [100, 'C'],
                [90, 'XC'],
                [50, 'L'],
                [40, 'XL'],
                [10, 'X'],
                [9, 'IX'],
                [5, 'V'],
                [4, 'IV'],
                [1, 'I']]
        
        for i in range(len(mapping)):
            # print(mapping[i][0], mapping[i][1])
            char_number = num // mapping[i][0]
            if char_number != 0:
                for _ in range(char_number):
                    result += mapping[i][1]
                num = num % mapping[i][0]
        
        return result
                

sol = Solution()
print(sol.intToRoman(1900))

