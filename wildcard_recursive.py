import sys
import traceback
from pprint import pprint

DEBUG = 1
TEST = 1

def log(var):
    if DEBUG == 1:
        print(var)
    else:
        return

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # match any char sequence - *
        # match single char - ?
        # 1. think about the normal case/pattern
        # 2. think about the boundary/corner case.
        log([s, p])
        if len(s) == 0 and len(p) == 0:
            return True
        else:
            if len(p) == 0:
                return False
            else:
                if p[-1] == '*':
                    return (len(s) > 0 and self.isMatch(s[:-1], p)) or self.isMatch(s, p[:-1])
                elif p[-1] == '?':
                    return len(s)> 0 and self.isMatch(s[:-1], p[:-1])
                else:
                    return len(s) > 0 and self.isMatch(s[:-1], p[:-1]) and s[-1] == p[-1]


solution = Solution()

if TEST == 1:

    '''
        there is a case from leetcode, and our algorithrm has run long time, maybe even a loop, need to figure out
        "aaabaaabaabababbabababaababbabbbbaaaaababbaabbbaab"
        "*babbbb*aab**b*bb*aa*"
    '''

    try:
        assert (solution.isMatch("aaaab", "a*b")) == True
        assert (solution.isMatch("ab", "a?b")) == False
        assert (solution.isMatch("aa", "a")) == False
        assert (solution.isMatch("aa", "*")) == True
        assert (solution.isMatch("cb", "?a")) == False
        assert (solution.isMatch("adceb", "*a*b")) == True
        assert (solution.isMatch("acdcb", "a*c?b")) == False


        
    except AssertionError as error:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        print('An error occurred on line {} in statement {}'.format(line, text))

            
    



