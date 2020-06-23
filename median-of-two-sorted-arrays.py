import sys

class Solution:

    def find_kth_element(self, nums1, nums2, begin1, begin2, k):
        print(nums1[begin1:])
        print(nums2[begin2:])
        print(k)

        """ if begin1 >= len(nums1):
            # all elements of nums1 are kicked-out
            return nums2[begin2 + k - 1] """
        
        if begin1 >= len(nums1):
            # all elements of nums1 kicked out
            # kth elements comes from nums2
            return nums2[begin2 + k -1]
        if begin2 >= len(nums2):
            return nums1[begin1 + k - 1]
        
        if k == 1:
            if nums1[begin1] < nums2[begin2]:
                return nums1[begin1]
            else:
                return nums2[begin2]     

            

        if begin1 + k//2 > len(nums1):
            # nums1 doesn't have so many elements
            # get rid of other arrays k//2 elements
            eleNum1 = sys.maxsize
        else:
            eleNum1 = nums1[begin1 + k//2 -1]
        
        if begin2 + k//2 > len(nums2):
            eleNum2 = sys.maxsize
        else:
            eleNum2 = nums2[begin2 + k//2 - 1]

        if eleNum1 > eleNum2:
            # get rid of k//2 elements from nums2
            begin1 = begin1
            begin2 = begin2 + k//2
            k = k - k//2
            return self.find_kth_element(nums1, nums2, begin1, begin2, k)
        else:
            begin1 = begin1 + k//2
            begin2 = begin2
            k = k - k//2
            return self.find_kth_element(nums1, nums2, begin1, begin2, k)


    def findMedianSortedArrays(self, nums1, nums2):
        left = (len(nums1) + len(nums2) + 1)//2
        right = (len(nums1) + len(nums2) + 2)//2
        if left == right:
            return self.find_kth_element(nums1, nums2, 0, 0, left) 
        else:
            return (self.find_kth_element(nums1, nums2, 0, 0, left) + self.find_kth_element(nums1, nums2, 0, 0, right))/2


""" solution = Solution()
nums1 = [1, 2, 3, 5, 10]
nums2 = [3, 4]
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)
assert result == 3

nums1 = [-5, 1, 2,3]
nums2 = [-1, 3]
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)
assert result == 1.5 """


solution = Solution()
nums1 = [-5, 1, 2,3, 7, 9]
nums2 = [-80, -7]
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)
assert result == 1.5

