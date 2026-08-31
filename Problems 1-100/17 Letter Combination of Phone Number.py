'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = "2"
Output: ["a","b","c"]
 
Constraints:
1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        self.num_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        ans_list = []
        self.solve(0,digits,ans_list,"")
        return ans_list


    def solve(self,pos,digits,ans_list,flow_res):
        if pos >= len(digits):
            ans_list.append(flow_res)
            return

        for char in self.num_map[digits[pos]]:
            self.solve(pos+1,digits,ans_list,flow_res+char)

sol = Solution()
print(sol.letterCombinations("23"))