'''
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

'''
# Brute Force
class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target-nums[i]:
                    return [i,j]

# Optimal 
# o(n2) -> O(N)
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = dict()
        for i in range(len(nums)):
            num_dict[nums[i]] = i

        print(num_dict)
        for i in range(0,len(nums)):
            if target-nums[i] in num_dict and i != num_dict[target-nums[i]]:
                return [i,num_dict[target-nums[i]]]


sol = Solution2()
print(sol.twoSum([3,2,4],6))

