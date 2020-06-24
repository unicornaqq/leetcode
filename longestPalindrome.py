class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_str = None
        if len(s) <= 1:
            longest_str = s
        max_length = 0
        for i in range(1, len(s)):
            #print(i)
            temp_length = 0
            if s[i] == s[i-1]:
                # example "abb" -> "bb"
                temp_length = 2
                j = 1
                for j in range(1, min(i,len(s)-i)):
                    if s[i+j] == s[i-j-1]:
                        temp_length += 2
                    else:
                        break
                if temp_length > max_length:
                    max_length = temp_length
                    longest_str = s[(i-j):(i+j)]
            else:
                j = 1
                for j in range(1, min(i+1, len(s)-i)):
                    if s[i-j] == s[i+j]:
                        temp_length += 2
                    else:
                        break
                if temp_length > 0 and temp_length + 1 > max_length:
                    max_length = temp_length + 1
                    longest_str = s[(i-j):(i+j+1)]
                    
        return longest_str


string = "aaa"
solution = Solution()
print(solution.longestPalindrome(string))

