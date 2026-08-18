'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        starting,maxi= 0,0

        for i in range(len(s)):
            odd_palindrome,odd_starting= self.check_palindrome(i,i,s)
            even_palindrome,even_starting = self.check_palindrome(i,i+1,s)

            if max(odd_palindrome,even_palindrome) > maxi:
                maxi = max(odd_palindrome,even_palindrome)
                starting = odd_starting if odd_palindrome > even_palindrome else even_starting

        return s[starting:starting+maxi]

    def check_palindrome(self,left,right,s)->tuple[int,int]:
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right +=1

        return right-left-1,left+1


    