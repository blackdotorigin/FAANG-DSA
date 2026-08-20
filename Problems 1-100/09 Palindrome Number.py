'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:
-2**31 <= x <= 2**31 - 1
'''
class Solution:
    def isPalindromeString(self, x: int) -> bool:
        # using String
        if x < 0:
            return False
        x_str = str(x)
        return int(x_str[::-1]) == x

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ans = 0
        original = x

        while x:
            digit = x % 10
            ans = ans * 10 + digit
            x //= 10
        return ans == original

    def isPalindromeNegative(self, x: int) -> bool:
            ans = 0
            x = abs(x)
    
            while x:
                digit = x % 10
                ans = ans * 10 + digit
                x = x//10
            return ans == x

sol = Solution()
print(sol.isPalindromeNegative(-1331))
    