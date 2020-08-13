""" Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass? """

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        last = 0
        ele = None
        prev = None
        while current != None:
            if last == n-1:
                ele = head
            current = current.next
            last += 1
            if current is None:
                # we have reached the end of the list
                # so, current ele is the nth element from the 
                # end
                if ele == head:
                    head = head.next
                else:
                    prev.next = ele.next
                    ele.next = None
                return head
            else:    
                if ele is not None:
                    prev = ele
                    ele = ele.next


def list_to_singly_linked_list(list):
    prev = None
    head = None
    for (i, ele) in enumerate(list):
        node = ListNode(ele)
        if i == 0:
            head = node
        if prev is not None:
            prev.next = node
        prev = node
    return head

def print_singly_linked_list(head):
    current = head
    result = []
    while current is not None:
        result.append(current.val)
        current = current.next
    print(result)


list = [1]
n = 1

sol = Solution()
head = list_to_singly_linked_list(list)
print_singly_linked_list(head)
print_singly_linked_list(sol.removeNthFromEnd(head, n))              