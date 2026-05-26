# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# this is my first attempt on 2026-05-26 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # first i make a fake starting node, 
        # since we dont know who is gonna be the head at the very beginning
        dummy = ListNode(0) # this is the head
        # then i use a tail pointer which always point to the last node of the merged list
        tail = dummy # at first, the tail is head 

        while list1 and list2:
            # i compare two linked list value
            if list1.val <= list2.val:
                tail.next = list1 # attach the smaller node to the tail.next
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
   
            tail = tail.next # then we move the list pointer forward

        # after the loop, if one of the list still have remaining nodes, I attached the list directly
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


        # Time complexity
        # O(m+n)
        # Space complexity
        # O(1)

                                