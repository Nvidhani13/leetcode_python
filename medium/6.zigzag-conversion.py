#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (48.51%)
# Likes:    7640
# Dislikes: 14643
# Total Accepted:    1.4M
# Total Submissions: 2.9M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
# 
# Example 3:
# 
# 
# Input: s = "A", numRows = 1
# Output: "A"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 : 
            return s
        answer = ""
        currRow = 0 
        s_size = len(s)-1
        for i in range(0 , numRows) : 
            answer += s[i]
            next_index= 2 * numRows - 2 * currRow - 2

            while next_index < s_size :
                answer += s[next_index]
                next_index += 2 * numRows - 2 * currRow - 2
            
            currRow += 1
        
        return answer

            

            


        
# @lc code=end

