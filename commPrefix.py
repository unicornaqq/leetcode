class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''
        result = ''
        for (i, char) in enumerate(strs[0]):
            if any([i >= len(elem) or elem[i] != char for elem in strs[1:]]):
                break
            else:
                result += char
        return result
    
mySul = Solution()
strs = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
print(mySul.longestCommonPrefix(strs))
print(mySul.longestCommonPrefix(strs2))