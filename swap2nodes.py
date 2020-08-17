# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

""" Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3. """

from sortedList import ListNode, list_to_singly_linked_list, print_singly_linked_list

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        index = 0
        current = None
        prev = None
        prev_prev = None
        current = head
        while current is not None:
            if index % 2 == 1:
                # print(index)
                prev.next = current.next
                current.next = prev
                if prev_prev is not None:
                    prev_prev.next = current 
                if prev == head:
                    head = current
                temp = prev
                prev = current
                current = temp
            prev_prev = prev
            prev = current
            current = current.next
            print(prev_prev.val if prev_prev is not None else None, 
                  prev.val if prev is not None else None, 
                  current.val if current is not None else None)
            index += 1
        return head

sol = Solution()
for my_list in [[1, 2, 3, 4, 5],
                [],
                [1, 2, 3, 4, 5, 6],
                [1],
                [1, 2]]:
    swapped_sorted_list = sol.swapPairs(list_to_singly_linked_list(my_list))
    print_singly_linked_list(swapped_sorted_list)