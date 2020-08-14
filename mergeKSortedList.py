class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        

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