'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
class Solution:
    # Brute Force
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        result = nums2 + nums1 # n + m
        result.sort() #O(m+n)log(n+m)
        res_len = len(result)
        even = len(result) % 2 == 0
        if even:
            median = (result[res_len//2-1] + result[res_len//2] ) / 2.0
        else:
            median = result[res_len//2]
        return median

    # Better Approach
    def better(self,nums1,nums2):
        i, j = 0,0
        result = []
        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and  (j>=len(nums2) or nums1[i] <= nums2[j]):
                    result.append(nums1[i])
                    i+=1
            elif j<len(nums2) and (i>=len(nums1) or nums1[i]>nums2[j]):
                result.append(nums2[j])
                j+=1
        # if j < len(nums2):
        #     while j<len(nums2):
        #         result.append(nums2[j])
        #         j+=1
        # if i < len(nums1):
        #     while j<len(nums1):
        #         result.append(nums1[i])
        #         i+=1
        res_len = len(result)
        even = len(result) % 2 == 0
        if even:
            median = (result[res_len//2-1] + result[res_len//2] ) / 2.0
        else:
            median = result[res_len//2]
        return median


    def optimal(self,nums1,nums2):
        # Arange smaller arrange and bigger arrary
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        m,n = len(nums1),len(nums2)
        low,high = 0,m
        while low <= high:
            partition_left = (low+high)//2
            partition_right = (m+n+1)//2 - partition_left

            l1 = nums1[partition_left-1] if partition_left > 0 else float("-inf")
            r1 = nums1[partition_left] if partition_left < m else float("inf")
            l2 = nums2[partition_right-1] if partition_right > 0 else float("-inf")
            r2 = nums2[partition_right] if partition_right < n else float("inf")

            if l1<= r2 and l2 <= r1:
                return max(l1,l2) if (m+n) % 2 == 1 else (max(l1,l2)+min(r1,r2))/2
            elif l2 > r1:
                low = partition_left + 1
            else:
                high = partition_left - 1
                


sol = Solution()
print(sol.optimal([1,3],[2]))
