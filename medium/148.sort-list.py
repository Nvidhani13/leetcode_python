#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (58.56%)
# Likes:    11584
# Dislikes: 346
# Total Accepted:    823.5K
# Total Submissions: 1.4M
# Testcase Example:  '[4,2,1,3]'
#
# Given the head of a linked list, return the list after sorting it in
# ascending order.
# 
# 
# Example 1:
# 
# 
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# 
# 
# Example 3:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 5 * 10^4].
# -10^5 <= Node.val <= 10^5
# 
# 
# 
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory
# (i.e. constant space)?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_mid(self,head):
        slow=head
        fast=head
        prev=head
        while(fast and fast.next):
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=None
        return slow
        
    def merge_list(self,left,right):
        # print("now loooooooook at merge list ")
        dummy=ListNode(0)
        tail=dummy
        
        while(left and right):
            if( left.val<right.val):
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next
            tail=tail.next
        tail.next=left if left else right 
        # print("this was dummy next",dummy.next)
        
        return dummy.next
        

       
        
        


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print("sort list ")
        if(not head or not head.next):
            return head
        mid=self.find_mid(head)
        # print("this is mid ",mid )
        
        # print("this is head",head)
        left=self.sortList(head)
        # print("this was left ",left )
        right=self.sortList(mid)
        # print("this was right ",right )
        
        
        return self.merge_list(left,right)
        
        
                
        
        
    
        
# @lc code=end

