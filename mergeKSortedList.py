""" Given an array of linked-lists lists, each linked list is sorted in ascending order.

Merge all the linked-lists into one sort linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: [] """

# How do we know which one from which list is bigger? 


from sortedList import ListNode
from sortedList import list_to_singly_linked_list
from sortedList import print_singly_linked_list

class Solution:
    def merge(self, lists):
        # print(lists)
        k = len(lists)
        if k == 0:
            return None
        elif k == 1:
            return lists[0]
        elif k == 2:
            head = None
            result = None
            current = None
            ele1 = lists[0]
            ele2 = lists[1]
            while ele1 is not None or ele2 is not None:
                if ele1 is not None and ele2 is not None:
                    if ele1.val <= ele2.val:
                        result = ele1
                        ele1 = ele1.next
                    else:
                        result = ele2
                        ele2 = ele2.next
                else:
                    if ele1 is None:
                        result = ele2
                        ele2 = ele2.next
                    else:
                        result = ele1
                        ele1 = ele1.next
                if head is None:
                    head = result
                    current = head
                else:
                    current.next = result
                    current = current.next
            return head
        else:
            return self.merge([self.merge(lists[0:k//2]), self.merge(lists[k//2:])])
                    
                    
    def mergeKLists(self, lists) -> ListNode:
        temp = self.merge(lists)
        # print_singly_linked_list(temp)
        return temp


lists = [[1,4,5],[1,3,4],[2,6]]
lists = []
lists = [[]]
linked_list = [list_to_singly_linked_list(e) for e in lists]
[print_singly_linked_list(elem) for elem in linked_list]
sol = Solution()
sol.mergeKLists(linked_list)
