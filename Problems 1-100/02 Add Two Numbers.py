'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Pythonic Way
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1 = ""
        ll2 = ""
        while l1 :
            ll1 += str(l1.val)
            l1 = l1.next
        while l2:
            ll2 += str(l2.val)
            l2 = l2.next
        result = str(int(ll1[::-1]) + int(ll2[::-1]))
        head = ListNode(0)
        dummy = head
        while len(result):
            dummy.next = ListNode(result[-1])
            result =  result[:-1]
            # 801 => res[::] => res[:-1:] +> 80
            dummy = dummy.next
        return head.next

    def solve(self,l1,l2):
        carry = 0
        head = ListNode(0)
        dummy = head
        while l1 or l2 or carry:
            tot1 = l1.val if l1 else 0
            tot2 = l2.val if l2 else 0
            res = tot1 + tot2 + carry
            dummy.next = ListNode(res%10)
            dummy = dummy.next
            carry = res // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next




    


            

        