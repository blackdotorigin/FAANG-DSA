'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:
1 <= n <= 8
'''
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        self.solve(0,0,result,n,"")
        return result

    def solve(self,open_count,closed_count,result,n,steps):
        if open_count - closed_count == 0 and open_count == n:
            result.append(steps)

        #Open a bracket
        if open_count < n:
            self.solve(open_count+1,closed_count,result,n,steps+"(")
        #Close a bracket
        if closed_count < open_count:
            self.solve(open_count,closed_count+1,result,n,steps+")")


sol = Solution()
print(sol.generateParenthesis(3))