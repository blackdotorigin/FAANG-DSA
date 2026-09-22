'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
 
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

'''
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first_occurence = float("inf")
        low,high = 0,len(nums)-1

        # Find the first Occurence
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                first_occurence = min(first_occurence,mid)
                high = mid-1

            elif nums[mid] > target:
                high = mid-1

            else:
                low = mid+1


        #  Skip Early if first Occurance is not found
        if first_occurence == float("inf"):
            return [-1,-1]

        # Find the Last Occurence
        last_occurance = float("-inf")
        low = first_occurence if first_occurence != float("inf") else 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                last_occurance = max(first_occurence,mid)
                low = mid+1

            elif nums[mid] > target:
                high = mid-1

            else:
                low = mid+1

        return [first_occurence,last_occurance] if first_occurence  != float("inf") else [-1,-1]

sol = Solution()
print(sol.searchRange([5,6,7,7,8,8,10],1))