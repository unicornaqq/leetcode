""" Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
 """
class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    def inner_next(self, nums, offset):
        if offset == len(nums) - 1 or offset == len(nums):
            return False
        elif offset == len(nums) - 2:
            if nums[offset] >= nums[offset+1]:
                return False
            else:
                self.swap(nums, offset, offset+1)
                return True
        else:
            temp = nums[offset]
            if self.inner_next(nums, offset+1): # TODO: a new list, how to mapping the operation on the original list
            # all the operating is on the copied array. 
            # we need the action on the nums, but, the operation in this recursive to be limited to the copy of 
            # array only instead of the original array.
                return True
            else:
                slice_of_nums = nums[offset:]
                slice_of_nums.sort()
                # new_index = slice_of_nums.index(temp) #TODO: for the case of 1 1 5, need to go to 5 instead of 1.
                new_index = len(slice_of_nums) - 1 - slice_of_nums[::-1].index(temp)
                if new_index == len(slice_of_nums) - 1:
                    # the max case:
                    if offset == 0:
                        nums[:] = slice_of_nums # please note this assign method
                    return False
                else:
                    i = new_index + 1
                    while i > 0:
                        self.swap(slice_of_nums, i, i-1)
                        i -= 1
                    # assign the slice_of_nums back to nums
                    nums[offset:] = slice_of_nums
                    return True
        
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.inner_next(nums, 0)
        
sol = Solution()
nums = [7, 8, 3]
# [7, 8, 3] -> [8, 3, 7]
""" [1, 2, 3] -> [1, 3, 2] -> [2, 1, 3] -> [2, 3, 1] -> [3, 1, 2] -> [3, 2, 1] -> [1, 2, 3]
[1->0]
[2->1]
[3->2]
this is kind of loop of the sequence change, just find the next one in the loop given the sequence provided. """
# nums = [1, 3, 2]
# nums = [1, 2, 3]
# nums = [3, 2, 1]
nums = [1, 5, 1]
# nums = [9, 3, 2, 9, 8, 7]
sol.nextPermutation(nums)
print(nums)
                