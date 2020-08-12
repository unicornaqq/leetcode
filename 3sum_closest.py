""" 
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4 

if I sort the nums => [-4, -1, 1, 1*, 2]

"""

class Solution:
    def threeSum(self, nums, target, hash_table):
        # print("target is {}".format(target))
        result = []
        # init the hash table for later usage
        if len(nums) < 3:
            return result
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):                        
                index = hash_table.get(target - nums[i] - nums[j])
                if index != None and index != i and index != j:                
                    result = [nums[i], nums[j], nums[index]]
        return result
    
    def threeSumClosest(self, nums, target: int) -> int:
        
        hash_table = dict()
        for (index, number) in enumerate(nums):
            hash_table[number] = index
        
        result = None
        for i in range(0, max(abs(3000-target), abs(-3000-target))+1):
            result = self.threeSum(nums, target+i, hash_table)
            if len(result) != 0:
                return sum(result)
            else:
                result = self.threeSum(nums, target-i, hash_table)
                if len(result) != 0:
                    return sum(result)
        return result
    
    
list = [-1,2,1,-4]
target = -10000
solu = Solution()
print(solu.threeSumClosest(list, target))
                
