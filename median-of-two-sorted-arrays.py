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
            # all elements of nums1 kicked out, there is no elements in nums1
            # kth elements comes from nums2
            return nums2[begin2 + k -1]
        if begin2 >= len(nums2):
            return nums1[begin1 + k - 1]
        
        if k == 1:
            # just need to find 1 element.
            if nums1[begin1] < nums2[begin2]:
                return nums1[begin1]
            else:
                return nums2[begin2]     


        """ The logic:
            if k//2 th element of nums1 is larger than k//2 th element of nums2
            it means the fist k//2 element from nums2 must be in the final list 
            with k elements.
            For example:
            Suppose k = 5
            nums1 = [-5, 1, 2, 3] k//2 th element => 1
            nums2 = [-100, 0, 5, 20] k//2 th element => 0
            1 > 0 => eleNum1 > eleNum2
            so, [-100, 0] must be part the final k elements, all the above deduction is based on the
            assumption that both nums1 and nums2 are ordered.
            
            Further thought:
            ================
            Divide the problem into 2 k//2 problems.
            For the 1st k//2 problem, we compare the k//2 th element of two arrays.
            The first k//2 elements of the array with smaller k//2 element, should be part of the final k elements list.
            Now, suppose nums1 is that smaller array.
                [left part of nums2, (k//2 elements from nums1), right part of nums2, k//2 of nums2]
            This is a general layout of the k element from nums1 and nums2, [left part of nums2] or [right part of nums2] could be empty.
            k//2 elements from nums1 can interleaved with elements of nums2.
            We can say for sure that none of the k//2 elements from nums1 can be the k th element.
            We need to find another k//2 elements from the joint nums1-[k//2 elements from nums1] and nums2.
            For the case shows in the general layout, the final result containing k elements could be as below:
                [left part of nums2, (k//2 elements from nums1), (part of nums1 started from k//2 + 1), right part of nums2] or 
                [left part of nums2, (k//2 elements from nums1), right part of nums2, (part of nums1 started from k//2 + 1)]
            Do we have another element that can push the (k//2 elements from nums1) out of the final array? 
            The answer is NO, that is because all the left parts ([k//2:]) either from nums1 or nums2 are bigger than (k//2 elements from nums1).
            
        """
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
        # please note the numbering is for the joint list with both nums1 and nums2
        left = (len(nums1) + len(nums2) + 1)//2
        right = (len(nums1) + len(nums2) + 2)//2
        if left == right:
            return self.find_kth_element(nums1, nums2, 0, 0, left) 
        else:
            # follow the direct meaning of median (left+right/2)
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

