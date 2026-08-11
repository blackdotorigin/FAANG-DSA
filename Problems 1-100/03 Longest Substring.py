'''
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        for i in range(len(s)):
            char = s[i]
            char_set = set()
            char_set.add(s[i])
            for j in range(i+1,len(s)):
                if s[j] not in char_set:
                    char+= s[j]
                    char_set.add(s[j])
                else:
                    break
            result = char if len(char) > len(result) else result
        return result

    def optimal(self,s:str)->int:
        result = ""
        char_dict = dict()
        i,j = 0,0
        while j < len(s):
            if s[j] in char_dict and char_dict[s[j]] >= i:
                result = result if j-i < len(result) else s[i:j]
                i = char_dict[s[j]] + 1
                char_dict[s[j]] = j
            else:
                char_dict[s[j]] = j
            j+=1
        return result




sol = Solution()
print(sol.optimal("abcabcbb"))
