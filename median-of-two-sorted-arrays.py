class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) != 1 or len(nums2) != 1:
            
            print(nums1)
            if len(nums1) % 2 == 0:
                # nums1 has even number of element
                median_1 = (nums1[len(nums1)//2 - 1] + nums1[len(nums1)//2])/2
                median_1_left = len(nums1)//2 - 1
                median_1_right = len(nums1)//2
            else:
                # nums1 has odd number of element
                median_1 = nums1[len(nums1) // 2]
                if len(nums1) == 1:
                    median_1_left = median_1_right = 0
                else:
                    median_1_left = len(nums1) // 2 - 1
                    median_1_right = len(nums1) // 2 + 1
            
            print(nums2)
            if len(nums2) % 2 == 0:
                # nums2 has even number of element
                median_2 = (nums2[len(nums2)//2 - 1] + nums2[len(nums2)//2])/2
                median_2_left = len(nums2)//2 - 1
                median_2_right = len(nums2)//2
            else:
                # nums1 has odd number of element
                median_2 = nums2[len(nums2) // 2]
                if len(nums2) == 1:
                    median_2_left = median_2_right = 0
                else:
                    median_2_left = len(nums2) // 2 - 1
                    median_2_right = len(nums2) // 2 + 1
                
            if median_1 > median_2:
                print("case 1")
                sub_nums1 = nums1[0:(median_1_left+1)]
                sub_nums2 = nums2[median_2_right:]
                print([median_1_left, median_2_right, sub_nums1, sub_nums2])
                return self.findMedianSortedArrays(sub_nums1, sub_nums2)
            elif median_1 < median_2:
                print("case 2")
                sub_nums1 = nums1[median_1_right:]
                sub_nums2 = nums2[0:(median_2_left+1)]
                print([median_1_right, median_2_left, sub_nums1, sub_nums2])
                return self.findMedianSortedArrays(sub_nums1, sub_nums2)
            else:
                return median_1
        else:
            return (nums1[0] + nums2[0])/2

solution = Solution()
nums1 = [1, 2, 3, 5, 10]
nums2 = [3, 4]
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)
assert result == 5