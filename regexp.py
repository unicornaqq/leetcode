class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        result = True
        
        if p == ".*":
            return True
        if len(s) != len(p) and p.find("*") == -1:
            return False
        
        precedence = None
        
        """ for i in range(0, min(len(s), len(p))):
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
                
        return result """
        
        (i, j) = (0, 0)        
        while i < len(s) and j < len(p):
            print("p[{}] is {}, and s[{}] is {}".format(j, p[j], i, s[i]))
            if p[j] == ".":
                precedence = "."
                i+=1
                j+=1
                continue
            elif p[j] == "*":
                if precedence != None:
                    if precedence == ".":
                        """ not always true, for example:
                        string "abc", pattern "a.*b"
                        How to handle this case. """
                        
                        return True
                    elif precedence == s[i]:
                        i+=1
                        continue
                    else:
                        j+=1
                        continue
                else:
                    return False
            elif p[j] == s[i]:
                precedence = p[i]
                i+=1
                j+=1
                continue
            else:
                return False
        
        return result           
                
to_match = "aab"
solution = Solution()
test_map = dict([
    ("a.*b", True),
    ("a***b", True),
    ("aab", True),
    ("a.b", True),
    ("c*a*b", True),
    ("a.*c", False)
])
for (k, v) in test_map.items():
    print(k)
    try:
        assert (solution.isMatch(to_match, k)) == v
    except AssertionError as error:
        print("case with pattern {} failed".format(k))
    