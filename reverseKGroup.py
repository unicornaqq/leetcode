""" Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed. 


How to handle the case when the length of the list is not multiple of k?
user two pointer,

suppose k is 3:
1 2 3 4 5 6 7
0 1 2 k 0 1 2


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from sortedList import ListNode, list_to_singly_linked_list, print_singly_linked_list
from stack import StackElement, Stack

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or k == 0:
            return head
        current = None
        new_current = None
        new_head = None
        first_element = None
        stack = Stack()
        i = 0
        current = head
        while current is not None:
            # print("the current value is {}".format(current.val))
            if i == 0:
                first_element = current
                i += 1
                temp = current.next
            elif i < k-1:
                # print("push the {}th element".format(i))
                # temp = current.next
                # current.next = None
                # elem = StackElement(current)
                # stack.push(elem)
                i += 1
                temp = current.next
            else:
                i = 0
                push_temp = first_element
                while push_temp != current:
                    temp = push_temp.next
                    push_temp.next = None
                    elem = StackElement(push_temp)
                    stack.push(elem)
                    push_temp = temp
                
                if new_head == None:
                    new_head = current
                temp = current.next
                if new_current != None:
                    new_current.next = current
                new_current = current
                
                elemFromStack = stack.pop()
                while elemFromStack != None:
                    # print("the poped ele is {}".format(elemFromStack.val.val))
                    elem = elemFromStack.val
                    new_current.next = elem
                    new_current = elem
                    elemFromStack = stack.pop()

            if temp == None and i!= 0:
                # we have reached to the end of the list, need to add all the element staring from first element to the original list.
                temp = first_element;
                while temp != None:
                    if new_current == None:
                        new_current = temp
                        new_head = temp
                        break
                    else:
                        new_current.next = temp
                        new_current = temp
                        temp = temp.next
                break
            current = temp
            # print_singly_linked_list(new_head)
        return new_head
    
sol = Solution()
k = 1
list = [1, 2, 3, 4, 5]
# list = []
# list = [1]
# list = [1, 2, 4 , 9, 10, 30, 11, 12]
result = sol.reverseKGroup(list_to_singly_linked_list(list), k)
print_singly_linked_list(result)
                            
                
            
            
        
            