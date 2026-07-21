# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head  == None:
            return head 
        else:
            odd = head
            even=odd.next
            temp = even
            while  odd.next is not None and even.next is not None :
                odd.next = even.next
                even.next = even.next.next
                odd=odd.next
                even=even.next
        odd.next = temp     
        return head     

