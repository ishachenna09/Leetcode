# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        slow = head
        fast=head
        #finding mid point 
        while fast.next and fast.next.next:
            # prev=slow
            slow = slow.next
            fast=fast.next.next
        # print("mid ",slow.val) 

        mid=slow
        # reversing 
        prev= None
        current = slow.next
        while current:
            nex = current.next
            current.next = prev
            prev=current
            current=nex
        # print("reverse head", prev.val)    
        
    #    checking palindrome
        mid.next=None
        current =head
        while current and prev :
            # print("current.val , prev.val", current.val , prev.val ) 
            if current.val == prev.val:
                current=current.next
                prev=prev.next
                # return False
            else:
                return False        
        return True



        

