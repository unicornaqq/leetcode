class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        mapping = {
            'M': 1000, 
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        
        i = 0
        while i < len(s):
            # print(mapping[i][0], mapping[i][1])
            if i+1 < len(s):
                x = mapping.get(s[i:i+2])
                if x is None:
                    x = mapping.get(s[i])
                    result += x
                    i += 1
                else:
                    result += x
                    i += 2
            else:
                x = mapping.get(s[i])
                result += x
                i += 1
                        
                    
        
        return result
                

sol = Solution()
print(sol.romanToInt('III'))

