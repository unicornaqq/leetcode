class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        result = True
        
        if p == ".*":
            return True
        if len(s) != len(p) and p.find("*") == -1:
            return False
        
        precedence = None
        star_mode = False
        
        for i in range(0, min(len(s), len(p))):
            print("p[{}] is {}, and s[{}] is {}".format(i, p[i], i, s[i]))
            if p[i] == ".":
                precedence = "."
                continue
            elif p[i] == "*" or star_mode == True:
                start_mode = True
                if precedence != None:
                    if precedence == ".":
                        return True
                    elif precedence == s[i]:
                        continue
                    else:
                        return False
                else:
                    return False
            elif p[i] == s[i]:
                precedence = p[i]
                continue
            else:
                return False
                
        return result
                
                
                
to_match = "aab"
pattern = "c*a*b"
solution = Solution()
print(solution.isMatch(to_match, pattern))