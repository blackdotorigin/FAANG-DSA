'''
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.


Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_target = float("inf")
        for i in range(0,len(nums)-2):
            j,k = i+1,len(nums)-1
            while j < k:
                sum = nums[i]+nums[j]+nums[k]
                if sum == target:
                    return sum
                elif target - sum > 0:
                    closest_target = sum if abs(target-sum) < abs(target-closest_target) else closest_target
                    j+=1
                else:
                    closest_target = sum if abs(target-sum) < abs(target-closest_target) else closest_target
                    k-=1
        return closest_target
sol = Solution()
print(sol.threeSumClosest(nums = [10,20,30,40,50,60,70,80,90], target = 1))