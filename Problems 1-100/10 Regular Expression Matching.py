'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
Return a boolean indicating whether the matching covers the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        prev_res = [[-1 for _ in range(len(p))] for _ in range(len(s))]
        return self.memo(s,p,0,0,prev_res)

    def recursion(self,s:str,p:str,i:int,j:int)-> bool:
        # Base Condition
        if j == len(p):
            return i == len(s)

        # Check for match:
        match = False
        if i < len(s):
            match = s[i] == p[j] or p[j] == "."

        if j+1 < len(p) and p[j+1] == "*":
            # Skip use of * or  Make use of *
            return self.recursion(s,p,i,j+2) or (match and self.recursion(s,p,i+1,j))

        if not match:
            return False

        return self.recursion(s,p,i+1,j+1)

    def memo(self,s:str,p:str,i:int,j:int,prev_res:list[list[int]])-> bool:
            # Base Condition
            if j == len(p):
                return i == len(s)
            # Check for match:
            match = False
            if i < len(s):
                if prev_res[i][j] != -1:
                    return prev_res[i][j]
                match = s[i] == p[j] or p[j] == "."
    
            if j+1 < len(p) and p[j+1] == "*":
                # Skip use of * or  Make use of *
                return self.memo(s,p,i,j+2,prev_res) or (match and self.memo(s,p,i+1,j,prev_res))
    
            if not match:
                return False
            prev_res[i][j] = self.memo(s,p,i+1,j+1,prev_res)
            return prev_res[i][j]

    def tabulation(self,s,p):
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]

        # Base Case (0,0) True:
        dp[0][0] = True

        for j in range(2,len(p)+1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]

        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] == s[i-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    # Case * as 0 occurence
                    dp[i][j] = dp[i][j-2]

                    # Case * may be has an occurance
                    if p[j-2] == s[i-1] or p[j-2] == ".":
                        dp[i][j] = dp[i][j] or dp[i-1][j]

        return dp[len(s)][len(p)]



    def space_optimisation(self,s,p):
        prev = [False for _ in range(len(p)+1)]

        # Base Case (0,0) True:
        prev[0] = True

        for j in range(2,len(p)+1):
            if p[j-1] == "*":
                prev[j] = prev[j-2]

        for i in range(1,len(s)+1):
            curr  = [False for _ in range(len(p)+1)]
            for j in range(1,len(p)+1):
                if p[j-1] == s[i-1] or p[j-1] == ".":
                   curr[j] = prev[j-1]
                elif p[j-1] == "*":
                    # Case * as 0 occurence
                    curr[j] = curr[j-2]

                    # Case * may be has an occurance
                    if p[j-2] == s[i-1] or p[j-2] == ".":
                        curr[j] = curr[j] or prev[j]
            prev = curr
        return prev[len(p)]




sol = Solution()
print(sol.isMatch("mississippi","mis*is*p*."))

        