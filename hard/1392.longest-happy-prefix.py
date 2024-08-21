#
# @lc app=leetcode id=1392 lang=python3
#
# [1392] Longest Happy Prefix
#
# https://leetcode.com/problems/longest-happy-prefix/description/
#
# algorithms
# Hard (46.14%)
# Likes:    1362
# Dislikes: 38
# Total Accepted:    48K
# Total Submissions: 103.3K
# Testcase Example:  '"level"'
#
# A string is called a happy prefix if is a non-empty prefix which is also a
# suffix (excluding itself).
# 
# Given a string s, return the longest happy prefix of s. Return an empty
# string "" if no such prefix exists.
# 
# 
# Example 1:
# 
# 
# Input: s = "level"
# Output: "l"
# Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"),
# and suffix ("l", "el", "vel", "evel"). The largest prefix which is also
# suffix is given by "l".
# 
# 
# Example 2:
# 
# 
# Input: s = "ababab"
# Output: "abab"
# Explanation: "abab" is the largest prefix which is also suffix. They can
# overlap in the original string.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPrefix(self, s: str) -> str:
        #! This is very famous algo and is also used in knuth mo
        
# @lc code=end

