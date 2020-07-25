import sys
import traceback
from enum import Enum

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

class sub_pattern:
    def next(self, s, input_index):
        log("next")
    
class dot_pattern(sub_pattern):
    def next(self, s, input_index):
        if s[input_index].isalpha():
            return (True, input_index+1)
        else:
            return (False, input_index+1)
        
class alpha_pattern(sub_pattern):
    def __init__(self, char):
        __char__ = char
    def next(self, s, input_index):
        if s[input_index] == __char__:
            return (True, input_index+1)
        else:
            return (False, input_index+1)
        
class alpha_star_pattern(sub_pattern):
    def __init__(self, char):
        __char__ = char
    def next(self, s, input_index):
        while(s[input_index] == __char__):
            input_index += 1
        return (True, input_index)
    
class dot_star_pattern(sub_pattern):
    def next(self, s, input_index):
        while(s[input_index].isalpha()):
            input_index += 1
        return (True, input_index)

class type(Enum):
    START = 1
    MIDDLE = 2
    END = 3
        
class sub_state:
    def __init__(self, type, sub_pattern):
        type = type
        sub_pattern = sub_pattern
    def next(self):
        sub_pattern.next()


class reg_state_machine:
    def __init__(self, regexp):
        log("created a statemachine with pattern {}".format(regexp))

    
    def run(self, s):
        log("statemachine is running")
    


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        statemachine = reg_state_machine(p)
        statemachine.run(s)
        return True

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

            
    



