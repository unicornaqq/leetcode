import sys
import traceback
from pprint import pprint

# recursive method will be used when the substate is not determinated.


(_, string, pattern, expected_result) = (None, None, None, None)
if len(sys.argv) == 4:
    (_, string, pattern, expected_result) = sys.argv[:]

DEBUG = 1
TEST = 1

def log(var):
    if DEBUG == 1:
        print(var)
    else:
        return

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
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
            # how handle the i == 0 case?
            # if i == 0:
            # it will try to check s[-1] which is definitely not acceptable
            # for the case of i == 0, which means it is an empty string.
            #
            # The only match cases:
            #   1. to match an empty string which is match[0][0]
            # which has been covered above;
            #   2. to match an empty string with p == '.*', which is corresponding
            # to match[0][2], it should be True. It goes to the branch: match[i][j-2].
            for j in range(1, len(p)+1):
                # for the j == 0 case, that means the pattern is empty. 
                # nothing can be matched as long as the input string s is not empty.
                # so, we just skip the j == 0 case in this loop, and leave it to the default False value.
                # print([i, j])
                if p[j-1] == '*' and j > 1:
                    # print("p[{}] is {}". format(j-1, p[j-1])) 
                    #                  a
                    # [0, 1, ... i-2, i-1, ., ...]
                    # [0, 1, ... j-2, j-1, ., ...]
                    #             a,  *
                    match[i][j] = (i > 0 and match[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.')) or match[i][j-2]
                else:
                    # for the j == 1 case:
                    # that means match[i][1] is try to match s(0, 1, 2, .. i-1) and p[0]
                    # you know, the only potential match case is s[0] and p[0], which
                    # is corresponding to match[1][1], so, it will be derived from match[0][0]
                    # if s[0] == p[0]. This kind of match is exactly what we want, single char match case.
                    match[i][j] = i > 0 and match[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                # print([i, j, match[i][j]])
        # pprint(match)
        return(match[len(s)][len(p)])
                
                
            
                
                

solution = Solution()

if TEST == 1:

    try:
        assert (solution.isMatch("aaaab", "a*b")) == True# the only match case: aaaab vs a*b
        assert (solution.isMatch("afafbeeab", "a.*b")) == True
        # for the case below, you can't match the b  after * to the
        # final b. so how to decide which b should be matched?
        assert (solution.isMatch("afafbeeab", "a.*beeab")) == True
        # same case, if we start from back to the front, which a 
        # should be matched to the a within (a.*)?
        assert (solution.isMatch("afafbeeab", "afa.*beeab")) == True
        assert (solution.isMatch("afafbeeab", "afa.*beeab")) == True
        assert (solution.isMatch("afafbeeabxxbeeab", "afa.*beeab")) == True
        # the beeab definitely should match the last beeab in
        # the origianl string
        assert (solution.isMatch("afafbeeabxxbeeab", "afa.*beeab.*b")) == True
        assert (solution.isMatch("afafbeeabxxbeeab", "ada.*beeab.*b")) == False

        assert (solution.isMatch("afafbeeabxxbeeab", "ad*a.*beeab.*e.b")) == False
        assert (solution.isMatch("afafbeeabxxbeeab", "af*a.*fb.*eab")) == True
        assert (solution.isMatch("afcafebeeabxxbeeab", "afc.*afc.*eab")) == False
        assert (solution.isMatch("acb", "ac")) == False
        assert (solution.isMatch("aaabdcaeebdcampbqc", "..ab.c.*")) == True
        assert (solution.isMatch("aaabdcaeebdcampbqc", "aaa.*......*bqc")) == True
        assert (solution.isMatch("aa", "a")) == False
        assert (solution.isMatch("mississippi", "mis*is*ip*.")) == True
        assert (solution.isMatch("mississippi", "mis*is*p*.")) == False
        assert (solution.isMatch("aaa", "ab*a")) == False
        assert (solution.isMatch("a", "ab*a")) == False
        assert (solution.isMatch("aab", "a.*b")) == True
        assert (solution.isMatch("aab", "a***b")) == True
        assert (solution.isMatch("aab", "aab")) == True
        assert (solution.isMatch("aab", "a.b")) == True
        assert (solution.isMatch("aab", "c*a*b")) == True
        assert (solution.isMatch("aab", "a.*c")) == False
        assert (solution.isMatch("aab", "a.*b.*c")) == False
        assert (solution.isMatch("bbbba", ".*a*a")) == True
        assert (solution.isMatch("ab", ".*..c*")) == True


        
    except AssertionError as error:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        print('An error occurred on line {} in statement {}'.format(line, text))

            
    



