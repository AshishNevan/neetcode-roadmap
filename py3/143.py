# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def travsere(self, head: Optional[ListNode]):
            if head.next == None:
                return
            print(head.val)
            travsere(head.next)

        travsere(head)
