import sys
string = str(sys.argv[1])
#string = "ccd"
#string = "dmdooeofmeoefok0000000000000oooooo"
#string = "oiakfopekfoakwenhuhekfff[iiii[fff"
#string = "sifjwaijfwejeafw[oje[oo[ejo["

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_str = None
        if len(s) <= 1:
            longest_str = s
        else:
            longest_str = s[0]
        max_length = 0
        for i in range(0, len(s)):
            print("i===={}".format(i))
            temp_length = 1
            #repeat_pattern_guard = 0
            #double_repeat_pattern_guard = 0
            skip_simple_repeat_pattern = False
                    
            j = 0
            for j in range(1, min(i+1, len(s)-i)):
                print("j={}".format(j))
                if s[i-j] == s[i+j]:
                    temp_length += 2
                    print("temp_length1 is {}".format(temp_length))
                    if temp_length > max_length:
                        max_length = temp_length
                        longest_str = s[(i-j):(i+j+1)]
                        print("the lstr is {}".format(longest_str))
                        print("max_length is {}".format(max_length))
                else:
                    j -= 1
                    break
            
            if j == 0:
                # it means, no substr as "aba"
                # need to check whether there is something like "aa" or "baab"
                repeat_pattern_found = False
                repeat_length = 0
                for index in range(i+1, len(s)):
                    if s[index] == s[i] and not skip_simple_repeat_pattern:
                        temp_length += 1
                        print("temp_length2 is {}".format(temp_length))
                        repeat_pattern_found = True
                        repeat_length = temp_length
                        if temp_length > max_length:
                            max_length = temp_length
                            longest_str = s[i:(index+1)]
                            print("the lstr is {}".format(longest_str))
                            print("max_length is {}".format(max_length))
                            print("repeat_length is {}".format(repeat_length))
                    elif repeat_pattern_found == True and i-(index-(repeat_length+i-1)) >= 0 and s[index] == s[i-(index-(repeat_length+i-1))]:
                        temp_length += 2
                        print("temp_length3 is {}".format(temp_length))
                        #repeat_pattern_guard = 0
                        skip_simple_repeat_pattern = True
                        #double_repeat_pattern_guard += 1
                        if temp_length > max_length:
                            longest_str = s[(i-(index-(repeat_length+i-1))):(index+1)]
                            max_length = temp_length
                            print("the lstr is {}".format(longest_str))
                            print("max_length is {}".format(max_length))
                    else:
                        break
        return longest_str



solution = Solution()
print(solution.longestPalindrome(string))


