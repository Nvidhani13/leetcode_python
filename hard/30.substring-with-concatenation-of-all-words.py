#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (32.62%)
# Likes:    1885
# Dislikes: 271
# Total Accepted:    475.2K
# Total Submissions: 1.5M
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string s and an array of strings words. All the strings of
# words are of the same length.
# 
# A concatenated string is a string that exactly contains all the strings of
# any permutation of words concatenated.
# 
# 
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef",
# "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is
# not a concatenated string because it is not the concatenation of any
# permutation of words.
# 
# 
# Return an array of the starting indices of all the concatenated substrings in
# s. You can return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# 
# Output: [0,9]
# 
# Explanation:
# 
# The substring starting at 0 is "barfoo". It is the concatenation of
# ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of
# ["foo","bar"] which is a permutation of words.
# 
# 
# Example 2:
# 
# 
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 
# Output: []
# 
# Explanation:
# 
# There is no concatenated substring.
# 
# 
# Example 3:
# 
# 
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 
# Output: [6,9,12]
# 
# Explanation:
# 
# The substring starting at 6 is "foobarthe". It is the concatenation of
# ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of
# ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of
# ["the","foo","bar"].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        word_len=len(words[0])
        n=len(s)
        m=len(words)
        window_size=m*word_len
        words_freq=Counter(words)
        result=[]
        for i in range(0,n - window_size+1):
            substring=s[i:i+window_size]
            current_words=[substring[j:j+word_len] for j in range(0,window_size,word_len)]
            current_words_freq=Counter(current_words)
            if(current_words_freq == words_freq) :
                result.append(i)
        
        return result

        
# @lc code=end

