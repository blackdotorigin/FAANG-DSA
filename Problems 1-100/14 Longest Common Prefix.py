'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''

class Solution1:
    # Better Approch
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i > len(word)-1 or word[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


''' Trie Solution is down Below'''

# Using Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self,word:str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.ends = True

    def longest_common_prefix(self,strs):
        node = self.root
        count = 0
        while len(node.children) <= 1 and not node.ends:
            if count > len(strs[0])-1:
                break
            node = node.children[strs[0][count]]
            count +=1
        return strs[0][:count]

class Solution2:
    def longestCommonPrefixTrie(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        trie:Trie = Trie()
        for word in strs:
            trie.insert(word)
        return trie.longest_common_prefix(strs)

