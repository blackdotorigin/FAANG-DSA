'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"


Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR 

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
'''

class Solution:
    # Better 
    def solve(self,s:str,numRows:int)->str:
        if numRows == 1 or numRows >= len(s):
            return s
        table = [[-1 for _ in range(len(s))]for _ in range(numRows)]
        letters_count = 0
        j = 0
        while letters_count < len(s):
            # Fill Downwards
            for i in range(numRows):
                if letters_count >= len(s):
                    break
                table[i][j] = s[letters_count]
                letters_count+=1

            j+=1

            # Fill Diagonally
            for i in range(numRows-2,0,-1):
                if letters_count >= len(s):
                    break
                table[i][j] = s[letters_count]
                letters_count+=1
                j+=1
        ans = ""
        for row in table:
            for char in row:
                if char != -1:
                    ans+=char
        return ans

    def best(self,s:str,numRows:int)->str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = ["" for _ in range(numRows)]
        pos = 0
        moving_down = False
        for char in s:
            res[pos] += char

            # Check for moving down
            if pos == 0 or pos == numRows-1:
                moving_down = not moving_down

            # Update pos
            pos = pos+1 if moving_down else pos-1
        return "".join(res)
            

sol = Solution()
print(sol.best("PAYPALISHIRING",4))