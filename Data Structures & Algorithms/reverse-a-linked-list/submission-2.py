# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# this is the solution wrote by myself on 20260526
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
     
       
        # initiate two pointer
        curr = head
        prev = None
        # using iterative method
        while curr:
            
            # we have to make prev to become curr next
            # we use a variable to store the curr.next before we change the curr so we wont lost that ref info
            next_node = curr.next
            curr.next = prev
            # we move the two pointer forward 
            prev = curr
            curr = next_node
        
        # if curr is none, it means we have process to the tail of the linked list
        return prev



        