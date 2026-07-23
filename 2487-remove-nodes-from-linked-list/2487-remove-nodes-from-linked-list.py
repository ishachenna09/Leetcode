# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head:Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        prev = None
        while current :
            head.next = prev
            prev=head
            head=current
            current=current.next
        head.next=prev    
        # return head 
        # print(head.val)
        # traverse list if next elemnt is small delete it 
        current = head
        return head

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first reverse the list
        head=self.reverse(head)
        current=head
        while current.next:
            if current.next.val < current.val:
                current.next = current.next.next
            else:
                current=current.next
        return self.reverse(head)        


