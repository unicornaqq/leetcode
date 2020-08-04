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
        # match[M][N] means whether s(len=M) match p(len=N)
        # match[i][j] = True if s(1, i-1) match with p(1, j-1)
        # [0, 1, ... i-2, i-1, ., ...]
        # [0, 1, ... j-2, j-1, ., ...]
        match = [[False for x in range(len(p)+1)] for y in range(len(s)+1)]
        match[0][0] = True
        # pprint(match)
        for i in range(0, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    # # here means every a-z
                    #                  #
                    # [0, 1, ... i-2, i-1, ., ...]
                    # [0, 1, ... j-2, j-1, ., ...]
                    #             #,  *
                    match[i][j] = ((i > 0 and match[i-1][j]) # no matter what s[i-1] is, since * match a sequence of chars here
                                or match[i][j-1]) # nothing matched by * here
                elif p[j-1] == '?':
                    #                  #
                    # [0, 1, ... i-2, i-1, ., ...]
                    # [0, 1, ... j-2, j-1, ., ...]
                    #             #,  ?
                    # it can match 0 or 1 any char for '?'
                    match[i][j] = ((match[i-1][j-1] and i > 0) ) # for 1 instance match
                else:
                    match[i][j] = (i > 0 and match[i-1][j-1] and 
                                    s[i-1] == p[j-1])
                # print([i, j, match[i][j]])
        # pprint(match)
        return(match[len(s)][len(p)])
                
                
            
                
                

solution = Solution()

if TEST == 1:

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

            
    



