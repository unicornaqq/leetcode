class Solution:
    def threeSum(self, nums, target, hash_table, current):
        # init the hash table for later usage

        my_set = set()
        for i in range(len(nums)):
            if i == current:
                continue
            for j in range(i+1, len(nums)):
                if j == current:
                    continue                     
                index = hash_table.get(target - nums[i] - nums[j])
                # print("i={}, j={}, index={}, current={}".format(i, j, index, current)) 
                if index != None and index > i and index > j and index != current:
                    temp = tuple(sorted((nums[j], nums[index], nums[i], nums[current])))
                    my_set.add(temp)
        return [[num for num in elem] for elem in my_set]
    
    def fourSum(self, nums, target):
        result = []
        nums.sort()
        if len(nums) < 4:
            return []
        
        hash_table = dict()
        for (index, number) in enumerate(nums):
            hash_table[number] = index
        
        my_set = set()    
        for (i, ele) in enumerate(nums):
            if i > 0 and ele == nums[i - 1]:
                continue
            else:
                new_target = target-ele
                # print([new_target, i])
                if new_target < nums[i]*3 or new_target > nums[-1]*3:
                    continue
                temp = self.threeSum(nums, new_target, hash_table, i)
                if len(temp) != 0:
                    [my_set.add(tuple(ele3)) for ele3 in temp]
        
        return [[num for num in elem] for elem in my_set]                
            


sol = Solution()
list = [1, 0, -1, 0, -2, 2]
# list = [0,0,0,0]
list = [0,4,-5,2,-2,4,2,-1,4]
target = 12
print(sol.fourSum(list, target))