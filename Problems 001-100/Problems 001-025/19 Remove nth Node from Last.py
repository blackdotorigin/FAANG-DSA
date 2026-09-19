'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''

# Definition for singly-linked list.
# class listNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
class Solution:
    # Optimal Approach Using Window or Fast/Slow Pointer 
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slow = fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


    def removeNthFromEndBrute(self, head: Optional[listNode], n: int) -> Optional[listNode]:
        ll_lenght = self.findLenght(head)
        node = head
        traverse = ll_lenght-n
        if traverse == 0:
            return head.next
        count = 1
        while node and count<traverse:
            node = node.next
            count +=1
        if node:
            node.next = node.next.next
        return head

    def findLenght(self,head):
        count = 0
        while head:
            head = head.next
            count +=1
        return count

          