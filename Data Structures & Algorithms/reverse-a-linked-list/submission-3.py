# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# this is the solution wrote by myself on 20260526
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
     
       
        # I will use pointer
        curr = head # the current node i am processing
        prev = None # and this is the previos node

        
        while curr: # using iterative method
 
            next_node = curr.next # before reverse curr next, i have to store the curr next, otherwise will lose the rest of the list
            curr.next = prev # then i reverse the pointer by setting this
            # and move both pointer forward
            prev = curr
            curr = next_node
        
        # when curr becomes none, it means we have process to the tail of the linked list
        # prev will be the new head of the reversed list
        return prev



        