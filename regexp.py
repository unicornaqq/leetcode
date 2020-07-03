import sys


(_, string, pattern, expected_result) = (None, None, None, None)
if len(sys.argv) == 4:
    (_, string, pattern, expected_result) = sys.argv[:]

DEBUG = 1

def log(var):
    if DEBUG == 1:
        print(var)
    else:
        return

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        subStringInP = p.split('.*')
        log("the len of the string is {}".format(len(s)))
        log(subStringInP)
        log(s)
        left_index = 0
        len_sub_string = 0
        for (index, sub) in enumerate(subStringInP):
            # with this method, we can make sure the sub
            # doesn't contain any .*, it means
            # it contains just char, . or *
            
            try:
                left_index = s.index(sub)
                right_index = s.rfind(sub)
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
                previous_star_left_index = 0
                previous_star_char = ''
                first_star_match = 0
                star_left_index = left_index
                for (star_index, star_sub) in enumerate(starSubString):
                    log([star_index, star_sub, left_index])
                    if star_sub == '':
                        # this is corresponding to the case 
                        # with multiple * concatenated
                        continue
                    try:
                        star_left_index = s.index(star_sub, star_left_index)
                        if first_star_match == 0:
                            first_star_match = 1
                            left_index = star_left_index
                        else:
                            if previous_star_char != '' and any([ c != previous_star_char for c in s[previous_star_left_index:star_left_index]]):
                                return False 
                        log(star_left_index)
                        previous_star_left_index = star_left_index
                        previous_star_char = star_sub[-1]
                    except ValueError:
                        if star_sub[:-1] == '':
                            # such as a*
                            continue
                        else:
                            try:
                                star_left_index = s.index(star_sub[:-1])
                                if first_star_match == 0:
                                    first_star_match = 1
                                    left_index = star_left_index
                                star_left_index += len(star_sub[:-1])
                                # we need this change since we have found
                                # a match stripped substring
                            except ValueError:
                                # it is possible, there is/are . inside
                                
                                return False
            if index == 0:
                # it is the head
                log("it is the head")
                if left_index != 0:
                    # it doesn't match the head of the string
                    # although it should do. Return 'False' 
                    # directly.
                    return False
            elif index == len(subStringInP) - 1:
                log("it is the tail")
                if right_index + len(sub) != len(s):
                    return False
            else:
                log("it is the middle")
                if left_index == 0 or (left_index == right_index and right_index + len(sub) == len(s)):
                    return False
                
        # subStringInP = p.split('.')        

        return True


solution = Solution()
# print(solution.isMatch("afafbeeab", "a.*b"))
# # for the case below, you can't match the b  after * to the
# # final b. so how to decide which b should be matched?
# print(solution.isMatch("afafbeeab", "a.*beeab"))
# # same case, if we start from back to the front, which a 
# # should be matched to the a within (a.*)?
# print(solution.isMatch("afafbeeab", "afa.*beeab"))
# print(solution.isMatch("afafbeeab", "afa.*beeab"))
# print(solution.isMatch("afafbeeabxxbeeab", "afa.*beeab"))
# # the beeab definitely should match the last beeab in
# # the origianl string
# print(solution.isMatch("afafbeeabxxbeeab", "afa.*beeab.*b"))
# print(solution.isMatch("afafbeeabxxbeeab", "ada.*beeab.*b"))

# if expected_result == None:                
#     to_match = "aab"
    
#     test_map = dict([
#         ("a.*b", True),
#         ("a***b", True),
#         ("aab", True),
#         ("a.b", True),
#         ("c*a*b", True),
#         ("a.*c", False), 
#         ("a.*b.*c", False)
#     ])
#     for (k, v) in test_map.items():
#         print(k)
#         try:
#             assert (solution.isMatch(to_match, k)) == v
#         except AssertionError as error:
#             print("case with pattern {} failed".format(k))
# else:
#     try:
#         assert (solution.isMatch(string, pattern)) == (expected_result == 'True')
#     except AssertionError as error:
#         print("case with pattern {} failed".format(pattern))
        
print(solution.isMatch("afafbeeabxxbeeab", "ad*a.*beeab.*.b")) #TODO, think about how to handle the . case