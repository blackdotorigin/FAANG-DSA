'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''


from typing import Optional
import heapq
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = result = ListNode(0)
        counter = 0
        priority_queue = []
        for ll in lists:
            while ll :
                heapq.heappush(priority_queue,(ll.val,counter,ll)) # Creates a priority queue
                counter +=1
                ll = ll.next

        while priority_queue:
            value,counter,address = heapq.heappop(priority_queue)
            result.next = address
            result = result.next

        return dummy.next


# My Brute Force Approach:
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = dummy = ListNode(0)
        while lists:
            i = 0
            mini,address = float("inf"),None
            while i < len(lists):
                if lists[i] is None :
                    if lists[-1] is not None:
                        lists[i] = lists[-1]
                        lists.pop()
                    else:
                        lists.pop()
                        break
                if lists[i].val < mini:
                    mini,address = lists[i].val,i
                i+=1
            if lists and address is not None:
                res.next = lists[address] 
                res = res.next    
                lists[address] = lists[address].next
        return dummy.next



        

    



        

