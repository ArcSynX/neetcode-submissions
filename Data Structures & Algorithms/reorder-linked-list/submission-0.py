# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # first find the middle of the linke list
        # second, reverse the second half
        # finally, merge the first half and reversed second half alternately

        # step 0: deal with null or single link list
        if not head or not head.next:
            return 

        # step 1
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # step 2 cut in half
        second = slow.next # head of the second half
        slow.next = None # cut the first half

        # step 2 reverse the second half
        # we wanna make curr.next point to prev
        # and move forward the two pointer
        # use two pointer
        prev = None
        curr = second

        while curr: 
            # we first store it
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        second = prev

        # step 4: we merge two link list alternately
        first = head

        # we keep doing this until the second is none
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second 
            second.next = tmp1

            first = tmp1
            second = tmp2

 




        