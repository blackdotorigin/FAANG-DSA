'''
You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation:
There is no concatenated substring.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].



Constraints:
1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
'''


# Brute Force
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        combinations = set()
        pos_used = [0] * len(words)
        self.recursion(words,pos_used,combinations,"")
        result = []
        for word in combinations:
            value = self.strStr(s,word)
            if value:
                for val in value:
                    result.append(val)
        result.sort()
        return result
        

    def strStr(self, haystack: str, needle: str) -> int:
            if not haystack or len(needle) > len(haystack):
                return []
            ans = []
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i] == needle[0]:
                    j,k = 1,i+1
                    while j < len(needle):
                        if not needle[j] == haystack[k]:
                            break
                        j+=1
                        k+=1
                    if j == len(needle):
                        ans.append(i)
            return ans

    def recursion(self,words,pos_used,combinations,flow_res):
        if sum(pos_used) == len(words):
            combinations.add(flow_res)
            return

        for i in range(len(words)):
            if pos_used[i]:
                continue
            pos_used[i] = 1
            self.recursion(words,pos_used,combinations,flow_res+words[i])
            pos_used[i] = 0



# Optimal approach

class Optimal:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_dict = {}
        for word in words:
            # if word in word_dict:
            #     word_dict[word] += 1
            # else:
            #     word_dict[word] = 1
            word_dict[word] = word_dict.get(word,0)+1


        window_size = len(words) * len(words[0])
        chunk_size = len(words[0])
        result = []
        for i in range(len(s)):
            seen = {}
            valid = True
            for j in range(i,i+window_size,chunk_size):
                chunk = s[j:j+chunk_size]
                print(chunk)
                if chunk not in word_dict:
                    valid = False
                    break    
                seen[chunk] = seen.get(chunk,0)+1
                if seen[chunk] > word_dict[chunk]:
                    valid = False
                    break
            if valid:
                result.append(i)

        return result
            