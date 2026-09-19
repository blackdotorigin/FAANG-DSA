'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -


sol = Solution()
print(sol.strStr("badbutsad","sad")) 1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                j,k = 1,i+1
                while j < len(needle):
                    if not needle[j] == haystack[k]:
                        break
                    j+=1
                    k+=1
                if j == len(needle):
                    return i
        return -1