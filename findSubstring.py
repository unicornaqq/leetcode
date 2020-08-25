""" You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a 
concatenation of each word in words exactly once and without any intervening characters.

 

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: [] """

import json
class Solution:
    def findSubstring(self, s: str, words):
      if len(s) == 0 or len(words) == 0:
        return []
      result = []
      word_dict = {word: words.count(word) for word in words}
      #print(word_dict)
      original_copy = word_dict.copy()
      len_of_raw_string = len(s)
      len_of_sub = len(words[0])
      first_match = True
      temp = 0
      i = 0
      while i <= (len_of_raw_string-len_of_sub):
      # for i in range(0, len_of_raw_string-len_of_sub, len_of_sub):
        #print("i is {}".format(i))
        #print(s[i:len_of_sub+i])
        if (word := s[i:len_of_sub+i]) in words:
          #print(word)
          # before -1 from the dict, it is 0 already, means, we should start a new match instance
          # please note, the offset should continue from previous offset.
          if word_dict[word] == 0:
            word_dict = original_copy.copy()
            first_match = True
            i = temp + len_of_sub
            continue
          if first_match == True:
            temp = i
            first_match = False
          word_dict[word] -= 1
          if all(word_dict[key] == 0 for key in word_dict.keys()):
            # one full match is found
            word_dict = original_copy.copy()
            first_match = True
            result.append(temp)
            # at the same time, we need to go back to find another potential match
            i = temp
            word_dict = original_copy.copy()
        else:
          word_dict = original_copy.copy()
          first_match = True
          # i = temp
        #print(word_dict)
        if first_match == False:
          i += len_of_sub
        else:
          i += 1
      return result
      
sol = Solution()
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","good"]
# s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
# words = ["fooo","barr","wing","ding","wing"]
s = ""
words = []
s = "ababaab"
words = ["ab","ba","ba"]
print(sol.findSubstring(s, words))