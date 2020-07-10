import sys
import traceback


(_, string, pattern, expected_result) = (None, None, None, None)
if len(sys.argv) == 4:
    (_, string, pattern, expected_result) = sys.argv[:]

DEBUG = 1
TEST = 0

def log(var):
    if DEBUG == 1:
        print(var)
    else:
        return

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        subStringInP = p.split('.*')
        log("the len of the string is {}".format(len(s)))
        log("Raw:{}".format(s))
        log("Pattern:{}".format(p))
        log(subStringInP)


        left_index = 0
        right_index = 0
        offset = 0
        roffset = 0
        
        for (index, sub) in enumerate(subStringInP):
            # with this method, we can make sure the sub
            # doesn't contain any .*, it means
            # it contains just char, . or *
            try:
                if sub == '':
                    (left_index, right_index, offset, roffset) = (left_index, right_index, offset, roffset)
                else:
                    left_index = s.index(sub, offset)
                    right_index = s.rfind(sub, offset)
                    offset = left_index + len(sub)
                    roffset = right_index + len(sub)
                log([left_index, right_index])
            except ValueError:
                # there could be * or . in the sub string
                # try to split the sub string with * first
                if sub.find("*") == -1 and sub.find(".") == -1:
                    return False
                starSubString = sub.split("*")
                # the case with no * inside will be simplified
                # to single string.
                log(starSubString)
                # return None
                previous_star_char_index = 0
                previous_star_char_rindex = 0
                previous_star_char = ''
                first_star_match = 0
                star_offset = offset # we start from the end of last matched sub string
                star_roffset = roffset
                for (star_index, star_sub) in enumerate(starSubString):
                    log([star_index, star_sub, star_offset, star_roffset])
                    if star_sub == '':
                        # this is corresponding to the case 
                        # with multiple * concatenated
                        continue
                    try:
                        star_left_index = s.index(star_sub, star_offset)
                        star_right_index = s.rfind(star_sub, star_offset)
                        if first_star_match == 0:
                            # this is the first sub string of
                            # the string splited by *
                            # e.g. abc*def*opl
                            # the location of a indicate the start
                            # of the "abc*def*opl", which is recored by 
                            # left_index
                            first_star_match = 1
                            left_index = star_left_index
                            right_index = star_right_index
                        else:
                            # def, opl for the e.g. above
                            # check whether the * matches 0 char
                            # or match repeated char.
                            # if previous_star_char is '', it means * represent
                            # 0 char. don't need to care about in this 
                            # branch. And it is handled in the exception
                            # handling logic.
                            
                            
                            """ after split the string with *, there could be different
                            way to match the substring, need to find out which way
                            is the right match, and then based on that match method to figure out
                            the offset and roffset of the whole substring containning *.
                            for the example:
                                Raw:afafbeeabxxbeeab
                                Pattern:af*a.*afa.*eab
                            although [af, a] can match the raw string in different way
                            but only afa at the head of the string should be the match object.
                            although, the a can match multiple instance TODO"""
                            
                            if previous_star_char != '' and (
                                any([ c != previous_star_char for c in s[previous_star_char_index:star_left_index]]) and 
                                any([ c != previous_star_char for c in s[previous_star_char_rindex:star_right_index]])):
                                return False 
                        log([star_left_index, star_right_index])
                        star_offset = star_left_index + len(star_sub)
                        star_roffset = star_right_index + len(star_sub)
                        # the char to be repeated is at the end of substring
                        previous_star_char_index = star_offset - 1
                        previous_star_char_rindex = star_roffset - 1
                        previous_star_char = star_sub[-1] # the char before * is the one to repeat
                        offset = star_offset # this is for the next iterate for .* splited substring
                        roffset = star_roffset
                    except ValueError:
                        if star_sub[:-1] == '':
                            # such as a*
                            continue
                        else:
                            try:
                                # this is for the case of 0 match
                                # so need to get rid of the end char, and try
                                # to match again
                                star_left_index = s.index(star_sub[:-1], star_offset)
                                star_right_index = s.rfind(star_sub[:-1], star_offset)
                                if first_star_match == 0:
                                    first_star_match = 1
                                    left_index = star_left_index
                                    right_index = star_right_index
                                star_offset += len(star_sub[:-1])
                                star_roffset += len(star_sub[:-1])
                                offset = star_offset
                                roffset = star_roffset

                            except ValueError:
                                # it is possible, there is/are . inside the current substring
                                # use the . to split the sub string
                                # the distance between the sub string should be 1
                                if star_sub.find('.') == -1:
                                    return False
                                else:
                                    # for (dot_index, dot_sub) in enumerate(star_sub):
                                    #     #TODO
                                    log("the star_sub is {}".format(star_sub))
                                    # how about the case such as ..a.c.. which starts with . and/or end with ..
                                    # if  the sub string only contain ., 
                                    dot_count = star_sub.count('.')
                                    if dot_count == len(star_sub):
                                        # . for all
                                        log("all are dots")
                                    else:
                                        # some are alpha, find the index of those alpha                                    
                                        log("some are alpha")        
                                    return False
            if index == 0:
                # it is the head
                # for things at head, the left offset/left_index should at 0
                # for head, we should use the left_index. 
                log("it is the head offset={}, roffset={}".format(offset, roffset))
                if left_index != 0:
                    # it doesn't match the head of the string
                    # although it should do. Return 'False' 
                    # directly.
                    return False
                # but there is another case, that the pattern only match partial of the string
                # in this case, the left_index is 0, but it doesn't match. #TODO
                # maybe, this to do can be handled by change the below elif to if, the head and tail is not excluseive.
            
            if index == len(subStringInP) - 1:
                # for pattern at the end, we should check the right_index instead.
                # the right_index + string_len, or the roffset should be right
                # to the end of the raw string
                log("it is the tail offset={}, roffset={}".format(offset, roffset))
                if offset != len(s) and roffset != len(s):
                    return False
            
            # else:
                # for pattern in the middle, it doesn't matter which part of the raw
                # string deos the pattern match to.
                # log("it is the middle")
                # if left_index == 0 or offset == len(s):
                #     return False
                
                
        # subStringInP = p.split('.')        
        if offset != len(s) and roffset != len(s):
            return False
        else:
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
        
    except AssertionError as error:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        print('An error occurred on line {} in statement {}'.format(line, text))

    if expected_result == None:                
        to_match = "aab"
        
        test_map = dict([
            ("a.*b", True),
            ("a***b", True),
            ("aab", True),
            ("a.b", True),
            ("c*a*b", True),
            ("a.*c", False), 
            ("a.*b.*c", False)
        ])
        for (k, v) in test_map.items():
            print(k)
            try:
                assert (solution.isMatch(to_match, k)) == v
            except AssertionError as error:
                print("case with pattern {} failed".format(k))
    else:
        try:
            assert (solution.isMatch(string, pattern)) == (expected_result == 'True')
        except AssertionError as error:
            print("case with pattern {} failed".format(pattern))
            
    print(solution.isMatch("afafbeeabxxbeeab", "ad*a.*beeab.*e.b")) #TODO, think about how to handle the . case
    print(solution.isMatch("afafbeeabxxbeeab", "af*a.*fb.*eab"))
    print(solution.isMatch("afcafebeeabxxbeeab", "afc.*afc.*eab"))
    print(solution.isMatch("acb", "ac"))


print(solution.isMatch("aaabdcaeebdcampbqc", "a..ac.c"))
