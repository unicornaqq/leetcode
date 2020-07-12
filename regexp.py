import sys
import traceback


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
        if p.find("*") == -1 and len(p) != len(s):
            return False
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
                                any([ d != previous_star_char for d in s[previous_star_char_rindex:star_right_index]])):
                                return False
                            
                            if previous_star_char == '' and (
                                star_left_index != star_offset and
                                star_right_index != star_roffset
                            ):
                            # this is for the case that the * match 0 instance.
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
                        # there are two cases:
                        # 1. 0 match for the 0;
                        # 2. .
                        if star_sub[:-1] == '' and star_sub != '.':
                            # such as a*
                            continue
                        else:
                            try:
                                # this is for the case of 0 match
                                # so need to get rid of the end char, and try
                                # to match again
                                # NOTE: and for this case, we need to make sure
                                # the next matched substring should follow
                                # previous matched substring directly.
                                if star_sub == '.':
                                    s.index(star_sub)
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
                                    log("the star_sub is {}".format(star_sub))
                                    # how about the case such as ..a.c.. which starts with . and/or end with ..
                                    # if  the sub string only contain ., 
                                    dot_count = star_sub.count('.')
                                    if dot_count == len(star_sub):
                                        # . for all
                                        log("all are dots")
                                        star_left_index = offset
                                        star_right_index = len(s)-len(star_sub)
                                        star_offset = star_left_index + len(star_sub)
                                        star_roffset = star_right_index + len(star_sub)
                                        
                                        offset = star_offset # this is for the next iterate for .* splited substring
                                        roffset = star_roffset
                                        
                                        if first_star_match == 0:
                                            first_star_match = 1
                                            left_index = star_left_index
                                            right_index = star_right_index
                                        
                                    else:
                                        # #TODO some are alpha, find the index of those alpha:                                     
                                        log("some are alpha")        
                                        dot_split_list = star_sub.split(".")
                                        log(dot_split_list)
                                        max_sub_len = 0
                                        max_sub_index = 0
                                        for (dot_list_index, dot_sub_string) in enumerate(dot_split_list):
                                            if len(dot_sub_string) > max_sub_len:
                                                max_sub_len = len(dot_sub_string)
                                                max_sub_index = dot_list_index
                                        max_sub_string = dot_split_list[max_sub_index]
                                        log("max sub string is {}".format(max_sub_string))
                                        try:
                                            anchor_star_sub_offset = star_sub.index(max_sub_string)
                                            anchor_raw = [i - anchor_star_sub_offset for (i,c) in enumerate(s) 
                                                          if (max_sub_string.startswith(c) 
                                                              and s[i:(i+len(max_sub_string))] == max_sub_string 
                                                              and i >= anchor_star_sub_offset
                                                              and i < (len(s)-len(max_sub_string))
                                                              and i >= offset)]
                                            # #TODO it is possible that there are multiple anchor point that can match, for example 3
                                            # but the left and right most match is not the complete match, the middle is the 
                                            # only match, this method can't cover it. 
                                            # this dot case is different with other no-dot cases since what we are trying to match
                                            # is just part of the substring, while for other cases, it matches the whole string, 
                                            # found is found.
                                            # so, we have to check all the possible locations of the anchors.
                                            log("anchor_raw is {}".format(anchor_raw))
                                            log("anchor_star_sub is {}".format(anchor_star_sub_offset))
                                            # NOTE: need to loop over the anchor_raw list for each possible location
                                            found_match_dot = False
                                            for (i,dot_index) in enumerate(anchor_raw):
                                                slice_raw_string = s[dot_index:(dot_index+len(star_sub))]
                                                # log(slice_raw_string)
                                                if any(dot == '.' or dot == slice_raw_string[i] for (i,dot) in enumerate(star_sub)):
                                                    log(slice_raw_string)
                                                    found_match_dot = True
                                                    if i == 0:
                                                        # TODO:update the left index
                                                        log("found the matching at the beginning")
                                                        star_left_index = dot_index
                                                        if first_star_match == 0:
                                                            first_star_match = 1
                                                            left_index = star_left_index
                                                        star_offset += len(star_sub)
                                                        offset = star_offset
                                                    if i == len(anchor_raw)-1:
                                                        # TODO: update the right index
                                                        log("find matching at the end")
                                                        star_right_index = dot_index
                                                        star_roffset = star_right_index + len(star_sub)
                                                        roffset = star_roffset
                                            if found_match_dot == False:
                                                return False

                                        except ValueError:
                                            log("dot split substring is not found")
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
                # #TODO but there is another case, that the pattern only match partial of the string
                # in this case, the left_index is 0, but it doesn't match. 
                # maybe, this to do can be handled by change the below elif to if, the head and tail is not excluseive.
            
            if index == len(subStringInP) - 1:
                # for pattern at the end, we should check the right_index instead.
                # the right_index + string_len, or the roffset should be right
                # to the end of the raw string
                log("it is the tail offset={}, roffset={}".format(offset, roffset))
                # TODO: for the case of abc.*, need to handle it carefully
                if offset != len(s) and roffset != len(s):
                    if subStringInP[index] != '':
                        return False
                    else:
                        return True
            
            # else:
                # for pattern in the middle, it doesn't matter which part of the raw
                # string deos the pattern match to.
                # log("it is the middle")
                # if left_index == 0 or offset == len(s):
                #     return False
                
                
        # subStringInP = p.split('.')        
        # if offset != len(s) and roffset != len(s):
        #     return False
        # else:
        #     return True
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
            # print(k)
            try:
                assert (solution.isMatch(to_match, k)) == v
            except AssertionError as error:
                print("case with pattern {} failed".format(k))
    else:
        try:
            assert (solution.isMatch(string, pattern)) == (expected_result == 'True')
        except AssertionError as error:
            print("case with pattern {} failed".format(pattern))
            
    



