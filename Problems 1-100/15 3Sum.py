'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
Constraints:
3 <= nums.length <= 3000
-10**5 <= nums[i] <= 10**5
'''

class Solution1:
    # Brute Force
    def threeSumBrute(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        ans.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        return [list(valid) for valid in ans]


class Solution2:
    #Optimal Approach
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans  = set()
        nums.sort()
        for i in range(len(nums)-2):
            j,k= i+1,len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] == 0:
                    ans.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                    while j < k :
                        if nums[j] != nums[j-1]:
                            break
                        j+=1
                    while k > j:
                        if nums[k] != nums[k+1]:
                            break
                        k-=1
                elif nums[i]+nums[j]+nums[k] > 0:
                    k-=1
                else:
                    j+=1
        return [list(elements) for elements in ans]