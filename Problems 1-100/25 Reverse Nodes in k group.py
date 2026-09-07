'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
 
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
'''
from typing import Optional

def create_linked_list(nums):
    head = root = ListNode(0)

    for num in nums:
        head.next = ListNode(num)
        head = head.next

    return root.next


def print_ll(head):
    while head:
        print(head.val,"->",end="")
        head = head.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1 : Initiilise the variables
        next_node_address = prev_batch_end = head
        prev_batch_start = root = ListNode(0)

        # Step 2 : Repets the flow
        while next_node_address:
            next_node_address,is_valid = self.get_next_batch_address(prev_batch_end,k)
            if is_valid:
                prev_batch_start.next  = self.reverse_k_elements(prev_batch_end,k)
                prev_batch_start = prev_batch_end
                prev_batch_end = next_node_address
            else:
                prev_batch_start.next = next_node_address
                next_node_address = None

        return root.next


    def get_next_batch_address(self,node,k):
        root = node
        while node and k:
            node = node.next
            k-=1

        return (node,True) if k == 0 else (root,False)

    def reverse_k_elements(self,head,k):
        prev = None
        while head and k:
            curr = head
            future = curr.next
            curr.next = prev
            prev = curr
            head = future
            k-=1
        return prev


sol = Solution()
print_ll(sol.reverseKGroup(create_linked_list([1,2,3,4,5]),3))

